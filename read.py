import write

# this program writes some chess data to a csv file
# arbitrary chosen parameters for which games to include:
# exclude all non-rated. Any rating
# include opening and year, win (1-0 white win, ½ or = draw, 0-1 white win)
# formatting (dictionary): {'year': {'opening': {'white wins': num0, 'draws': num1, 'black wins': num2}}}

def parse_game(game):
    global totalNum, totalIgnored
    data = []  # list of year, opening, result
    game = game.split("<br/>")
    data.append(game[1][-4:])
    data.append(game[0][-4: -1])
    data.append("failed")
    for i in range(len(game[-1]) - 1, 0, -1):
        if game[-1][i] == "-":
            data[2] = game[-1][i - 1: i + 2]
            break

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
        print("ignored this game:")
        print(game[-2:])
        totalIgnored += 1
        return "failed"

    print(data)
    return data

finalDict = {}
totalNum = 0
totalIgnored = 0
EOF = False

IN_NAME = "sampleData/Sample Database 1.txt"

# read and parse
with open(IN_NAME, "r", errors="replace") as inFile:
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
                opencode = stats[1]
                result = stats[2]

                # write to final dictionary
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

            # reset gameString, include the rest of the line
            gameString = line[1]
        else:
            gameString += line.rstrip()

    print(finalDict)

print("ignored games: ", totalIgnored)
print("included games: ", totalNum)

write.write(finalDict)
