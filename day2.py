"""
英制单位英寸与公制单位厘米互换
"""
# value = float(input('请输入长度：'))
# unit = input('请输入单位：')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value*2.54))
# elif unit == 'cm' or unit == '厘米' :
#     print('%f厘米 = %f英寸' %(value, value/2.54) )
# else :
#     print('请输入有效单位') 

"""
百分制成绩转换为等级制成绩
"""
# sorce = float(input('请输入成绩：'))
# if sorce >= 90:
#     grade = 'A'
# elif sorce >= 80:
#     grade = 'B'
# elif sorce >= 70:
#     grade = 'C'
# elif sorce >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
# print('对应的等级是：', grade)

"""
输入三条边长，如果能构成三角形就计算周长和面积
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b >  c and a + c > b and b + c > a:
    print('周长：%f' % (a + b + c))
    p = (a + b + c)/2
    area = (p * (p - a)*(p - b)*(p - c) ** 0.5)
    print('面积：%f'%(area))
else:
    print('不能构成三角形')