fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
a = input("좋아하는 과일은?") #input은 입력한 것을 변수로 선언해준다.
if a in fruit.values(): #a가 fruit이라는 딕셔너리 안에 value값 중 하나면
#"정답입니다"가 출력된다.
    print("정답입니다.")
else:
    print("오답입니다.")#value값 중 없다면 "오답입니다."가 출력된다.