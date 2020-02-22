# coding: utf-8

import os
import time
import logging

from dataclasses import dataclass
from functools import wraps
from typing import TypeVar, List, Dict, Optional, Union
from enum import Enum, unique

import cx_Oracle as oracle
import psycopg2
import pymysql

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


# this can avoid err when use fetchall ^.^
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class Elapsed:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        end = time.perf_counter()
        logger.info("%s elapsed time: %d", self.func.__name__, end - start)
        return result

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)
        
        
@dataclass
@unique
class DBOption(Enum):
    oracle: int = 1
    mysql: int = 2
    postgresql: int = 3


@dataclass
class FetchDataFromDB(object):
    config: Dict
    which_db: TypeVar("db", str, int)
    db_name = None

    # don't need set
    _connection_pool = None
    _use_pool = None

    def __post_init__(self):
        self.user = self.config.get("user")
        self.ip = self.config.get("ip") or self.config.get("host")
        self.port = self.config.get("port")
        self.db = self.config.get("db") or self.config.get("database")
        self.passwd = self.config.get("passwd") or self.config.get("password")
        self._connection_pool = None
        self._use_pool = None

    def connect_oracle(self):
        url = self.ip + ":" + self.port + "/" + self.db
        connection = oracle.connect(
            self.user,
            self.passwd,
            url,
        )
        return connection

    def connect_mysql(self):
        connection = pymysql.connect(
            host=self.ip,
            port=self.port,
            user=self.user,
            password=self.passwd,
            db=self.db,
            charset="utf8",
        )
        return connection

    def connect_postgresql(self, use_pool=True):
        """use connection pool for reuse"""

        db_cfg = dict(
            host=self.ip,
            port=self.port,
            database=self.db,
            user=self.user,
            password=self.passwd,
        )

        if self._connection_pool is None:
            self._connection_pool = ThreadedConnectionPool(
                minconn=10,
                maxconn=100,
                **db_cfg,
            )
        if use_pool:
            self._use_pool = True
            connection = self._connection_pool.getconn()
        else:
            connection = psycopg2.connect(**db_cfg)
        return connection

    def connect(self):
        if isinstance(self.which_db, int):
            which_db = DBOption(self.which_db).name
        else:
            which_db = self.which_db
        self.db_name = which_db
        connection = getattr(self, "connect_" + which_db)()
        return connection

    @Elapsed
    def query(
            self,
            sql: str,
            nums: Optional[int] = None,
            style: str = "lower"
    ) -> List[Dict]:
        """sql attention:
        don't end with a semicolon or get a error.
        """

        # 2019-12-02   add special treatment for connection pool
        connection = self.connect()
        conn = connection
        # with connection as conn:
        try:
            cursor = conn.cursor()
            try:
                with lock:
                    logger.info(sql)
                cursor.execute(sql)
            except Exception as e:
                with lock:
                    logger.exception(sql, exc_info=True)
            if cursor.description and list(cursor.description):
                if self.db_name in ["mysql", "oracle"]:
                    columns = [getattr(obj[0], style)() for obj in cursor.description]
                else:
                    columns = [getattr(obj.name, style)() for obj in cursor.description]
                if nums is None:
                    rets = cursor.fetchall()
                else:
                    rets = cursor.fetchmany(nums)
                rets = [dict(zip(columns, objs)) for objs in rets]
                with lock:
                    logger.info("--fetch end--".center(60, "*"))
            else:
                rets = []
                with lock:
                    logger.critical("no results get! check this")
        finally:
            flag = self._handle_connection_pool(conn)
            if not flag:
                conn.close()
        return rets

    def _handle_connection_pool(self, conn):
        if self._use_pool:
            if self._connection_pool is not None:
                try:
                    self._connection_pool.putconn(conn)
                except psycopg2.pool.PoolError:
                    logger.debug("just ignore ===> for future debug")
                    # logger.exception("just ignore ===> for future debug",
                    #                  exc_info=True)
                return True
        return False

    def closeall(self):
        if self.db_name == "postgresql":
            if self._connection_pool is not None:
                self._connection_pool.closeall()
                print("\n\n\nclose all connection\n\n\n")

    def insertmany(
            self, table_name: str,
            cols: Union[list, tuple],
            values: List[Union[list, tuple]],
            batch_size: int = 2000
    ) -> None:
        print("db_name  ==>  ", self.db_name)
        if self.db_name == "postgresql":
            self.gp_insertmany(table_name=table_name,
                               cols=cols,
                               values=values,
                               batch_size=batch_size)
        elif self.db_name == "oracle":
            self.oracle_insertmany(table_name=table_name,
                                   cols=cols,
                                   values=values,
                                   batch_size=batch_size)
        elif self.db_name == "mysql":
            self.mysql_insertmany(table_name=table_name,
                                  cols=cols,
                                  values=values,
                                  batch_size=batch_size)
        else:
            raise TypeError("just support Oracle and GP(PG)")

    def oracle_insertmany(
            self, table_name: str,
            cols: Union[list, tuple],
            values: List[Union[list, tuple]],
            batch_size: int = 2000
    ) -> None:
        conn = self.connect()

        # assert self.db_name in ("oracle", "gp", "pg"), "just support for Oracle and PG(GP)"

        try:
            cursor = conn.cursor()
            _insert_sql = """
            INSERT INTO {table_name} ({columns}) VALUES ({placeholder})
            """
            nums = len(cols)
            columns = ", ".join(cols)
            placeholder = (", ".join([":{}".format(i) for i in range(1, nums + 1)]))

            insert_sql = _insert_sql.format(table_name=table_name,
                                            columns=columns,
                                            placeholder=placeholder,
                                            )
            i = 0
            while i < len(values):
                i += batch_size
                cursor.executemany(insert_sql, values[i - batch_size:i])
                with lock:
                    logger.info("from:{} to {}".format(i - batch_size, i))
                conn.commit()
                
            print("insert into {} with {} rows success".format(table_name,
                                                               len(values)))
        finally:
            flag = self._handle_connection_pool(conn)
            if not flag:
                conn.close()

    def mysql_insertmany(
            self, table_name: str,
            cols: Union[list, tuple],
            values: List[Union[list, tuple]],
            batch_size: int = 10000
    ) -> None:
        conn = self.connect()
        try:
            cursor = conn.cursor()
            _insert_sql = """
            INSERT INTO {table_name} ({columns}) VALUES ({placeholder})
            """
            nums = len(cols)
            columns = ", ".join(cols)
            placeholder = (", ".join(["%s".format(i) for i in range(1, nums + 1)]))

            insert_sql = _insert_sql.format(table_name=table_name,
                                            columns=columns,
                                            placeholder=placeholder,
                                            )
            i = 0
            while i < len(values):
                i += batch_size
                cursor.executemany(insert_sql, values[i - batch_size:i])
                with lock:
                    logger.info("from:{} to {}".format(i - batch_size, i))
                conn.commit()
               
            print("insert into {} with {} rows success".format(table_name,
                                                               len(values)))
        except:
            conn.rollback()
            logger.fatal("向mysql插入数据失败，已回退~")
        finally:
            flag = self._handle_connection_pool(conn)
            if not flag:
                conn.close()

    def gp_insertmany(
            self, table_name: str,
            cols: Union[list, tuple],
            values: List[Union[list, tuple]],
            batch_size: int = 2000
    ) -> None:
        conn = self.connect()

        assert self.db_name in ("postgresql",), "just support for PG(GP)"

        nums = len(cols)
        columns = ", ".join(cols)
        _insert_sql = """
                    INSERT INTO {table_name} ({columns}) VALUES {placeholder}
                    """
        placeholder = ", ".join(["%s"] * nums)
        placeholder = "%s"
        insert_sql = _insert_sql.format(table_name=table_name,
                                        columns=columns,
                                        placeholder=placeholder,
                                        )
        try:
            cursor = conn.cursor()
            i = 0
            while i < len(values):
                i += batch_size
                placeholders = values[i - batch_size:i]
                # cursor.executemany(insert_sql, placeholders)
                execute_values(cursor, insert_sql, placeholders)
                with lock:
                    logger.info("from:{} to {}".format(i - batch_size, i))
                conn.commit()
               
            print("insert into {} with {} rows success".format(table_name,
                                                               len(values)))
        finally:
            flag = self._handle_connection_pool(conn)
            if not flag:
                conn.close()
            
            
            
  class Pagination:
    """
    docs:
        Reduce memory usage.
    attention:
        if you want execute fast, set batch_size a large num,
        H-O-W-E-V-E-R,
        this will increase memory usage,
        there are no free lunch, you should know.
    """

    debug = False

    def __init__(self, sql, execute_func, batch_size=100_000):
        self.sql = sql
        self.execute_func = execute_func
        self.batch_size = batch_size

    def preprocess(self):
        wrapped_sql = """
                    SELECT 
                        * 
                    FROM 
                        (SELECT 
                            ROWNUM rm, 
                            t.* 
                        FROM ({0}) t 
                        WHERE 
                            ROWNUM < {2}) 
                    WHERE rm >= {1}
                    """
        return wrapped_sql

    @Elapsed
    def postprocess(self):
        i, batch_size = 1, self.batch_size
        wrapped_sql = self.preprocess()
        while True:
            i += batch_size
            sql = wrapped_sql.format(self.sql, i-batch_size, i)
            data = self.execute_func(sql)
            if not data:
                break
            if self.debug:
                if i > batch_size * 3:
                    break
            yield data
          
