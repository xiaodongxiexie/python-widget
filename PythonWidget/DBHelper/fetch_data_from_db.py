# coding: utf-8

import os
import time

from dataclasses import dataclass
from typing import TypeVar, List, Dict, Optional, Union
from enum import Enum, unique

import cx_Oracle as oracle
import psycopg2
import pymysql


# this can avoid err when use fetchall ^.^
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


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

    def __post_init__(self):
        self.user = self.config.get("user")
        self.ip = self.config.get("ip") or self.config.get("host")
        self.port = self.config.get("port")
        self.db = self.config.get("db") or self.config.get("database")
        self.passwd = self.config.get("passwd") or self.config.get("password")

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

    def connect_postgresql(self):
        connection = psycopg2.connect(
            host=self.ip,
            port=self.port,
            database=self.db,
            user=self.user,
            password=self.passwd,
        )
        return connection

    def connect(self):
        if isinstance(self.which_db, int):
            which_db = DBOption(self.which_db).name
        else:
            which_db = self.which_db
        self.db_name = which_db
        connection = getattr(self, "connect_" + which_db)()
        return connection

    def query(
                self,
                sql: str,
                nums: Optional[int] = None,
                style: str = "lower"
                ) -> List[Dict]:
        """sql attention:
        don't end with a semicolon or get a error.
        """
        connection = self.connect()
        with connection as conn:
            if self.db_name == "mysql":
                cursor = conn
            else:
                cursor = conn.cursor()
            try:
                cursor.execute(sql)
                logger.info(sql)
            except Exception as e:
                logger.exception(sql, exc_info=True)
            if self.db_name in ["mysql", "oracle"]:
                columns = [getattr(obj[0], style)() for obj in cursor.description]
            else:
                columns = [getattr(obj.name, style)() for obj in cursor.description]
            if nums is None:
                rets = cursor.fetchall()
            else:
                rets = cursor.fetchmany(nums)
            rets = [dict(zip(columns, objs)) for objs in rets]
            return rets

    def insertmany(
                self, table_name: str,
                cols: Union[list, tuple],
                values: List[Union[list, tuple]],
                batch_size: int = 2000
                ) -> None:
        conn = self.connect()

        assert self.db_name == "oracle", "just support for Oracle"

        with conn:
            _insert_sql = """
            INSERT INTO {table_name} ({columns}) VALUES ({placeholder})
            """
            nums = len(cols)
            columns = ", ".join(cols)
            placeholder = (", ".join([":{}".format(i) for i in range(1, nums+1)]))
            insert_sql = _insert_sql.format(table_name=table_name,
                                            columns=columns,
                                            placeholder=placeholder,
                                            )
            i = 0
            _start = time.perf_counter()
            while i < len(values):
                start = time.perf_counter()
                i += batch_size
                curcor.executemany(insert_sql, values[i-batch_size:i])
                logger.info("{}: from:{} to {}".format(insert_sql, i-batch_size, i))
                conn.commmit()
                end = time.perf_counter()
                progressbar(
                    i,
                    len(values),
                    cur_consume_time=end - start,
                    total_consume_time=end - _start,
                            )
            print("insert into {} with {} rows success".format(table_name,
                                                               len(values)))
            
            
            
            
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
          
