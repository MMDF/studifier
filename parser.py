import random
data = dict()


def getcorrectanswer(key):
    return data[key]


def checkiftrue(key, answer):
    if data[key] == answer:
        return True
    else:
        return False


def getrandomkey():
    keys = list(data.keys())
    return keys[random.randint(0, len(keys) - 1)]


def parse(str):
    data_file = open(str, "r")
    data_str = data_file.read().decode("utf-8")
    try:
        for line in data_str.split("\n"):
            parts = line.split("|")
            data[parts[0]] = parts[1]
    except:
        pass
    return True
