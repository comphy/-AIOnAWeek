# -*- coding: utf-8 -*-

"""
isa.py 프로그램
is-a 링크에 의한 의미 네트워크를 이용한 추론
사용 방법 : c:\>python isa.py
"""


# 의미 네트워크의 정의
semnet = { 
    "휴대단말기"    : "컴퓨터",
    "노트북"        : "컴퓨터",
    "거치형 PC"     : "컴퓨터",
    "스마트폰"      : "휴대단말기",
    "태블릿"        : "휴대단말기",
    "데스크톱"      : "거치형 PC",
    "서버"          : "거치형 PC",
}

# 메인 실행부
while True:
    # 분류 대상 입력
    print("A는 B입니까? 라는 질문을 다룹니다. A와 B를 입력하세요")
    A = input("A를 입력: ")
    B = input("B를 입력: ")
    print("질문: ", A, "는 ", B, "입니까?")
    print("추론을 시작합니다.")
    # A가 의미 네트워크를 포함하지 않는다면 종료
    if (A in semnet) == False:
        print("'", A, "'", "를 모릅니다.")
        continue
    # is-a 링크를 따라가면서 B를 찾는다
    obj = A
    while obj != B:
        print(" ", obj, "는 ", semnet[obj], "입니다.")
        if semnet[obj] == B:
            print("결론: ", A, "는 ", B, "입니다.")
            break
        if(semnet[obj] in semnet) == False:
            print("결론: ", A, "는 ", B, "가 아닙니다.")
            break
        obj = semnet[obj]
    print("추론 종료.")
# isa.py 끝내기
