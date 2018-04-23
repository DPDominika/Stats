import csv
import os


def prepare_resources():
    directory = 'stats/single_run_stats/'
    id_list = []
    for file in os.listdir(directory):
        if os.path.splitext(file)[1] == '.tsv':
            id_list.append(os.path.join(file))
    return id_list


def create_all_options(id_list):
    all_options = []
    for i in range(1, len(id_list) + 1):
        all_options.append('RUN_ID' + str(i))
    return all_options


def extract(file, data_name):
    with open(file) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        data = []
        for row in reader:
            data.append(row[data_name])
        return data


def create_data(all_options, id_list, data_name):
    vars_data = {}
    for i in range(len(all_options)):
        vars_data[all_options[i]] = {'x': extract('stats/single_run_stats/' + id_list[i], 'SAMPLE'), 'y': extract('stats/single_run_stats/' + id_list[i], data_name)}
    return vars_data




# print(extract('stats/single_run_stats/180317.tsv', 'SAMPLE'))
# id_list = prepare_resources()
# print(id_list)
# all_options = create_all_options(id_list)
# print(create_vars_data(all_options, id_list))