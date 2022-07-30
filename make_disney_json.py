import csv
import json

def make_json(disney_titles_csv, disney_titles_json):
    
    data = []
    
    with open(disney_titles_csv, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            data.append(rows)
    
    with open(disney_titles_json, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

disney_titles_csv = r'/Users/arianazaagsma/Desktop/NucampFolder/Python/3-DevOps/Portfolio Project - Latest/disney_titles_csv.csv'
disney_titles_json = r'/Users/arianazaagsma/Desktop/NucampFolder/Python/3-DevOps/Portfolio Project - Latest/disney_titles_json.json'

make_json(disney_titles_csv, disney_titles_json)
