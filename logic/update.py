import json
import shutil
import os


def update(last_good_coin):
    with open('config.json') as json_file:
        config_json = json.load(json_file)

        config_files = [
            config_json['sequence_file_name'],
            config_json['base_file_name'],
            config_json['asset_id_file_name'],
            config_json['private_file_name'],
            config_json['public_file_name']
        ]
        print("Loaded config files")
        print(config_files)

    good_coin_pos = get_coin_position(config_files[0], last_good_coin)
    print("good_coin_pos: " + str(good_coin_pos))

    for file_name in config_files:
        copy_file(file_name)
        remove_lines_in_file(file_name, good_coin_pos)

    print("Successfully updated!")


# saving for backup
def copy_file(old_file):
    # new_file = old_file + "tmp"
    # shutil.copy(old_file, new_file)
    # print("Make copy {}. Done!".format(new_file))
    pass


def get_coin_position(filename, good_coin):
    print("get_coin_position")
    with open(filename, 'r') as file:
        coin_list_id = file.read().splitlines()
        coin_id = coin_list_id.index(good_coin)
        file.close()
    return coin_id


def remove_lines_in_file(filename, good_coin_pos):
    print("remove_lines_in_file")
    with open(filename, 'r+') as file:
        coin_list = file.read().splitlines()
    file.close()
    for i in range(good_coin_pos + 1):
        if os.path.basename(filename) != "address.csv":
            coin_list.pop(0)
        else:
            coin_list.pop(1)
    with open(filename, 'w') as file:
        for item in coin_list:
            line = "{}\n".format(item)
            file.write(line)
    file.close()