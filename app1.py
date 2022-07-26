import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif w.title() in data: #if user entered "texas" this ill check for "Texas" as well
        return data[w.title()]

    elif w.upper() in data: #in case use enters wodrs like USA or NATO
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:
        yes_no =  input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yes_no == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yes_no == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

i = 1

if type(output) == list:
    for item in output:
        print("{}".format(i) + ") " + item)
        i = i + 1
else:
    print(output)