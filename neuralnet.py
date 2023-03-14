# -*- coding: utf-8 -*-
"""
neuralnet.py 프로그램
단순한 계층형 신경망의 계산(학습 없음)
사용방법 : c:\>python neuralnet.py
"""

# 모듈 가져오기 

# 글로벌 변수
INPUTNO = 2     # 입력 수
HIDDENNO = 2    # 은닉층의 셀 수

# 형식 인수의 정의
# forward() 함수
def forward(wh, wo, hi, e):
    """ 순방향의 계산 """
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
    """ 전이 함수 (단계 함수) """
    # 단계함수의 계산
    if u >= 0:
        return 1.0
    else:
        return 0.0
# f() 함수 끝내기


# 메인 실행부
wh = [[ -2, 3, -1], [-2, 1, 0.5]]           # 은닉층의 가중치
wo = [-60, 94, -1]                          # 출력층의 가중치
e = [[ 0, 0], [ 0, 1], [ 1, 0], [ 1, 1]]    # 데이터 세트
hi = [ 0 for i in range(HIDDENNO + 1)]      # 은닉층의 출력

# 계산의 본체
for i in e:
    print(i, "->", forward(wh, wo, hi, i))

# neuralnet.py 끝내기

