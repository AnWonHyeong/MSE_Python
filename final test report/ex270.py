#268번 코드를 바탕으로 270번 코드를 생성
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
    #self 자리에 객체가 생성될 때 매서드__init__가 호출된 것이 self이므로
    #생성된 객체가 self다. 문제에서 주는 값들을 담기 위해 아래의 코드를 작성한다.
        self.name = name 
        #넘어온 값을 저장하기 위해self라는 공간안에 name이라는 이름으로 변수를 만들고
        #name으로 바인딩을 한다.
        self.code = code
        #넘어온 값을 저장하기 위해self라는 공간안에 code라는 변수를 만들고
        #code로 바인딩을 한다.
        self.per = per
        #넘어온 값을 저장하기 위해self라는 공간안에 per이라는 변수를 만들고
        #per로 바인딩을 한다.
        self.pbr = pbr
        #넘어온 값을 저장하기 위해self라는 공간안에 pbr로 변수를 만들고
        #pbr로 바인딩을 한다.
        self.dividend = dividend
        #넘어온 값을 저장하기 위해self라는 공간안에 dividend로 같은 변수를 만들고
        #dividend로 바인딩을 한다.

        #return을 적지 않아도 none값을 return한다.
    def set_name(self, name):
        self.name = name
        #self.name이 가리키는 공간안에 name이라는 변수가 있지만
        #새로운 값이 오기 때문에 그 값을 바인딩 하기 위해 이와 같이 코드를 짠다.
    def set_code(self, code):
        self.code = code
        #self.code이 가리키는 공간안에 code이라는 변수가 있지만
        #새로운 값이 오기 때문에 그 값을 바인딩 하기 위해 이와 같이 코드를 짠다.
    def get_name(self):
        return self.name
        #가져갈 공간만 리턴해주면 된다.
    def get_code(self):
        return self.code
        #위와 같다.
    def set_per(self, per):
        self.per = per
        #self.name과 같은 이유이다.
    def set_pbr(self, pbr):
        self.pbr = pbr
        #위와 같은 이유다.
    def set_dividend(self, dividend):
        self.dividend = dividend
        #위와 같은 이유이다.


#270번
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성) #append로 생성된 객체를 넣는다.
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)  #.을 찍어 변수에 접근한다.