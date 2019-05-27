# coding: utf-8

import os
import glob
import re


"""
日志分析器。
"""


class  LogParser:


    def __init__(self, root, unknown=True, verbose=True):
        """

        :param root: 日志根目录
        :param unknown: 是否只解析未匹配成功户型（暂时只支持True)
        :param verbose:
        """
        self.root = root
        self.unknown = unknown # TODO
        self.verbose = verbose

    def __call__(self):
        return self.parser()

    def search(self):
        dirs = []
        files = glob.glob(os.path.join(self.root, '*'))
        for file in files:
            if os.path.isdir(file):
                dirs.append(file)
        return dirs

    def find_suit_dirs(self):
        dirs = self.search()
        pat = re.compile('(.*\d+_\d+)')
        suitable_dirs = list(map(lambda x: pat.findall(x), dirs))
        return self.flat_l(suitable_dirs)

    def parser(self, save=False):
        """

        :param save: 是否保存解析结果 # TODO
        :return:
        """
        dirs = self.find_suit_dirs()
        for dir in dirs:
            per_dir_files = glob.glob(os.path.join(dir, '*.json'))
            if self.verbose:
                print('-'.center(50, '-'))
            tmp_set = set() # 用于去重
            for per in per_dir_files:
                if self.unknown:
                    if '未知' in per:
                        pat = re.compile('.*?(\d+)_(\d+)')
                        pat2 = re.compile('\]-(.[^-_]+?)[_-]')
                        solution_id, dna_Solution_id = pat.findall(dir)[0]
                        name = pat2.findall(per)[0]
                        tmp_set.add((solution_id,
                                     dna_Solution_id,
                                     name))
            for ele in tmp_set:
                solution_id, dna_Solution_id, name = ele
                if self.verbose:
                    print('匹配失败户型: ', solution_id,
                          '被匹配DNA:', dna_Solution_id,
                          '户型名称: ', name)

    @staticmethod
    def flat(L):
        for ele in L:
            if isinstance(ele, list):
                yield from LogParser.flat(ele)
            else:
                yield ele

    @staticmethod
    def flat_l(L):
        return list(LogParser.flat(L))


if __name__ == "__main__":
    root = 'log'
    parser = LogParser(root)
    parser()
