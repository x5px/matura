def repeat_string(s, req_len):
    return (s * req_len)[:req_len]

def szyfruj(plain_text, klucz):
    plain_text = plain_text.replace(" ","")
    klucz = repeat_string(klucz, len(plain_text))
    s_tab = []
    for i in range(0, len(plain_text)):
        pt_ascii = ord(plain_text[i])-64
        k_ascii = ord(klucz[i])-64
        if (pt_ascii+k_ascii)%26 == 0:
            s_tab.append(chr((pt_ascii+k_ascii)%26+64+26)) # loop
        else:    
            s_tab.append(chr((pt_ascii+k_ascii)%26+64))
    print(''.join(s_tab))

plain_text = input("Podaj tekst do zaszyfrowania: ")
klucz = input("Podaj klucz: ")
szyfruj(plain_text, klucz)
