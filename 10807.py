n = int(input())
given = list(map(int,input().split()))    #map() 함수를 사용하여 공백으로 구분된 정수들을 하나의 리스트로 변환합니다.
v = int(input())

count = given.count(v)
print(count)