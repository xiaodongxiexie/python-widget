# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import pymysql


def rconn(config):
	conn = pymysql.connect(**config)
	return conn


def insert2mysql(table_name, keys, mapping):
    """
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