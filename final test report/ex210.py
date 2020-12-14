#def는 함수로 선언
def message1(): #message1을 "A"를 출력하는 것으로 정의
    print("A")

def message2(): #message2을 "B"를 출력하는 것으로 정의
    print("B")

def message3(): #message3을 정의
    for i in range (3) : #3번 반복
        message2() 
        print("C") #message2와 "C"를 출력하는 것을 3번 반복
    message1() #message2와 "c"를 출력하는 for문이 종료된 후 message1을 실행
# 전체 for문 종료

message3() #위으 반복문을 통해 생성된 값을 출력