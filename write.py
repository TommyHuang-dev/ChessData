import csv
import read

OUT_NAME = "chessParsedData.csv"

with open(OUT_NAME, 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'first', 'last_name': 'last'})
