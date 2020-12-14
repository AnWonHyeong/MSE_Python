class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성") #자식 class가 생성될 때 개채가 생성될 때
        #생성자가 호출되고 "자식생성"을 출력한다.
        super().__init__()
        #부모 class에 접근하고 생성자를 호출하여 "부모생성"을 출력한다.
        #super는 자식 클래스에서 부모클래스의 내용을 사용하고 싶을 경우 사용한다.
        #예를 들어 아빠라는 클래스와 아들, 딸이라는 각각의 클래스가 있다고 하자.
        #이 때 딸은 예쁘다를 가지고 있고 아들은 아무것도 없다고하자.
        #아들과 딸이 각각 아빠에게 잘생김 이라는 메소드를 받는다고 하면
        #아들은 잘생김을 출력하지만 딸은 이미 예쁘다라는 메소드를 사용중이기 때문에
        #잘생김 메소드를 무시하고 예쁘다를 출력하게 된다.
        #추가적으로 딸의 메소드를 변형시켜도 아들이나 아빠에게 영향을 주지는 않는다.
        #출처:https://rednooby.tistory.com/55
        

나 = 자식() 