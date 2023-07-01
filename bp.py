# -*- coding: utf-8 -*-
"""
bp.py 프로그램
오차역전파법에 의한 계층형 신경망의 학습
오차의 추이나 학습 결과가 되는 결합개수 등을 입력합니다.
사용방법 : c:\>python bp.py
"""

# 모듈 가져오기 
import math
import sys
import random

# 글로벌 변수
INPUTNO = 5         # 입력층의 뉴런 수 
HIDDENNO = 3        # 은닉층의 뉴런 수
OUTPUTNO = 5        # 출력층의 뉴런 수
ALPHA = 10          # 학습 계수
SEED = 65535        # 난수 시드
MAXINPUTNO = 100    # 데이터의 최대 수
BIGNUM = 100.0      # 오차의 초깃값
LIMIT = 0.001       # 오차의 상한 값

# 형식 인수의 정의
# forward() 함수
def forward(wh, wo, hi, e):
    ''' 순방향 계산 '''
    # hi의 계산
    for i in range(HIDDENNO):
        u = 0.0
        for j in range(INPUTNO):
            u += e[j] * wh[i][j]
        u -= wh[i][INPUTNO]     # 임계값 처리
        hi[i] = f(u)
    # 출력 o의 계산
    o = 0.0
    for i in range(HIDDENNO):
        o += hi[i] * wo[i]
    o -= wo[HIDDENNO]           # 임계값 처리
    return f(o)
# forward() 함수 끝내기

# f() 함수
def f(u):
    ''' 전이 함수 '''
    # 시그모이드 함수의 계산 
    return 1.0 / (1.0 + math.exp(-u))
# f() 함수 끝내기

# olearn() 함수
def olearn(wo, hi, e, o, k):
    ''' 출력층의 가중치 학습 '''
    # 오차 계산
    d = (e[INPUTNO + k] - o) * o * (1 - o)
    # 가중치 학습
    for i in range(HIDDENNO):
        wo[i] += ALPHA * hi[i] * d
    # 임계값 학습
    wo[HIDDENNO] += ALPHA * (-1.0) * d
    return
# olearn() 함수 끝내기

# hlearn() 함수
def hlearn(wh, wo, hi, e, o, k):
    ''' 은닉층의 가중치 학습 '''
    # 은닉층의 각 셀 j를 대상
    for j in range(HIDDENNO):
        dj = hi[j] * ( 1 - hi[j]) * wo[j] * (e[INPUTNO + k] - o ) * o * (1 - o)
        # i번째의 가중치를 처리
        for i in range(INPUTNO):
            wh[j][i] += ALPHA * e[i] * dj
        # 임계값 학습
        wh[j][INPUTNO] += ALPHA * ( -1.0) * dj
    return
# hlearn() 함수 끝내기


# 메인 실행부
# 난수의 초기화
random.seed(SEED)

# 번수의 준비
wh = [[random.uniform(-1, 1) for i in range(INPUTNO + 1)]
    for j in range(HIDDENNO)]       # 은닉층의 가중치
wo = [[random.uniform(-1,1) for i in range(HIDDENNO + 1)]
    for j in range(OUTPUTNO)]    # 출력층의 가중치
hi = [0.0 for i in range(HIDDENNO + 1)] # 은닉층의 출력
o = [0.0 for i in range(OUTPUTNO)]
err = BIGNUM
    
# 학습 데이터 세트
e = [[ 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [ 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
     [ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
     [ 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
     [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]

n_of_e = len(e)

# 결합하중의 초깃값 출력
print(wh, wo)

# 학습
count = 0
while err > LIMIT:
    # 복수의 출력층에 대응
    for k in range(OUTPUTNO):
        err = 0.0
        for j in range(n_of_e):
            # 순방향 계산
            o[k] = forward(wh, wo[k], hi, e[j])
            # 출력층의 가중치 조정
            olearn(wo[k], hi, e[j], o[k], k)
            # 은닉층의 가중치 조정
            hlearn(wh, wo[k], hi, e[j], o[k], k)
            # 오차의 합산
            teacherno = INPUTNO + k
            err += (o[k] - e[j][teacherno]) * ( o[k] - e[j][teacherno])
        count += 1
        # 오차의 출력
        print(count, " ", err)
# 결합 하중의 출력
print(wh, wo)

# 학습 데이터에 대한 출력
for i in range(n_of_e):
    print(i)
    print(e[i])
    outputlist = []
    for j in range(OUTPUTNO):
        outputlist.append(forward(wh, wo[j], hi, e[i]))
    print(['{:.3f}'.format(num) for num in outputlist])
# bp.py 끝내기
