import requests #requests는 HTTP 요청을 보내는 모듈이다.
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#requests.get()은 GET요청을 만든다. json모듈은 문자열로 바꿔서 전달해준다.
변동폭 = float(btc['max_price']) - float(btc['min_price'])
#float는 실수로 변환해준다.
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > (최고가):
    print("상승장")#시가와 변동폭의 합이 최고가보다 크면 출력한다.
else:
    print("하락장")#시가와 변동폭의 합이 최고가보다 낮으면 출력한다. 