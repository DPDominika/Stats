import csv
import os


def prepare_resources(directory):
    id_list = []
    for file in os.listdir(directory):
        if os.path.splitext(file)[1] == '.tsv':
            id_list.append(os.path.join(file))
    return id_list


def create_all_options(id_list):
    options = []
    for i in range(1, len(id_list) + 1):
        options.append('RUN_ID' + str(i))
    return options


def extract(file, data_name):
    with open(file) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        data = []
        for row in reader:
            data.append(row[data_name])
        return data


def create_data(options, id_list, data_name):
    data = {}
    for i in range(len(options)):
        data[options[i]] = {'x': extract('stats/single_run_stats/' + id_list[i], 'SAMPLE'), 'y': extract('stats/single_run_stats/' + id_list[i], data_name)}
    return data




