import csv

# this program writes some chess data to a csv file

# arbitrary chosen parameters for which games to include:
# exclude all non-rated. Any rating
# include opening and year, win (1-0 white win, ½ or = draw, 0-1 white win)
# formatting (dictionary): {'year': {'opening': {'white wins': num0, 'draws': num1, 'black wins': num2}}}

finalDict = {}

# read and parse
with open("Sample Database.txt", "r", errors="replace") as inFile:
    # inFile.readline()
    for line in inFile:
        # ECO code
        openCode = line.rstrip()[-5:]
        # year
        line = inFile.readline()
        year = line.rstrip()[-4:]
        # result (1-0, ½-½, 0-1)
        line = inFile.readline()
        line = inFile.readline()
        result = line.rstrip()[-3:]
        # convert (-1 black wins, 0 draw, 1 white wins)
        if result == '1-0':
            result = '1'
        elif result == '0-1':
            result = '-1'
        elif result == '-Â½':
            result = '0'
        else:
            print("SOMETHING NOT FORMATTED A fdkabewalfabef ")
            print(line)

        print(openCode, year, result)
        line = inFile.readline()
3
# write to chessParsedData.csv
with open('chessParsedData.csv', 'w', newline='') as outFile:
    writer = csv.writer(outFile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['row 1', 'row 2'])
    writer.writerow(['1', '2', '3'])

