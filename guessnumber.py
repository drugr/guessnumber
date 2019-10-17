import random
r = random.randint(1, 100)
r = str(r)
while True:
	num = input('請輸入數字: ')#裡面是字串喔~~~~!!!!
	#num = int(num)
	if num == r:
		print('恭喜猜對了~~!')
		break
	else:
		if num > r:
			print('你猜得太大囉~')
		else:
			print('你猜得太小囉~')