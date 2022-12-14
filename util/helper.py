def verifIP(ip):
    # split the ip into a array by the '.'
    splited_ip = ip.split('.')

    # check if the array is len(4)
    if len(splited_ip) != 4:
        return False

    for i in splited_ip:
        try:
            int(i)
        except:
            print("An exception occurred")
            return False

        if int(i) < 0 or int(i) > 255:
            return False

    return True


def verif_ip_reseau(ip):
    if not verifIP(ip):
        return False

    binary_ip = toBinary(ip)

    array_last_bit = list(binary_ip.split('.')[-1])
    if int(array_last_bit[-1]) == 1 or int(array_last_bit[-2]) == 1:
        return False
    return True


def verifMasque(masque):
    # split the masque into a array by the '.'
    splitted_masque = masque.split('.')

    # check if the array is len(4)
    if len(splitted_masque) != 4:
        return False

    last = 255

    for i in splitted_masque:
        # check is the current element is a integer
        try:
            int(i)
        except:
            print("An exception occurred")
            return False

        if int(i) not in [0, 128, 192, 224, 240, 248, 252, 255]:
            return False

        # check if the current element is greater than the last element
        if last != 255 and int(i) != 0:
            return False
        last = int(i)


    # Biggest subnet mask is 255.255.255.252
    if int(splitted_masque[3]) > 252:
        return False

    # Littlest subnet mask is 255.255.255.252
    if int(splitted_masque[0]) != 255:
        return False

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
        if i != '.':
            tmp += i

        else:
            result += str(int(tmp, 2)) + "."
            tmp = ""

    return result[:-1]


def formaterNombre(num):
    return f'{num:,}'


# Donne l'adresse du sous r??seau en binaire
# params: ip en binaire et masque en binaire
def SR(ip, masque):
    result = ""

    for i in range(len(ip)):
        if ip[i] == '.':
            result += '.'

        elif masque[i] == '1':
            result += ip[i]
        else:
            result += '0'

    return result


# Donne l'adresse broadcast du r??seau en binaire
# params: id en binaire, masque en binaire
def broadcast(ip, masque):
    result = ""

    for i in range(len(ip)):
        if ip[i] == '.':
            result += '.'

        elif masque[i] == '1':
            result += ip[i]
        else:
            result += '1'

    return result
