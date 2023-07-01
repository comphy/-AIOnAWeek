# -*- coding: utf-8 -*-
"""

doctor.py 프로그램
간단히 작성한 ELIZA 프로그램 
사용방법 : c:\>python doctor.py

"""

# 모듈 가져오기 
import re

# 초기 설정
LIMIT = 20      # 최소 횟수
CYCLE = 5       # 반복 횟수

# 메인 실행부 
count = 0
endcount = 0

print("Dr> 나는 Doctor. 이야기를 들어볼까요?")
while True:      # 1 행마다 패턴을 조사해서 응답한다.
    inputline = input("당신>")
    if count >= CYCLE:      # 반복
        print("Dr> ", inputline, "입니까...")
        count = 0
    elif re.search("선생님", inputline):
        print("Dr> 내가 아닌 당신에 관한 이야기를 합시다.")
    elif re.search("어머니", inputline):
        print("Dr> 당신의 어머니에 대해 이야기해주세요.")
    elif re.search("아버지", inputline):
        print("Dr> 당신의 아버지에 대해 이야기해주시요.")
    elif re.search("의견", inputline):
        print("Dr> 내 의견을 듣고 싶은 겁니까?")
    elif re.search("이 걱정입니다", inputline):
        print("Dr> ", inputline.replace("이 걱정입니다", "가 걱정입니까?"))
    else :
        print("Dr> 계속해보세요")
    count += 1
    endcount += 1
    if endcount >= LIMIT:
        break
print("Dr> 그러면 여기서 마칩시다. 수고하셨습니다.")

# doctor.py 끝내기

