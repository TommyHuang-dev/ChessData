import csv

# this program writes some chess data to a csv file

# arbitrary chosen parameters for which games to include:
# exclude all non-rated. Any rating
# include opening and year, win (1-0 white win, ½ or = draw, 0-1 white win)
# formatting (dictionary): {'year': {'opening': {'white wins': num0, 'draws': num1, 'black wins': num2}}}

finalDict = {}
IN_NAME = "Sample Database 2.txt"
OUT_NAME = "chessParseData.csv"

# read and parse
with open(IN_NAME, "r", errors="replace") as inFile:
    # inFile.readline()
    for line in inFile:
        # ECO code
        openCode = line.rstrip()[-5:]

        # year
        line = inFile.readline()
        year = line.rstrip()[-4:]

        # read through all stuffs
        while len(line) > 1:
            line = inFile.readline()

        # result (1-0, ½-½, 0-1)
        lineNew = inFile.readline()
        while len(lineNew) > 1:
            lineOld = lineNew
            lineNew = inFile.readline()
        line = lineOld

        result = line.rstrip()[-3:]
        # convert result (-1 black wins, 0 draw, 1 white wins)
        if result == '1-0':
            result = '1'
        elif result == '0-1':
            result = '-1'
        elif result[-1] == "½":
            result = '0'
        else:
            print("dis line: " + line)

        print(openCode, year, result)


