from socket import  *

s = socket ()

minhastr = input("Informe uma frase para ser criptografada: ")
meusbytes=str.encode (minhastr, "UTF-8")

s.connect(("127.0.0.1", 8729))
s.send (meusbytes)

data = s.recv (1024)

print ('{}'.format(data.decode('utf-8')))

s.close ()