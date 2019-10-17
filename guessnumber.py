import random
r = random.randint(1, 10)
r = str(r)
while True:
	num = input('請輸入數字: ')#裡面是字串喔~~~~!!!!
	#num = int(num)
	if num == r:
		print('恭喜猜對了~~!')
		break
	else:
		print('猜錯囉~~，在猜一次吧')
		print('是', r,'喔')