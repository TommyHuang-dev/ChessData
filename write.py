import csv


def write(data_dict):
    # generate the list of opening names
    print("Getting opening names...")
    opening_names = []
    for year in data_dict:
        for opening in data_dict[year]:
            if opening not in opening_names:
                opening_names.append(opening)
    opening_names.sort()
    print("Finished getting opening names!")

    print("Writing to files...")

    with open("outputData/white.csv", 'w', newline='') as whiteFile, \
            open("outputData/black.csv", 'w', newline='') as blackFile, \
            open("outputData/draw.csv", 'w', newline='') as drawFile, \
            open("outputData/popularity.csv", 'w', newline='') as popularityFile, \
            open("outputData/number of games.csv", 'w', newline='') as numFile:

        fieldnames = ['Year'] + opening_names

        whiteWriter = csv.DictWriter(whiteFile, fieldnames=fieldnames)
        blackWriter = csv.DictWriter(blackFile, fieldnames=fieldnames)
        drawWriter = csv.DictWriter(drawFile, fieldnames=fieldnames)
        popularityWriter = csv.DictWriter(popularityFile, fieldnames=fieldnames)
        numWriter = csv.DictWriter(numFile, fieldnames=["Year", "Number of Games"])

        whiteWriter.writeheader()
        blackWriter.writeheader()
        drawWriter.writeheader()
        popularityWriter.writeheader()
        numWriter.writeheader()

        whiteRow = {}
        blackRow = {}
        drawRow = {}
        popularityRow = {}
        numRow = {}

        for year in sorted(data_dict.keys()):
            whiteRow["Year"] = year
            blackRow["Year"] = year
            drawRow["Year"] = year
            popularityRow["Year"] = year
            numRow["Year"] = year
            total_games_in_year = sum([sum(data_dict[year][i].values()) for i in data_dict[year]])

            numRow["Number of Games"] = total_games_in_year

            for opening in opening_names:
                if opening not in data_dict[year]:
                    whiteRow[opening] = 0
                    blackRow[opening] = 0
                    drawRow[opening] = 0
                    popularityRow[opening] = 0
                else:
                    total_games_of_opening_in_year = sum(data_dict[year][opening].values())
                    whiteRow[opening] = data_dict[year][opening]["white"] / total_games_of_opening_in_year
                    blackRow[opening] = data_dict[year][opening]["black"] / total_games_of_opening_in_year
                    drawRow[opening] = data_dict[year][opening]["draw"] / total_games_of_opening_in_year
                    total_games_of_opening_in_year = sum(data_dict[year][opening].values())
                    popularityRow[opening] = total_games_of_opening_in_year / total_games_in_year

            whiteWriter.writerow(whiteRow)
            blackWriter.writerow(blackRow)
            drawWriter.writerow(drawRow)
            popularityWriter.writerow(popularityRow)
            numWriter.writerow(numRow)
    print("Done writing to files!")
# write({'1834': {'C24': {'white': 1, 'draw': 0, 'black': 0}, 'C42': {'white': 1, 'draw': 0, 'black': 0}, 'B21': {'white': 1, 'draw': 0, 'black': 1}, 'D20': {'white': 4, 'draw': 1, 'black': 3}, 'C37': {'white': 1, 'draw': 0, 'black': 0}, 'C53': {'white': 0, 'draw': 1, 'black': 0}, 'D32': {'white': 1, 'draw': 0, 'black': 0}, 'C25': {'white': 0, 'draw': 0, 'black': 1}, 'C38': {'white': 1, 'draw': 0, 'black': 1}, 'C33': {'white': 0, 'draw': 0, 'black': 1}, 'C23': {'white': 0, 'draw': 1, 'black': 1}, 'C51': {'white': 0, 'draw': 0, 'black': 1}}})
# write({'1834': {'C24': {'white': 1, 'draw': 0, 'black': 0}, 'B21': {'white': 0, 'draw': 0, 'black': 1}, 'D32': {'white': 1, 'draw': 0, 'black': 0}, 'D20': {'white': 2, 'draw': 0, 'black': 3}, 'C25': {'white': 0, 'draw': 0, 'black': 1}, 'C38': {'white': 1, 'draw': 0, 'black': 1}, 'C33': {'white': 0, 'draw': 0, 'black': 1}, 'C51': {'white': 0, 'draw': 0, 'black': 1}}, '1835': {'C42': {'white': 1, 'draw': 0, 'black': 0}}, '1837': {'D20': {'white': 1, 'draw': 0, 'black': 0}}, '1832': {'B21': {'white': 1, 'draw': 0, 'black': 0}}, '1831': {'C37': {'white': 1, 'draw': 0, 'black': 0}}, '1840': {'C53': {'white': 0, 'draw': 1, 'black': 0}}, '1852': {'D20': {'white': 1, 'draw': 1, 'black': 0}, 'C23': {'white': 0, 'draw': 1, 'black': 1}}})