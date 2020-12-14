def 함수0(num) :  #함수0에 대하여 정의
    return num * 2  #num에 2를 곱하고 num에 그 값을 저장

def 함수1(num) : #함수1 정의
    return 함수0(num + 2) #함수0에 num에 2를 더한 값을 리턴

def 함수2(num) : #함수2 정의
    num = num + 10 #num을 num에 10을 더한 값으로 변환
    return 함수1(num) # 함수1에 num 값을 리턴

c = 함수2(2)
#c = 함수2(2)이므로 함수2를 먼저 적용하면
#함수2(num)에서 num은 2이므로 정의된 코드를 따라서
#함수1의 num에 12가 리턴된다.
#그리고 함수1(num)에서 num은 12이고 정의에 따라서
#함수0의 num에 14가 리턴된다.
#그리고 함수0의 정의에 따라서
#num값에 14 *2 =28이 리턴된다.
#그리고 최종적으로 변수c에 28이 저장된다.
print(c)  #따라서 c를 출력하면 28이라는 값이 출력된다.