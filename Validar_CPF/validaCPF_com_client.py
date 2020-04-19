from socket import  *

s = socket()

minhastr = input('Informe o cpf: ')

print (minhastr)
meusbytes=str.encode (minhastr, "UTF-8")
print (meusbytes)

s.connect(("127.0.0.1", 8729))
s.send (meusbytes)

data = s.recv (1024)

print (data.decode("utf-8"))

s.close ()