# username,password => database
# 'user_001','123456'

# a,b,c,d=5,5,10,4

# result=a==b #True
# result=(a==c)

# print(result)

username='hector_001'
password='123456'

result=('user_001'==username,password=='334455')

print(result)
if result==False:username='user_001'

print(result)
