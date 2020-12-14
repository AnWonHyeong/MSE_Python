ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

total_profit = 0    #총 수익금의 초기값을 0으로 설정
for day_price in ohlc[1:]:  #ohlc의 1번째 행부터 반복
    profit  = day_price[0] - day_price[3]
    #나온 day_price 리스트에서 오픈 값은 0번째 값과 종값인 3번째 값을 slicing하여
    #오픈 값에서 종값을 뺸다.
    total_profit += profit
    #total_profit에 profit값을 추가한다.
    #total_profit += profit은 total_profit = total_profit + profit와
    #같다.
    
print(total_profit)