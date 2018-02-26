numbers = [i ** 3 for i in range(1, 11)]  # 从1到10的立方数
for value in range(1, len(numbers) + 1):
    print(numbers[value - 1])  # 将它们打印出来
print("The first three items in the list are:")
print(numbers[0:3])
print("Three items from the middle of the list are:")
print(numbers[4:7])
print("The last three items in the list are;")
print(numbers[-3:])  # 切片器的用途

print("------------------------------")

new_numbers = numbers[:]  # 创建新的列表并复制
numbers.append("old")
new_numbers.append("new")

for value in range(1, len(numbers) + 1):
    print(numbers[value - 1])

for value in range(1, len(numbers) + 1):
    print(new_numbers[value - 1])
