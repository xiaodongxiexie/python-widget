# coding: utf-8

from dataclasses import dataclass
from typing import TypeVar, List, Dict, Optional
from enum import Enum

import cx_Oracle as oracle
import psycopg2


@dataclass
class DBOption(Enum):
    oracle: int = 1
    mysql: int = 2
    postgresql: int = 3


@dataclass
class FetchDataFromDB(object):
    config: dict
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
        connection = oracle.connect(self.user,
                                    self.passwd,
                                    url)
        return connection

    def connect_mysql(self):
        pass

    def connect_postgresql(self):
        connection = psycopg2.connect(host=self.ip,
                                      port=self.port,
                                      database=self.db,
                                      user=self.user,
                                      password=self.passwd)
        return connection

    def connect(self):
        if isinstance(self.which_db, int):
            which_db = DBOption(self.which_db).name
        else:
            which_db = self.which_db
        self.db_name = which_db
        connection = getattr(self, "connect_" + which_db)()
        return connection

    def query(self, sql: str, nums: Optional[int] = None) -> List[Dict]:
        connection = self.connect()
        with connection as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            if self.db_name in ["mysql", "oracle"]:
                columns = [obj[0] for obj in cursor.description]
            else:
                columns = [obj.name for obj in cursor.description]
            if nums is None:
                rets = cursor.fetchall()
            else:
                rets = cursor.fetchmany(nums)
            rets = [dict(zip(columns, objs)) for objs in rets]
            return rets
