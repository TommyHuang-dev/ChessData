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


    # with open("chessParsedData.csv", 'w', newline='') as csvfile:
    #     fieldnames = ['Year'] + opening_names
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #
    #     writer.writeheader()
    #     writer.writerow({'first_name': 'first', 'last_name': 'last'})
    pass

write({'1834': {'C24': {'white': 1, 'draw': 0, 'black': 0}, 'C42': {'white': 1, 'draw': 0, 'black': 0}, 'B21': {'white': 1, 'draw': 0, 'black': 1}, 'D20': {'white': 4, 'draw': 1, 'black': 3}, 'C37': {'white': 1, 'draw': 0, 'black': 0}, 'C53': {'white': 0, 'draw': 1, 'black': 0}, 'D32': {'white': 1, 'draw': 0, 'black': 0}, 'C25': {'white': 0, 'draw': 0, 'black': 1}, 'C38': {'white': 1, 'draw': 0, 'black': 1}, 'C33': {'white': 0, 'draw': 0, 'black': 1}, 'C23': {'white': 0, 'draw': 1, 'black': 1}, 'C51': {'white': 0, 'draw': 0, 'black': 1}}})
write({'1834': {'C24': {'white': 1, 'draw': 0, 'black': 0}, 'B21': {'white': 0, 'draw': 0, 'black': 1}, 'D32': {'white': 1, 'draw': 0, 'black': 0}, 'D20': {'white': 2, 'draw': 0, 'black': 3}, 'C25': {'white': 0, 'draw': 0, 'black': 1}, 'C38': {'white': 1, 'draw': 0, 'black': 1}, 'C33': {'white': 0, 'draw': 0, 'black': 1}, 'C51': {'white': 0, 'draw': 0, 'black': 1}}, '1835': {'C42': {'white': 1, 'draw': 0, 'black': 0}}, '1837': {'D20': {'white': 1, 'draw': 0, 'black': 0}}, '1832': {'B21': {'white': 1, 'draw': 0, 'black': 0}}, '1831': {'C37': {'white': 1, 'draw': 0, 'black': 0}}, '1840': {'C53': {'white': 0, 'draw': 1, 'black': 0}}, '1852': {'D20': {'white': 1, 'draw': 1, 'black': 0}, 'C23': {'white': 0, 'draw': 1, 'black': 1}}})