class OMG : #클래스가 생기고 OMG라는 변수가 받는다.
    def print() : #print()라는 어떤 함수를 정의한다. 여기까지가 클래스를 정의한 것이다.
        print("Oh my god")

myStock = OMG() #객체 생성 이 객체는 생성자가 없고 초기화를 한것이 아니기 때문에 비어있다.
myStock.print() #OMG.print(mystock)으로 불러오게 된다.
#mystock.print를 하면 mystock안에 print가 없으므로 자신의 클래스로 이동한다.
#클래스로 돌아갔을때 함수가 있으므로 호출할 수 있다. 그러나 실제로는 OMG.print(mystock)으로
#호출되게 된다. 인자로 함수로 넘어가게 된다. 즉 부른 개채(mystock)이 OMG.print의 객체로
#들어가게 된다. 따라서 오류가 발생하지 않으려면 
#class OMG : 
#    def print(self) :
#        print("Oh my god") 
#의 형태로 코드를 작성해야 한다. 