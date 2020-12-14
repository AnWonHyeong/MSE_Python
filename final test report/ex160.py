a = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in a:
    b = i.split('.') #변수를'.'을 기준으로 나눈다. 이떄 '.'은 나타나지 않는다.
    #split멤버 함수는 문자열을 괄호안에 있는 것을 기준으로 분리한다.
    if (b[1] == 'h') or (b[1] == 'c'): #분리한 문자열 중에서 1번째에 해당하는것이
    #h나 c면 변수를 출력한다.
        print(i)