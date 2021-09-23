import re

def to_camelcase(string):
    split_string = string.replace(" ", "_").split("_")
    split_string = [re.sub(r'\W+', '', s) for s in split_string]
    return "".join(s.capitalize() for s in split_string)
