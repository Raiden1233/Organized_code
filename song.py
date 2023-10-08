# utf8 encoding for special characters
def rules_():
    with open('rules.txt', 'r', encoding='utf8') as r: # replace 'rules.txt' with any name of your txt file u have
        song = r.readlines()

        return song # returning a list of strings
