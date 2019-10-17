import random
start = input('請決定猜數字最小值: ')
end = input('請決定猜數字最大值: ')
start = int(start)
end = int(end)
while True:
	if end > start:
		r = random.randint(start, end)
		count = 0
		while True:
			end = str(end)
			start = str(start)
			num = input('請輸入' + start +'到' + end + '中間的數字: ')#裡面是字串喔~~~~!!!!
			count += 1
			num = int(num)
			if num == r:
				print('恭喜猜對了~~!')
				print('總共猜了', count, '次喔!!')
				break
			elif num > r:
				print('你猜得太大囉~')
			elif num < r:
				print('你猜得太小囉~')
			print('總共猜了', count, '次喔!!', r)
	else:
		print('最大值要大於最小值喔!!')
		start = input('請決定猜數字最小值: ')
		end = input('請決定猜數字最大值: ')
		start = int(start)
		end = int(end)