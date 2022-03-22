yy1, yy2 = input().split() #두 연도 입력
yy1, yy2 = int(yy1), int(yy2) 
day = input() # 요일 입력
week = ['월','화','수','목','금','토','일'] #요일을 저장한 리스트
n = 0 #요일 계산을 위한 변수
count = 0 #두 연도 사이에 있는 윤년의 수를 넣을 변수

for yy in range(yy1,yy2): #두 연도 사이의 윤년의 수 구하기
	if yy % 400 == 0:
		isLeap = True 
	elif yy % 100 == 0:
		isLeap = False
	elif yy % 4 == 0:
		isLeap =True
	else:
		isLeap = False
	if isLeap: 
		count += 1
	
n += count + yy2 - yy1 # 두 연도 사이의 일수를 통해 요일 계산 (365일은 7일로 나누면 나머지 1일이기에 * 365는 생략)

#첫 번째 연도의 1월1일 요일에 따른 두 번째 연도의 요일 구하는 법
for i in range(7):
	if day == week[i]:
		if i+n%7 < 7:# 만약 리스트의 인덱스가 6을 넘는다면 다시 0번째 인덱스로가 월요일이 된다
			print(week[i+n%7])
		else:
			print(week[i+n%7 - 7])
			
#201903798 허준혁 [컴퓨터.전자 시스템 공학부]
