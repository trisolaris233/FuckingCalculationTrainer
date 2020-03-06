# 行车速度80迈，切莫忘记安全带
# 本人计算正确率高达0.5 笑死我了
# 别说万以内乘除法了，万以内加减法50%的概率挂掉
# 自己产生一点随机数练一下

import random


if __name__ == "__main__":

	while True:
		a = random.randint(100,999)
		b = random.randint(100,999)

		method = random.randint(1,100)
		key = 0

		if method % 2:
			print("{}*{}=".format(a,b))
			key = a*b

		else:
			print("{}/{}".format(a,b))
			key = a/b


		input()
		print(round(key,2))
		input()


