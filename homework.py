#encoding :utf-8
#2017-03-20
#
#
#作业一，乘法表
import random


lista = [ '1','2','3','4','5','6','7','8','9' ]


for i in  lista :
	for j in lista :
		if int(i) != int(j) :
 			print ( i , '*' , j , '=', int(i) * int(j) ,' ',end= '')
		else :
 			print ( i , '*' , j ,'=', int(i) * int(j))
 			break


#作业二
#猜数游戏

random_num = random.randint(0,100)

#print (random_num)
end=1
while end <= 5 :

	key = input('请输入一个数字')
	key = int(key)

	if key < random_num :
		print ('猜小了')
	elif key > random_num :
		print ('猜大了')
	else:
		print ('猜对了')
		break
	end += 1
if end > 5 :
	print ('太笨了，下次再来')
else:
	print ('你猜了',end,'次')
exit()















