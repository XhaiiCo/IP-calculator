
def verifIP(ip):
    # split the ip into a array by the '.'
    splited_ip = ip.split('.')

    # check if the array is len(4)
    if(len(splited_ip) != 4):
        return False

    for i in splited_ip:
        try:
            int(i)
        except:
            print("An exception occurred")
            return False

        if(int(i) < 0 or int(i) > 255):
            return False

    return True


def verifMasque(masque):
    # split the masque into a array by the '.'
    splited_masque = masque.split('.')

    # check if the array is len(4)
    if(len(splited_masque) != 4):
        return False

    last = 255

    for i in splited_masque:
        # check is the current element is a integer
        try:
            int(i)
        except:
            print("An exception occurred")
            return False

        # check is the current element is between 0 and 250
        if(int(i) < 0 or int(i) > 255):
            return False

        # check if the current element is greater than the last element
        if(int(i) > last):
            return False
        last = int(i)

    return True


def toBinary(txt):
    splited = txt.split('.')
    result = ""

    for i in splited:
        binary = bin(int(i))[2:]  # convert in binary

        while len(binary) < 8:
            binary = '0' + binary

        result += binary + "."

    return result[:-1]


def toPointer(binary):
    result = ""
    tmp = ""
    for i in binary + ".":
        if(i != '.'):
            tmp += i

        else:
            result += str(int(tmp, 2)) + "."
            tmp = ""

    return result[:-1]

def formaterNombre(num):
    return f'{num:,}'
