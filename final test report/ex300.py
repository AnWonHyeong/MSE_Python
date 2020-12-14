per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0) #예외가 발생하면 출력
    else:
        print("clean data") #예외가 발생하지 않을 때 출력
    finally: 
        print("변환 완료") #예외 발생과 상관없이 출력
        
#"10.31"을 가지고 왔을 때, 10.31.은 실수로 변환할 수 있으므로 try 부분의 실행코드가 실행된다.
#그리고 예외가 발생하지 않았으므로 else부분의 코드가 수행된다. 마지막으로 finally부분의
#코드가 실행된다.
#""은 실수로 변환할 수 없어 예외가 생기고 그로인해 except의 실행코드가 실행되고
#else의 실행코드는 실행되지 않는다. 마지막으로 finally부분이 실행된다.
#"8.00"은 "10.31"과 동일하다.