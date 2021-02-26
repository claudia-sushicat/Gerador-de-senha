import random
import string
import time

print('Gerador de senhas')
time.sleep(0.5)
print("\nCarregando quantidade de senhas .")
time.sleep(0.2)
print("\nCarregando quantidade de senhas ..")

def wordlist():
    arquivo = open("rockyou.txt",encoding="utf8")
    leitura = arquivo.read().splitlines()
    print("\nA quantidade de senhas a serem comparadas são: " + str(len(leitura)))
    arquivo.close()
    return leitura

texto = wordlist()

def gerador_senha(length):
    symbols = ["_","@","-","*","="]
    letras = string.ascii_lowercase + string.ascii_uppercase + str(symbols)  + string.digits
    senha_gerada = ''.join(random.choice(letras) for i in range(length))    
    invalid_characters = [" ","/","]","[","","'",".",","]
    str(invalid_characters)
    for i in senha_gerada:
        if i in invalid_characters:
            valid_character = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
            senha_gerada = senha_gerada.replace(i, valid_character)    
    return senha_gerada

nova_senha = gerador_senha(8)

senha = input('Digite uma senha:')
   
if senha in texto or len(senha) < 8 or len(senha) > 16:
    print('Senha vuneravel : já existe na wordlist *pode ter caracteres excessivos ou em quantidade insuficiente')
    time.sleep(1.5)
    print('Gerando uma senha :D...')
    time.sleep(2.0)    
    while nova_senha in texto:
        print('Nova senha já existe... gerando nova')
        nova_senha = gerador_senha(8)
    print(nova_senha + "\n senha segura, não existe na wordlist")
    
    








            
            
