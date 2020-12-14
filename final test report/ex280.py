import random

class Account:
    #모든 객체가 참조하는 함수는 클래스 안에 위치한다. 이를 class variable이라고 한다.
    account_count = 0
    #계좌가 생성 될 때마다 이 클래스로부터 account_count의 값이 1씩 증가한다.
    def __init__(self, name, balance):
        self.deposit_count = 0
        #계좌가 생성될 때 입금한 회수가 없으므로
        self.deposit_log = []
        #입금이 될 떄마다 입출금 현황을 기록해야 하므로 빈 리스트 생성
        self.withdraw_log = []
        #입금이 될 떄마다 입출금 현황을 기록해야 하므로 빈 리스트 생성

        self.name = name #self 공간에 name이 가리키는 곳에 name으로 변수 생성
        self.balance = balance
        self.bank = "SC은행" #문제의 기본 은행 이름은 SC은행이므로 저장.

        num1 = random.randint(0, 999) #randint는 0과 999를 포함한 랜덤한 수를 뽑아준다.
        num2 = random.randint(0, 99)  #위와 같다. 이 경우 99까지다.
        num3 = random.randint(0, 999999)  #위와 같다. 이 경우 999999까지다.

        num1 = str(num1).zfill(3)  # 문자열로 변경 .zfill은 괄호안의 자릿수로 변경한다.
        #ex) 이 코드로 변경하면 1 -> '1' -> '001'이 된다. 이를 변수로 바인딩.
        num2 = str(num2).zfill(2)  
        num3 = str(num3).zfill(6) 
        self.account_number = num1 + '-' + num2 + '-' + num3 #계좌번호 생성
        Account.account_count += 1
    #객체에 접근 필요가 없는 method를 class method라고 한다.
    def get_account_num(cls): #self대신 cls를 입력. Account클래스에 접근하는 것과 동일
        print(cls.account_count)

    def deposit(self, amount): #잔고는 객체안에 저장되므로 self로 받아야함.
    #instance method형태로 구현
        if amount >= 1: #1원 이상 입금 가능이므로
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count %  5 == 0: #5의 배수이면
                self.balance = (self.balance * 1.01)
                #이자를 지급한다. 이자는 1%

    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)#withdraw_log에 출금한 양을 입력
            self.balance -= amount #출금

    def display_info(self): #계좌 불러올 때 아래의 것들을 출력
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:#deposit_log에 출금한 양에 대한 것을 추가
            print(amount)


k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()
