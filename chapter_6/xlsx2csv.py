#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
本文件简单实现了excel转csv的格式
"""

__author__ = 'tomtiddler'

import csv

import xlrd


rbook = xlrd.open_workbook("for_read.xlsx")
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols  # 列数
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, "总分", None)

for row in range(1, rsheet.nrows):  # 行数
    t = sum([float(x) for x in rsheet.row_values(row, 3, 6)])
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)

with open("pufa_copy.csv", "w") as wf:
    writer = csv.writer(wf)
    resl = []
    for row in range(rsheet.nrows):
        resu = list(rsheet.row_values(row))
        resl.append(resu)
    writer.writerows(resl)

if __name__ == "__main__":
    pass

