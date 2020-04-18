import json
import hashlib
import os


# Based on tutorial: https://www.youtube.com/watch?v=JxPWs8Ojdx8

blockchain_dir = os.curdir + '/chains/'


def get_sorted_files():
    files = sorted(os.listdir(blockchain_dir))
    return sorted([int(i) for i in files])


def get_hash(filename):
    file = open(f'{blockchain_dir}{filename}', 'rb').read()
    return hashlib.md5(file).hexdigest()


def check_block_status():
    files = get_sorted_files()

    results = []
    for file in files[1:]:
        actual_hash = json.load(open(blockchain_dir + str(file)))['hash']
        previous_file = str(file - 1)
        expected_hash = get_hash(previous_file)
        res = 'OK' if actual_hash == expected_hash else 'corrupted'
        print(f"Block {previous_file} is {res}")
        results.append({'block': previous_file, 'result': res})
    return results


def write_block(sender, amount, recipient):
    files = get_sorted_files()
    previous_file = files[-1]

    filename = str(previous_file + 1)
    previous_hash = get_hash(str(previous_file))

    data = {
        'sender': sender,
        'amount': amount,
        'recipient': recipient,
        'hash': previous_hash
    }
    with open(f'{blockchain_dir}{filename}', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block(sender='ivan', amount=2, recipient='petr')
    check_block_status()


if __name__ == '__main__':
    main()
