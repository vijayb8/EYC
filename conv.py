import os
import json


def parse_content(file, content, printed):
    json_obj = json.loads(content)
    json_array = json_obj['sensordata']
    for event in json_array:
        sensor_stuff = event
        if not printed:
            for key in sensor_stuff.keys():
                file.write(str(key) + ",")
            file.write(";")

        for value in sensor_stuff.values():
            file.write(str(value) + ",")
        file.write(";")


def main():
    printed_once = False
    path = 'E:\hackathon\Data_import\CologneEnvironment'
    # path_csv = 'E:\hackathon\Data_import\csv'
    res = open("res.csv", "w+")
    for file in os.listdir(path):
        if file != "environment-sids.txt":
            new_path = path + "\\" + file
            f = open(new_path, 'r')
            content = f.read()
            print(file, content)
            #parse_content(res, content, printed_once)
            json_obj = json.loads(content)
            json_array = json_obj['sensordata']
            for event in json_array:
                sensor_stuff = event
                if not printed_once:
                    for key in sensor_stuff.keys():
                        res.write(str(key) + ",")
                    #res.seek(-1, os.SEEK_END)
                    #res.truncate()
                    res.write("\n")
                    printed_once = True

                for value in sensor_stuff.values():
                    res.write(str(value) + ",")
                #res.seek(-1, os.SEEK_END)
                #res.truncate()
                res.write("\n")


if __name__ == '__main__':
    main()
