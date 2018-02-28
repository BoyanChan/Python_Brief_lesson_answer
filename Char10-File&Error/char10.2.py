
filename = 'guest.txt'
with open(filename, 'a') as file_obj:
    file_obj.write("Guest Name: \n")
    while True:
        string = input("Write a name,'q'to leave ")
        if string == 'q':
            break
        print("Hi!"+string+".")
        file_obj.write(string+"\n")
