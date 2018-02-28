print("---Give me teo number---")
print("---I will give the sum--")
print("---Press '0' to exit----\n")

while True:
    try:
        num1 = input("Number 1:")
        num1 = int(num1)
    except ValueError:
        print("Can't enter text")
        continue
    else:
        if num1 == 0:
            break

    try:
        num2 = input("Number 2:")
        num2 = int(num2)
    except ValueError:
        print("Can't enter text")
        continue
    else:
        if num2 == 0:
            break

    sum = num1+num2
    print(str(num1)+"+"+str(num2)+"="+str(sum))

print("------------------------------")

filename = 'b.txt'
try:
    with open(filename) as file:
        contens = file.read()
except FileNotFoundError:
    msg = "Sorry,file not exist"
    print(msg)
    with open('no.txt','a') as f_obj:
        f_obj.write(filename+"\n")
