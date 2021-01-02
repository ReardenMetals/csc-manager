import json


# saving for backup
def openForSavingInTemp(filename, filename_temp):
    with open(filename, 'r') as file:
        data = file.read()
    with open(filename_temp, 'w') as filetemp:
        filetemp.write(data)
    filetemp.close()
    file.close()
    print "Make copy {}. Done!".format(filetemp.name)


def getCoinPositionByIdInFile(filename, good_coin_id):
    with open(filename, 'r') as file:
        coin_list_id = file.read().splitlines()
        coin_id = coin_list_id.index(good_coin_id)
        file.close()
    return coin_id


def removeLinesInFile(filename, good_coin_pos):
    with open(filename, 'r+') as file:
        coin_list = file.read().splitlines()
        for i in range(good_coin_pos + 1):
            if (coin_list[0] != 'WIF,Address,Seed'):
                coin_list.pop(0)
            else:
                coin_list.pop(1)
    file.close()
    with open(filename, 'w') as file:
        for item in coin_list:
            line = "{}\n".format(item)
            file.write(line)
    file.close()


def main():
    with open('config.json') as json_file:
        config_json = json.load(json_file)
        base_file_name = config_json['base_file_name']
        asset_id_file_name = config_json['asset_id_file_name']
        private_file_name = config_json['private_file_name']
        public_file_name = config_json['public_file_name']
        serial_file_name = config_json['serial_file_name']
        sequence_file_name = config_json['sequence_file_name']
        rebase_file_name = config_json['rebase_file_name']
        reasset_id_file_name = config_json['reasset_id_file_name']
        reprivate_file_name = config_json['reprivate_file_name']
        republic_file_name = config_json['republic_file_name']
        reserial_file_name = config_json['reserial_file_name']
        resequence_file_name = config_json['resequence_file_name']

    good_coin_pos = raw_input("Enter the last good coin id : ")
    good_coin = getCoinPositionByIdInFile(sequence_file_name, good_coin_pos)
    print  good_coin

    openForSavingInTemp(base_file_name, rebase_file_name)
    openForSavingInTemp(asset_id_file_name, reasset_id_file_name)
    openForSavingInTemp(private_file_name, reprivate_file_name)
    openForSavingInTemp(public_file_name, republic_file_name)
    openForSavingInTemp(sequence_file_name, resequence_file_name)

    removeLinesInFile(base_file_name, good_coin)
    removeLinesInFile(asset_id_file_name,good_coin)
    removeLinesInFile(private_file_name,good_coin)
    removeLinesInFile(public_file_name,good_coin)
    removeLinesInFile(sequence_file_name,good_coin)


if __name__ == "__main__":
    main()
