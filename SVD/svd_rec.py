# -*-coding:utf-8-*-
"""
@author:Mark
@file: svd_rec.py 
@time: 2018/05/29
"""
from numpy import *


def loadExData():
    return [[0, 0, 0, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [5, 5, 5, 0, 0],
            [1, 1, 1, 0, 0]]


Data = loadExData()
U, Sigma, VT = linalg.svd(Data)
pass
