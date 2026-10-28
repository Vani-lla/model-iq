import re

def file_name_check(file_name):
    # Regular expression to match the file name criteria
    pattern = r'^[a-zA-Z][a-zA-Z0-9]{0,2}[^0-9]*\.(txt|exe|dll)$'
    return 'Yes' if re.match(pattern, file_name) else 'No'
