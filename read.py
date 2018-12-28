import write

# this program writes some chess data to a csv file
# arbitrary chosen parameters for which games to include:
# exclude all non-rated. Any rating
# include opening and year, win (1-0 white win, ½ or = draw, 0-1 white win)
# formatting (dictionary): {'year': {'opening': {'white wins': num0, 'draws': num1, 'black wins': num2}}}

finalDict = {}
totalNum = 0
totalIgnored = 0

IN_NAME = "Sample Database.txt"

# read and parse
with open(IN_NAME, "r", errors="replace") as inFile:
    # inFile.readline()
    openCode = ""
    for line in inFile:
        # ECO code
        while len(line.rstrip()) <= 3 or line.rstrip()[-1] != ']':
            line = inFile.readline()
        openCode = line.rstrip()[-4:-1]

        # year
        line = inFile.readline()
        year = line.rstrip()[-4:]

        # read through all stuffs, go through some blank spaces and some not blank spaces
        while len(line) > 1:
            line = inFile.readline().rstrip()
        while len(line) < 3:
            line = inFile.readline().rstrip()
        # result (1-0, ½-½, 0-1)
        while len(line) > 1:
            lineOld = line
            line = inFile.readline().rstrip()
        line = lineOld

        result = line.rstrip()[-3:]
        # convert result (-1 black wins, 0 draw, 1 white wins)
        if result == '1-0':
            result = 'white'
        elif result[-1] == "½":
            result = 'draw'
        elif result == '0-1':
            result = 'black'
        else:
            totalIgnored += 1
            print(line)
            continue

        # print(openCode, year, result)
        # if the year is not in the dictionary, add it
        if year not in finalDict:
            finalDict[year] = {}

        # if the opening code is not in the year, add it and the win-draw-loss rate
        if openCode not in finalDict[year]:
            finalDict[year][openCode] = {}
            finalDict[year][openCode]['white'] = 0
            finalDict[year][openCode]['draw'] = 0
            finalDict[year][openCode]['black'] = 0

        finalDict[year][openCode][result] += 1
        totalNum += 1

    print(finalDict)

print("ignored games: ", totalIgnored)
print("included games: ", totalNum)

write.write(finalDict)
