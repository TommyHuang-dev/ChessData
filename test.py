openFile = open("Database1.htm", "r")

for i in range(50):
    print(openFile.readline().rstrip())
