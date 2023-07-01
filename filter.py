# -*- coding: utf-8 -*-
"""
filter.py 프로그램
공간 필터 적용
2차원 데이터를 읽어내고 공간 필터를 적용한다
사용 방법 : c:\>python filter.py
"""

# 모듈 가져오기 
import math
import sys

# 글로벌 변수 
INPUTSIZE = 11      # 입력 수

# 형식 인수의 정의
# getdata() 함수
def getdata(im):
    """ 이미지 데이터 읽어오기 """
    n_of_e = 0      # 데이터 세트의 행 수
    # 데이터 입력
    for line in sys.stdin:
        im[n_of_e] = [float(num) for num in line.split()]
        n_of_e += 1
    return 
# getdata() 함수 끝내기

# filtering() 함수
def filtering(filter, im, im_out):
    """ 필터 적용 """
    for i in range(1, INPUTSIZE - 1):
        for j in range(1, INPUTSIZE - 1):
            im_out[i][j] = calcfilter(filter, im, i, j)
    return
# filtering() 함수 끝내기 

# calcfilter() 함수
def calcfilter(filter, im, i, j):
    """ 필터 적용 """
    sum = 0.0
    for m in range(3):
        for n in range(3):
            sum += im[i - 1 + m][j - 1 + n] * filter[m][n]
    if sum < 0:     # 결과가 마이너스일 경우는 0으로 한다
        sum = 0
    return sum
# calcfilter() 함수 끝내기 

# 메인 실행부 
np = 1.0 / 9.0

filter = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]     # 라플라시안 필터
# filter = [[ np, np, np], [np, np, np], [np, np, np]]  # 평균필터

im = [[0.0 for i in range(INPUTSIZE)]
    for j in range(INPUTSIZE)]                  # 입력 데이터
im_out = [[0.0 for i in range(INPUTSIZE)]
    for j in range(INPUTSIZE)]                  # 출력 이미지

# 입력 데이터 읽어오기 
getdata(im)

# 필터 적용
filtering(filter, im, im_out)

# 결과 출력
for i in im_out:
    for j in i:
        print("{:3f} ".format(j), end="")
    print()

# filter.py 끝내기


