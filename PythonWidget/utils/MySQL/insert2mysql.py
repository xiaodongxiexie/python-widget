# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import pymysql


def rconn(config):
    """
    example:
        config = {'host': 'localhost',
                  'port': 3306,
                  'user': 'admin',
                  'passwd': 'admin',
                  'db': 'db',
                  'charset': 'utf8'}
    """
	conn = pymysql.connect(**config)
	return conn


def insert2mysql(table_name, keys, mapping):
    """
    insert mysql by given key list
    :param table_name:
    :param keys:
    :param mapping: dict
    """
    astring = ''
    for index, ele in enumerate(keys):
        if index == 0:
            astring += '{{{}!r}}'.format(ele)
        else:
            astring += ',{{{}!r}}'.format(ele)
    conn = rconn()
    with conn:
        cursor = conn.cursor()
        insert_header = "insert into {} ".format(table_name)
        insert_middle = "({}) values ".format(','.join(keys))

        insert_tail = astring.format_map(mapping)
        insert_tail = '({})'.format(insert_tail)

        sql_str = insert_header + insert_middle + insert_tail

        cursor.execute(sql_str)
        cursor.close()
        conn.commit()


def select_max_value(table_name, key):
    """
    return the max value by the given key in table
    :param table_name: 表名
    :param key: 列名
    :return: integer
    """
    conn = rconn()
    with conn:
        cursor = conn.cursor()
        sql_str = 'select max({}) from {}'.format(key, table_name)
        cursor.execute(sql_str)
        result = cursor.fetchall()[0][0]
    if result is None:
        return 0
    return result


def select_col_name_from_table(table_name):
    """
    return the column names
    :return: list
    """
    conn = rconn()
    with conn:
        try:
            cursor = conn.cursor()
        except:
            conn.connect()
            cursor = conn.cursor()
        sql = 'select * from {} limit 1'.format(table_name)
        cursor.execute(sql)
        des = cursor.description
        col_names = []
        for ele in des:
            col_names.append(ele[0])
        return col_names


def get_distinct(key, table_name):
    """
     return unique value by given key in given table
    :param key: 列名
    :param table_name: 表名
    :return: list
    """
    conn = rconn()
    with conn:
        sql = 'select distinct({}) from {}'.format(key, table_name)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    seq = []
    for ele in result:
        seq.append(ele[0])
    return seq
