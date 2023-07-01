# -*- coding: utf-8 -*-
"""
pooling.py 프로그램
폴링 처리
2차원 데이터를 읽어와 폴링을 처리한다
사용방법: c:\>python pooling.py
"""

# 모듈 가져오기 
import math
import sys

# 글로벌 변수 
INPUTSIZE = 8       # 입력 수 


# 형식 인수으 정의  
# pool() 함수 
def pool(im, im_out):
    """ 폴링 계산 """
    for i in range(0, INPUTSIZE, 2):
        for j in range(0, INPUTSIZE, 2):
            im_out[int(i / 2)][int(j / 2)] = maxpooling(im, i, j)
    return 
# pool() 함수 끝내기 


# maxpooling() 함수 
def maxpooling(im, i, j):
    """ 최대값 폴링 """
    # 값 설정
    max = im[i][j]
    # 최대값 검출
    for m in range(2):
        for n in range(2):
            if max < im[i + m][j + n]:
                max = im[i + m][j + n]
    return max
# maxpooling() 함수 끝내기 

# 메인 실행부 
im = [[0, 0, 0, 0, 0, 0, 0, 0],
      [0, 3, 0, 0, 4, 0, 5, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [2, 2, 2, 2, 2, 2, 2, 2],
      [1, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [3, 0, 7, 0, 1, 0, 3, 0],
      [0, 6, 0, 5, 0, 1, 0, 3]
      ]                                     # 입력 데이터
im_out = [[0.0 for i in range(INPUTSIZE)]
          for j in range(INPUTSIZE)]        # 출력 데이터

# 풀링 계산
pool(im, im_out)

# 결과 출력
for i in range(int(INPUTSIZE / 2)):
    for j in range(int(INPUTSIZE / 2)):
        print("{:.3f} ".format(im_out[i][j]), end = "")
    print()

# pooling.py 끝내기


