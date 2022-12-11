import pyAesCrypt


password = input('Введите пароль для шифрования файла: ')

# #encrypt
# pyAesCrypt.encryptFile('data.txt','data.aes',password)

#decrypt
pyAesCrypt.decryptFile('data.aes', 'dataout.txt', password)