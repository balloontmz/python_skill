#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import xlrd, xlwt

"""
book = xlrd.open_workbook("for_read.xlsx")
# book.sheets() 全部表格
sheet = book.sheet_by_index(0)

nr = sheet.nrows  # 行数
nc = sheet.ncols  # 列数

cell = sheet.cell(0, 0)
ty = cell.ctype  # 类型
val = cell.value  # 值

ro = sheet.row(1)  # 返回一个列表，元素为对象
ro_val = sheet.row_values(1, 1)  # 返回第一行的从下标1开始的元素列表 

sheet.put_cell()  # 增加一个单元格

# 写文件
wbook = xlwt.Workbook()

wsheet = wbook.add_sheet("sheet1")

wsheet.write(1, 1, "value")
"""

if __name__ == "__main__":
    rbook = xlrd.open_workbook("for_read.xlsx")
    rsheet = rbook.sheet_by_index(0)

    nc = rsheet.ncols  # 列数
    rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, "总分", None)

    for row in range(1, rsheet.nrows):  # 行数
        t = sum([float(x) for x in rsheet.row_values(row, 3, 6)])
        # for x in rsheet.row_values(row, 3, 6):
        #     t += float(x)
        rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)

    wbook = xlwt.Workbook()
    wsheet = wbook.add_sheet(rsheet.name)

    style = xlwt.easyxf("align: vertical center, horizontal center")
    for r in range(rsheet.nrows):
        for c in range(rsheet.ncols):
            wsheet.write(r, c, rsheet.cell_value(r, c), style=style)
    wbook.save("for_write.xlsx")


