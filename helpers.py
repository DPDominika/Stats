import csv


def extract(file, data_name):
    with open(file) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        data = []
        for row in reader:
            data.append(row[data_name])
        return data


