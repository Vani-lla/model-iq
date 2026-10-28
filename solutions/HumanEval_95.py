import re

def check_dict_case(d):
    if not d:
        return False

    keys = list(d.keys())
    lower_case = all(key.islower() for key in keys)
    upper_case = all(key.isupper() for key in keys)

    return lower_case or upper_case
