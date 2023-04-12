
# def square(num):
#     return num **2

# result=square(2)
# print(result)

def square(num):
    return num **2

numbers=[1,3,5,7]

result = list(map(square,numbers))

for item in map(square,numbers):
    print(item)

print(result)