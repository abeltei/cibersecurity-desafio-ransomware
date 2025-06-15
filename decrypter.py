import os
import pyaes

# Abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave para descriptografia (deve ser exatamente a mesma da criptografia)
key = b"testeransomwares"[:16]  # Pegando os primeiros 16 bytes

# Descriptografar os dados
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo descriptografado
new_file = "teste.txt"
with open(new_file, "wb") as file:
    file.write(decrypt_data)

print(f"Arquivo '{file_name}' descriptografado com sucesso para '{new_file}'!")
