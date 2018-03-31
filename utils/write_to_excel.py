# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
from collections import Iterable
import xlwt
import os

def write_to_excel(col_names=None,
                   filename='test.xls',
                   content=None,
                   is_test=True):
    if is_test:
        if os.path.exists(filename):
            os.remove(filename)
    if not isinstance(col_names, Iterable):
        raise TypeError("col_names must be iterable")

    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('sheet')
    # ------------------------------------
    font = xlwt.Font()
    style = xlwt.XFStyle()
    alignment = xlwt.Alignment()

    font.name = '楷体'
    font.bold = True
    font.underline = False
    font.shadow = True

    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER

    style.font = font
    style.alignment = alignment
    # ------------------------------------

    worksheet.col(0).width = 5000

    for col, name in enumerate(col_names):
        worksheet.write(0, col, name, style)
    if content is not None:
        for col, value in enumerate(content, start=1):
            for col2, value2 in enumerate(value):
                worksheet.write(col, col2, value2, style)
    workbook.save(filename)


if __name__ == "__main__":
    col_names = ['solutionId', 'dnaSolutionId', 'isSuccessful']
    content = []
    for i in range(10):
        content.append([i, i+1, i+2])
    write_to_excel(col_names, content=content)





