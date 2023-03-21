# -*- coding: utf-8 -*-
"""
qlearning.py 프로그램
강화학습(Q학습)의 예제 프로그램
사용 방법 : c:\>python qlearning.py
"""

# 모듈 가져오기 
import random

# 글로벌 변수
GENMAX = 100            # 학습 반복 변수
NODENO = 7              # Q값의 노드 수 
ALPHA = 0.1             # 학습계수
GAMMA = 0.9             # 할인율
EPSILON = 0.3           # 행동 선택의 불규칙성을 결정
REWARD  = 1000.0        # 보상
SEED = 32767            # 난수 시드

# 형식 인수의 정의 
# selecta() 함수
def selecta(olds, qvalue):
    """ 행동을 선택한다 """
    # e-greedy법에 의한 행동 선택
    if random.random() < EPSILON:
        # 불규칙하게 행동
        if(random.randint(0,1) == 0):
            s = 2 * olds + 1
        else:
            s = 2 * olds + 2
    else:
        # Q값 최댓값을 선택
        if (qvalue[2 * olds + 1]) > (qvalue[2 * olds + 2]):
            s = 2 * olds + 1
        else:
            s = 2 * olds + 2
    return s
# selecta() 함수 끝내기

# updateq() 함수
def updateq(s, qvalue):
    """ Q값을 갱신한다 """
    if (s >= 3):        # 마지막 단의 경우
        if s == 6:
            # 보상 부여
            qv = qvalue[s] + int(ALPHA * (REWARD - qvalue[s]))
        else:
            # 보상 없음
            qv = qvalue[s]
    else:   # 마지막 단 외
        if (qvalue[2 * s + 1]) > (qvalue[2 * s + 2]):
            qmax = qvalue[2 * s + 1]
        else:
            qmax = qvalue[2 * s + 2]
        qv = qvalue[s] + ALPHA * (GAMMA * qmax - qvalue[s])
    return qv
# updateq() 함수 끝내기

# 메인 실행부 
qvalue = [0.0 for i in range(NODENO)]       #  Q값을 저장한 리스트

# 난수 초기화
random.seed(SEED)

# Q값의 초기화 
for i in range(NODENO):
    qvalue[i] = random.uniform(0, 100)      # 0에서 100 사이의 난수로 초기화
print(qvalue)

# 학습의 본체
for i in range(GENMAX):
    s = 0       # 행동의 초기 상태
    # 마지막 단계까지 반복
    for t in range(2):
        # 행동 선택
        s = selecta(s, qvalue)
        # Q값의 계산
        qvalue[s] = updateq(s, qvalue)
    # Q값의 출력
    print(qvalue)
# qlearning.py 끝내기

    