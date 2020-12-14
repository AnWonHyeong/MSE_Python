data = "  삼성전자  "
data1 = data.strip() 
#strip은 좌우 공백을 제거해준다. 추가적으로 lstrip은 왼쪽만, rstrip은 오른쪽만 지워준다.
print(data1)
#정답 외의 방법
print(data[2:6]) #(0부터 세서)2번째 문자부터 5번째 문자까지 출력(6번째 문자 전까지), slicing