import csv

# {'year': ('classical': {white, draw, black}, modern...

def write(data_dict):
    # generate the list of style names
    print("Getting style names...")
    play_styles = ["classical", "hypermodern", "other"]

    print("Writing to files...")

    with open("outputData/popularityByStyle.csv", 'w', newline='') as popularityFile, \
            open("outputData/number of games.csv", 'w', newline='') as numFile:
        # top row
        fieldnames = ['Year'] + play_styles

        popularityWriter = csv.DictWriter(popularityFile, fieldnames=fieldnames)
        numWriter = csv.DictWriter(numFile, fieldnames=["Year", "Number of Games"])

        popularityWriter.writeheader()
        numWriter.writeheader()

        popularityRow = {}
        numRow = {}

        for year in sorted(data_dict.keys()):
            popularityRow["Year"] = year
            numRow["Year"] = year

            total_games_in_year = sum([sum(data_dict[year][i].values()) for i in data_dict[year]])
            numRow["Number of Games"] = total_games_in_year

            for style in play_styles:
                if style not in data_dict[year]:
                    popularityRow[style] = 0
                else:
                    total_games_of_style_in_year = sum(data_dict[year][style].values())
                    popularityRow[style] = total_games_of_style_in_year / total_games_in_year
            popularityWriter.writerow(popularityRow)
            numWriter.writerow(numRow)
    print("Done writing to files!")

# write({'1834': {'C24': {'white': 1, 'draw': 0, 'black': 0}, 'C42': {'white': 1, 'draw': 0, 'black': 0}, 'B21': {'white': 1, 'draw': 0, 'black': 1}, 'D20': {'white': 4, 'draw': 1, 'black': 3}, 'C37': {'white': 1, 'draw': 0, 'black': 0}, 'C53': {'white': 0, 'draw': 1, 'black': 0}, 'D32': {'white': 1, 'draw': 0, 'black': 0}, 'C25': {'white': 0, 'draw': 0, 'black': 1}, 'C38': {'white': 1, 'draw': 0, 'black': 1}, 'C33': {'white': 0, 'draw': 0, 'black': 1}, 'C23': {'white': 0, 'draw': 1, 'black': 1}, 'C51': {'white': 0, 'draw': 0, 'black': 1}}})
# write({'1834': {'C24': {'white': 1, 'draw': 0, 'black': 0}, 'B21': {'white': 0, 'draw': 0, 'black': 1}, 'D32': {'white': 1, 'draw': 0, 'black': 0}, 'D20': {'white': 2, 'draw': 0, 'black': 3}, 'C25': {'white': 0, 'draw': 0, 'black': 1}, 'C38': {'white': 1, 'draw': 0, 'black': 1}, 'C33': {'white': 0, 'draw': 0, 'black': 1}, 'C51': {'white': 0, 'draw': 0, 'black': 1}}, '1835': {'C42': {'white': 1, 'draw': 0, 'black': 0}}, '1837': {'D20': {'white': 1, 'draw': 0, 'black': 0}}, '1832': {'B21': {'white': 1, 'draw': 0, 'black': 0}}, '1831': {'C37': {'white': 1, 'draw': 0, 'black': 0}}, '1840': {'C53': {'white': 0, 'draw': 1, 'black': 0}}, '1852': {'D20': {'white': 1, 'draw': 1, 'black': 0}, 'C23': {'white': 0, 'draw': 1, 'black': 1}}})