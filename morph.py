# -*- coding: utf-8 -*-
"""
morph.py 프로그램
정규표현을 이용한 간단한 형태소 분리 프로그램
사용방법 : c:\>python morph.py
"""

# 모듈 가져오기
import re

# 형식 인수의 정의
# whatch() 함수
def whatch(ch):
    """ 글자 종류의 판정 """
    if re.match('[가-횧]+', ch):
        chartype = 0
    elif re.match('[A-Za_z]+',ch):
        chartype = 1
    elif re.match('[0-9]+', ch):
        chartype = 2
    else:
        chartype = 3
    return chartype
# whatch() 함수 끝내기

# 메인 실행부
# 분석 대상 문자열의 설정
inputtext = "TOTAL합계120000원입니다."
# 띄어쓰기 문장의 생성
outputtext = ""
for i in range(len(inputtext) - 1):
    print(inputtext[i], end = "")
    if whatch(inputtext[i]) != whatch(inputtext[i + 1]):
        print(" ", end = "")
print(inputtext[-1:])
# morph.py 끝내기




