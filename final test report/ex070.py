data = [2,4,3,1,5,10,9]
data.sort(reverse = False)
#멤버 함수 sort는 리스트 내의 요소를 정렬 해준다. 기본값은 reverse = False 이다.
print(data)

data2 = sorted(data)
#sorted함수는 원래의 리스트를 복사하지 않고도 정렬할 수 있다.
print(data2)