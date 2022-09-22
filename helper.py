
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


def SR(ip, masque):
    result = ""

    for i in range(len(ip)):
        if(ip[i] == '.'):
            result += '.'

        elif(masque[i] == '1'):
            result += ip[i]
        else:
            result += '0'

    return result


def broadcast(ip, masque):
    result = ""

    for i in range(len(ip)):
        if(ip[i] == '.'):
            result += '.'

        elif(masque[i] == '1'):
            result += ip[i]
        else:
            result += '1'

    return result


def start(ip, masque):

    print("=" * 20)
    print("IP is", verifIP(ip))
    print("Masque is", verifMasque(masque))
    if(verifIP(ip) and verifMasque(masque)):
        print("=" * 20)

        print("IP binary is    ", toBinary(ip))
        print("Masque binary is", toBinary(masque))
        print("Sous-réseaux :  ", SR(toBinary(ip), toBinary(masque)),
              "=>", toPointer(SR(toBinary(ip), toBinary(masque))))
        print("Broadcast :     ", broadcast(toBinary(ip), toBinary(masque)),
              "=>", toPointer(broadcast(toBinary(ip), toBinary(masque))))


start(input("IP : "), input("Masque : "))
