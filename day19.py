def login(username, password):
    print("Testing:", username, password)

try:
    file = open("users.txt", "r")
    for line in file:
        data = line.strip().split(",")
        username = data[0]
        password = data[1]
        print("Username:", username)
    file.close()
except FileNotFoundError:
    print("Error: File not found bro! Check the file name")
except:
    print("Something went wrong")