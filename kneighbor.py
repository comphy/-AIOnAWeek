# -*- encoding: utf-8 -*-
"""
kneighbor.py 프로그램
K-인접기법 계산 프로그램
사용방법 : c:\>python kneighbor.py
"""

# 메인 실행부
# 학습 데이터 세트의 정의
itemdata = [ [ 30, 50, "A"], [ 65, 40, "B"],
            [ 90, 100, "A"], [ 90, 60, "B"],
            [ 70, 60, "B"], [ 40, 50, "A"],
            [ 80, 50, "B"]]

#분류 대상 입력
h = float(input("분류 대사을 입력하세요:"))
a = float(input("분류 대상의 상부 표면 면적을 입력하세요:"))

#리스트 정렬
itemdata.sort(key = lambda x : (x[0] - h) ** 2 + (x[1] - a) ** 2)

#결과 출력
print(itemdata)

#kneighbor.py 끝내기
