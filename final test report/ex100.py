data = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(data, close_price))
#zip은 각 각의 리스트에서 같은 번호에 있는 것끼리 묶어준다.
#'09/05'는 data에서 0번째이고 10500은 close_price에서 0번이므로 두 원소를 묶는다.
print(close_table)