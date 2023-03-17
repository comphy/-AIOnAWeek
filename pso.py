# -*- coding: utf-8 -*- 
"""
pso.py 프로그램
입자군집 최적화에 의한 함수의 극값 탐색 프로그램
결과를 그래프로 그린다
사용방법: c:\>python pso.py
"""

# 모듈 가져오기 
import random
import numpy as np
import matplotlib.pyplot as plt

# 상수
N = 30          # 입자 개수
TIMELIMIT = 50  # 시뮬레이션 중단 시간
w = 0.3         # 관성상수
C1 = 1.2        # 로컬 질량
C2 = 1.2        # 글로벌 질량
SEED = 65535    # 난수 시드

# 클래스의 정의 
# Particle 클래스
class Particle:
    """ 입자를 표현하는 클래스의 정의 """
    def __init__(self):     # 생성자
        self.x = random.uniform(-2.0, 2.0)      # x좌표의 초깃값
        self.y = random.uniform(-2.0, 2.0)      # y좌표의 초깃값
        self.value = calcval(self.x, self.y)    # 평갓값
        self.bestval = self.value               # 최적값
        self.vx = random.uniform(-1.0, 1.0)     # 속도 x성분의 초깃값
        self.vy = random.uniform(-1.0, 1.0)     # 속도 y성분의 초깃값
        self.bestpos_x = self.x                 # 최적 위치 (x좌표)
        self.bestpos_y = self.y                 # 최적 위치 (y좌표)

    def optimize(self):     # 다음 시간의 상태 계산
        r1 = random.random()    # 난수 r1의 설정
        r2 = random.random()    # 난수 r2의 설정
        # 속도의 갱신
        self.vx = w * self.vx \
                + C1 * r1 * (self.bestpos_x - self.x) \
                + C2 * r2 * (gbestpos_x - self.x)
        self.vy = w * self.vy \
                + C1 * r1 * (self.bestpos_y - self.y) \
                + C2 * r2 * (gbestpos_y - self.y) 
        
        # 위치의 갱신
        self.x += self.vx
        self.y += self.vy

        # 최적값의 갱신
        self.value = calcval(self.x, self.y)
        if self.value < self.bestval:
            self.bestval = self.value
            self.bestpos_x = self.x
            self.bestpos_y = self.y
# Particle 클래스의 정의 끝내기


# 형식 인수의 정의
# calcval() 함수
def calcval(x, y):
    """ 평갓값 계산 """
    return x * x + y * y
# calcval() 함수의 끝내기

# setgbeat() 함수
def setgbest():
    """ 군중의 최적 위치와 최적값 설정 """
    global gbestval
    global gbestpos_x
    global gbestpos_y
    for i in range(N):
        if ps[i].value < gbestval:
            gbestval = ps[i].bestval
            gbestpos_x = ps[i].bestpos_x
            gbestpos_y = ps[i].bestpos_y
# setgbest() 함수 끝내기

# 메인 실행부
# 초기화
random.seed(SEED)   # 난수의 초기화
# 입자군집 생성
ps = [Particle() for i in range(N)]

# 군중의 최적 위치와 최적값 생성
gbestpos_x = ps[0].bestpos_x 
gbestpos_y = ps[0].bestpos_y
gbestval = ps[0].bestval
setgbest()


# 그래프 데이터의 초기화
xlist = []
ylist = []


# 탐색
for t in range(TIMELIMIT):
    print("t = ", t)
    for i in range(N):
        ps[i].optimize()        # 다음 시간의 상태를 계산
        setgbest()
        # 그래프 데이터 추가 
        xlist.append(ps[i].x)
        ylist.append(ps[i].y)
    # 그래프의 표시
    plt.clf()   # 그래프 영역의 클리어 
    plt.axis([-2, 2, -2, 2])    # 그림 영역의 설정
    plt.plot(xlist, ylist, "o") #"●") # 플롯
    plt.pause(0.01)
    # 그림 데이터의 클리어 
    xlist.clear()
    ylist.clear()
plt.show()
# pso.py 끝내기

