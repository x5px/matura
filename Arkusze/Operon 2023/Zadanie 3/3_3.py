import math

def repeat_string(s, req_len):
    return (s * req_len)[:req_len]

def unrepeat(s, req_len):
    print(s[:req_len // len(s)] + s[:req_len % len(s)]) # ale mi copilot zaimponował w tym momencie
    # na rozszerzeniu copilot labs wziąłem custom brush -> reverse function

def find_first_len(s):
    for i in range(1, math.ceil(len(s) / 2) + 1):
        if repeat_string(s[:i], len(s)) == s:
            return i
    return -1

def znajdz_kod(enc_text, dec_text):
    enc_text = enc_text.replace(" ","").strip()
    dec_text = dec_text.replace(" ","").strip()
    # print(enc_text, dec_text)
    enctab = []
    dectab = []
    keytab = []
    for i in range(0, len(enc_text)):
        enctab.append(ord(enc_text[i])-64)
        dectab.append(ord(dec_text[i])-64)
        keytab.append((ord(enc_text[i])-64)-(ord(dec_text[i])-64))
    # print(enctab)
    # print(dectab)
    keytab = [chr(x%26+64) if x%26 != 0 else chr(x%26+64+26) for x in keytab]
    return ''.join(keytab)


with open("../dane/odszyfruj.txt", 'r+') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()

    for i in range(0, len(lines), 2):
        dec_text = lines[i]
        enc_text = lines[i+1]
        plain_code = znajdz_kod(enc_text, dec_text)
        unrepeat(plain_code, find_first_len(plain_code))