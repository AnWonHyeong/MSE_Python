def print_max(a, b, c) :
    max_val = 0     #max_val는 괄호 안의 세 개의 숫자 중 가장 큰 수
    #초기값은 0으로 설정
    if a > max_val :
        max_val = a #a의 값이 max_val보다 크다면 max_val에는 a값이 담긴다.
    if b > max_val :
        max_val = b #b의 값이 a보다 크다면 max_val에는 b의 값이 담긴다.
        #그렇지 않다면 a의 값이 유지된다.
    if c > max_val :
        max_val = c #c의 값이 앞의 코드에서 담긴 b또는 a의 값보다 크다면 c의 값이,
        #그렇지 않다면 앞의 코드에서 담긴 값이 저장된다.
    print(max_val)

#ex1) print_max(50, 100, -20)
#출력값은 100