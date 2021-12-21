import json

with open("tests.json") as fo:
    data1 = json.load(fo)

with open("values.json") as fo:
    data2 = json.load(fo)

for dest in data1['tests']:

    if 'values' in dest:
        for dest_1 in dest['values']:
            if 'values' in dest_1:
                for dest_2 in dest_1['values']:
                    if 'values' in dest_2:
                        for dest_3 in dest_2['values']:

                            for source in data2['values']:
                                if source['id'] == dest_3['id']:
                                    dest_3['value'] = source['value']

                    for source in data2['values']:
                        if source['id'] == dest_2['id']:
                            dest_2['value'] = source['value']

            for source in data2['values']:
                if source['id'] == dest_1['id']:
                    dest_1['value'] = source['value']

    for source in data2['values']:
        if source['id'] == dest['id']:
            dest['value'] = source['value']

with open("report.json", "w") as write_file:
    json.dump(data1, write_file, indent=2)
