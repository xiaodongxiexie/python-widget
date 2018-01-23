# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-01-23 19:29:16
# @Last Modified by:   xiaodong
# @Last Modified time: 2018-01-23 20:22:58
import os

import numpy as np
import pandas as pd

from pandas import Series, DataFrame

class LogParser:

    """
    指定格式日志分析。
    """

    def __init__(self, path, i=5):
        self.path = path
        self.circulation = i

    def __extract_data(self):
        with open(self.path, encoding='utf-8') as f:
            data = f.readlines()
        L = []
        for ele in data:
            if ele.strip():
                L.append(ele)
            else:
                yield L
                L = []

    def __data2list(self):
        all_data = list(self.__extract_data())
        tmp = []
        for ele in all_data:
            if ele:
                tmp.append(ele)
        return tmp

    def __frame_list(self):
        frame = []
        seq = self.__data2list()
        for mem in seq:
            tmp = Series(mem).map(lambda x: str(x))
            tmp = tmp.str.extract('(\w+).*([><]{3}).*(\d\d:\d\d:\d\d)', expand=True)
            tmp.columns = ["Desc", "Direct", "Time"]
            frame.append(tmp)
        return frame

    def __e(self):
        i = self.circulation
        frame = self.__frame_list()
        for test in frame:
            data = test.query("Desc=='solutions'")
            shape = data.shape
            if shape[0]//2 == i:
                yield test

    def mean(self, key='layout'):
        i = self.circulation
        tmp = []
        L = list(self.__e())
        for ele in L:
            need = ele.query("Desc=='%s'" %key)
            need = need.sort_values(by='Time')
            i = pd.to_datetime(need.Time.iloc[-1]) - pd.to_datetime(need.Time.iloc[0])
            tmp.append(i)
        return np.mean(tmp)

    def total(self):
        i = self.circulation
        tmp = []
        L = list(self.__e())
        for ele in L:
            total_time = pd.to_datetime(ele.Time).max() -  pd.to_datetime(ele.Time).min()
            tmp.append(total_time)
        return np.mean(tmp)

    def parser(self, loc=-1, single=True, multi=False):
        frame = list(self.__e())

        for i, j in frame[loc].groupby("Desc"):#print(j.sort_values(by='C'), end='\n\n')
            tmp = []
            for x, y in j.groupby("Direct"):
                output = y.sort_values(by="Time")
                tmp.append(output)
                if single:
                    print(output, end='\n\n')
            if multi:
                tmp[1].index = tmp[0].index = range(len(tmp[0]))
                print(tmp[0].join(tmp[1].drop("Desc", axis=1), lsuffix='_input', rsuffix='_output'), end='\n\n')


if __name__ == "__main__":
    root = r"C:\work\work\智能布局\服务器2\AutoLayout\go_on"
    Log = LogParser(os.path.join(root, 'mp_test_log_3.txt'), i=5)
    Log.parser(single=False, multi=True)
    print(Log.mean(key='solutions'), Log.total())

