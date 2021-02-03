import json
import shutil
import os


# saving for backup
def copy_file(old_file):
    new_file = old_file+"tmp"
    shutil.copy(old_file, new_file)
    print "Make copy {}. Done!".format(new_file)


def get_coin_position(filename, good_coin):
    with open(filename, 'r') as file:
        coin_list_id = file.read().splitlines()
        coin_id = coin_list_id.index(good_coin)
        file.close()
    return coin_id


def remove_lines_in_file(filename, good_coin_pos):
    with open(filename, 'r+') as file:
        coin_list = file.read().splitlines()
    file.close()
    for i in range(good_coin_pos + 1):
            if (os.path.basename(filename) != "address.csv"):
                coin_list.pop(0)
            else:
                coin_list.pop(1)
    with open(filename, 'w') as file:
        for item in coin_list:
            line = "{}\n".format(item)
            file.write(line)
    file.close()


def main():

    with open('config.json') as json_file:
        config_json = json.load(json_file)
        good_coin = raw_input("Enter the last good coin id : ")
        good_coin_pos = get_coin_position(config_json.values()[0], good_coin)

        for file_name in config_json.keys():
            copy_file(config_json[file_name])
            remove_lines_in_file(config_json[file_name],good_coin_pos)



if __name__ == "__main__":
    main()
