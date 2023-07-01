# -*- coding: utf-8 -*-
"""
nim.py 프로그램
님 게임을 대상으로 한 게임트리 생성 프로그램
사용 방법 : c:\>python nim.py
"""

# 형식 인수의 정의 
# printlist() 함수
def printlist():
    """ 오픈 리스트와 클로즈드 리스트의 출력 """
    print("openlist: ", openlist)
    print("closedlist: ", closedlist)
# printlist() 함수 끝내기

# expand() 함수
def expand(openlist, closedlist):
    """ 오픈 리스트의 맨 앞 요소를 전개 """
    # 글로벌 변수
    global nodeno
    # 맨 앞 요소를 꺼낸다 
    firstnode = openlist[0].copy()
    # 전개
    parentno = firstnode[0]
    # 각각의 돌더미를 무너뜨린다
    for i in range(len(firstnode[2])):
        # i번째의 돌더미에서 돌을 잡아내고 j개 남긴다
        for j in range(firstnode[2][i]):
            nodeno += 1     # 새로운 노드의 번호
            newnode = [nodeno, parentno]
            newnode.append(firstnode[2].copy())
            newnode[2][i] = j
            openlist.append(newnode.copy())     # 오픈 리스트의 맨 끝에 추가
    # 전개 대상 노드의 클로즈드 리스트에 추가
    closedlist.append(firstnode.copy())
    # 전개 대상 노드의 오픈 리스트에서 삭제
    del openlist[0]
# expand() 함수 끝내기

# 메인 실행부
# 초기화 
nodeno = 0          # 게임트리에 포함된 노드번호
#openlist = [[ 0, 0, [ 2, 1]]]      # 초기 상태가 2개인 돌더미 (2 1)의 경우
openlist = [[ 0, 0, [ 3, 2]]]       # 초기 상태가 2개인 돌더미 (3 2)의 경우
#openlist = [[ 0, 0, [ 3, 2, 1]]]   # 초기 상태가 3개인 돌더미 (3 2 1)의 경우
closedlist = [ ]
printlist()

# 탐색의 본체
while openlist:     # 오픈 리스트가 텅 빌 때가지 반복한다
    # 오픈 리스트의 맨 앞 요소를 전개
    expand(openlist, closedlist)
    printlist()
print("전개 종료")
printlist()
# nim.py 끝내기


