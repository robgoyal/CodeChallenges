#!/usr/bin/env/python

# DiagonalDifference.py
# Code written by Robin Goyal
# Created on 10-08-2016
# Last updated on 10-08-2016

N = int(raw_input().strip())

matr = []
for matr_index in range(N):
    index_temp = map(int, raw_input().strip().split())
    matr.append(index_temp)

primDiag = 0
seconDiag = 0

for i in range(N):
    primDiag += matr[i][i]
    seconDiag += matr[i][N-1-i]

result = abs(primDiag - seconDiag)
print result
