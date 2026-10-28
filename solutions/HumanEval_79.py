import math

def decimal_to_binary(decimal):
    if decimal == 0:
        return "db0db"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return "db" + binary + "db"