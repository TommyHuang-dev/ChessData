import write, time, string

# this program writes some chess data to a csv file
# arbitrary chosen parameters for which games to include:
# exclude all non-rated. Any rating
# include opening and year, win (1-0 white win, ½ or = draw, 0-1 white win)
# formatting (dictionary): {'year': {'opening': {'white wins': num0, 'draws': num1, 'black wins': num2}}}

PRINT_ERRORS = False
PRINT_PROGRESS = True
YEAR_CUTOFF = 1900
MOVES_CUTOFF = 4  # any game with less than this will not be included

start_time = time.time()

def parse_game(game):
    global totalNum, totalIgnored, PRINT_ERRORS, classicalOpen, modernOpen
    data = []  # list of year, opening, result, school of chess
    game = game.split("<br/>")
    data.append(game[1][-4:])
    # year cutoff
    if int(data[0]) < YEAR_CUTOFF:
        totalIgnored += 1
        return "failed"
    # num moves cutoff
    for i in range(2, len(game)):
        if str(MOVES_CUTOFF) + "." not in game[i]:
            totalIgnored += 1
            return "failed"

    # some logic for ECO codes
    if game[0][-1] == "]":
        data.append(game[0][-4: -1])
    else:
        totalIgnored += 1
        return "failed"
    data.append("failed")
    for i in range(len(game[-1]) - 1, 0, -1):
        if game[-1][i] == "-":
            data[2] = game[-1][i - 1: i + 2]
            break

    data.append("")
    for i in classicalOpen:
        if i in data[1]:
            data[3] = "classical"
            break
    if not data[3]:
        for i in modernOpen:
            if i in data[1]:
                data[3] = "hypermodern"
                break
    if not data[3]:
        data[3] = "other"

    # ignore some openings
    # for i in ignoreList:
    #     if i in data[1]:
    #         totalIgnored += 1
    #         return "failed"

    if data[2] == "1-0":
        data[2] = "white"
        totalNum += 1
    elif data[2] == "2-1":
        data[2] = "draw"
        totalNum += 1
    elif data[2] == "0-1":
        data[2] = "black"
        totalNum += 1
    else:
        if PRINT_ERRORS:
            print("ignored this game:")
            print(game[-2:])
        totalIgnored += 1
        return "failed"

    return data

# classical openings list
classicalOpen = []
modernOpen = []

with open("classicalOpenings", "r", errors="replace") as classFile:
    for line in classFile:
        line = line.split()
        classicalOpen += line

with open("modernOpenings", "r", errors="replace") as modFile:
    for line in modFile:
        line = line.split()
        modernOpen += line

print(classicalOpen)
print(modernOpen)

# ignore these openings
ignoreList = []

finalDict = {}
totalNum = 0
totalIgnored = 0

# read and parse
def readFile(path):
    global PRINT_PROGRESS
    with open(path, "r", errors="replace") as inFile:
        year = ""
        openCode = ""
        result = ""
        gameString = ""  # string for one game

        for line in inFile:
            if "</p>" in line:
                # separate two different games
                line = line.rstrip().split("</p>")
                gameString += line[0]

                # call parse_game, which returns an list of all the important details
                stats = parse_game(gameString)
                if stats != "failed":  # if it failed, it will skip this step
                    year = stats[0]
                    openCode = stats[1]
                    result = stats[2]
                    style = stats[3]
                    # write to final dictionary
                    # if the year is not in the dictionary, add it
                    if year not in finalDict:
                        finalDict[year] = {"classical": {"black": 0, "draw": 0, "white": 0}, "hypermodern": {"black": 0, "draw": 0, "white": 0}, "other": {"black": 0, "draw": 0, "white": 0}}
                    # if the opening code is not in the year, add it and the win-draw-loss rate

                    finalDict[year][style][result] += 1
                    if PRINT_PROGRESS and totalNum % 100000 == 0:
                        print("Progress:", totalNum)

                # reset gameString, include the rest of the line
                gameString = line[1]
            else:
                gameString += line.rstrip()


print("Reading games...")

# readFile("sampleData/Sample Database 2.htm")
# readFile("sampleData/Sample Database 1.txt")
readFile("Database1.htm")
readFile("Database2.htm")

print("Done reading games!")

print(finalDict)

print("ignored games: ", totalIgnored)
print("included games: ", totalNum)

write.write(finalDict)

print("Total time:", time.time() - start_time, "s")
