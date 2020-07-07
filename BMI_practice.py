height = input('請輸入身高(公分): ')
weight = input('請輸入體重(公斤): ')
height = float(height) / 100
weight = float(weight)
bmi = weight / height / height
print('你的BMI值為', bmi)
if bmi < 18.5:
	print('你屬於過輕體型。')
elif bmi >= 18.5 and bmi < 24:
	print('你屬於正常體型。')
elif bmi >= 24 and bmi < 27:
	print('你已經過重了。')
elif bmi >= 27 and bmi < 30:
	print('你已被歸類於輕度肥胖族群。')
elif bmi >= 30 and bmi < 35:
	print('你已被歸類於中度肥胖族群。')
elif bmi >= 35:
	print('你已被歸類於重度肥胖族群！')
else:
	print('請輸入正確的值。')