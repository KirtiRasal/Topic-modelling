import json
from pathlib import Path
import os

data_file_name_with_path = 'data/data_files.json'

def main():

    with open(file=data_file_name_with_path, mode='r') as file:
        data = json.load(fp=file)

    for d in data:
        d['Effective_date'] = str(d['Effective_date']).split('-')[0]

    data = sorted(data, key=lambda di: di['Effective_date'])

    p = Path('data/sample')

    print(os.getcwd())

    for idx, d_ in enumerate(data):
        folder = str(d_['Effective_date'])
        year_folder = p / folder
        print(year_folder)
        year_folder.mkdir(exist_ok=True)
        with open(file=(year_folder / f'{idx}.txt'), mode='w', encoding="utf-8") as file:
            file.write(d_['clean_Document_Content'])


if __name__ == "__main__":
    main()


