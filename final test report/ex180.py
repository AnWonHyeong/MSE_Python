low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = [] #volatility를 리스트로 선언
for i in range (len(high_prices)): #for문을 low_prices또는 high_prices의
#길이만큼 반복
    volatility.append (high_prices[i] - low_prices[i])
    #멤버 함수append는 리스트 마지막에 괄호안에 것을 추가해준다. 
    #우리는 for문을 통해 4번 반복하여 append를 통해 생성한 값을 차례대로 volatility에
    #집어 넣는다.
print(volatility)