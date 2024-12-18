abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher = ["hE", "zA", "dC", "fH", "zA", "hE", "zA", "hA", "iJ", "zA", "eI", "aD", "jB", "cB", "hH", "gA", "zA", "fH", "fN"]

def decryption(abc, cipher):
    liste = []
    for sec in cipher:
        ch1 = int(abc.index(sec[0].lower())) + 1
        ch2 = int(abc.index(sec[1].lower())) + 1
        sum = ch1 + ch2
        if sum == 27:
            liste.append('a')
        else:
            liste.append(abc[sum - 1])

    plain_text = ''
    c = 0
    for i in liste:
        c += 1
        if c == 6:
            plain_text += '::'
            plain_text += i
        else:
            plain_text += i

    print('Password Found : ' + plain_text)

decryption(abc, cipher)
