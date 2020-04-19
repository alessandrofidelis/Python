from socket import *
from threading import Thread

def criptar(mensagem):
	zenit, polar = 'zenit', 'polar'
	final_message = ''
	message = mensagem
	n = 0
	for i in range(len(message)):
		x = message[n]
		if x in zenit:
			x = int(zenit.find(message[n]))
			final_message += polar[x]
		elif x in polar:
			x = int(polar.find(message[n]))
			final_message += zenit[x]
		else:
			final_message += message[n]
		n += 1
	return final_message
	


def atende (conn, cliente):
	conn.settimeout(10.00)
	while True:
		try:
			data = conn.recv (4096)
			
		except:
			#print ("Erro na conexão com o cliente "+str(cliente))
			print('Erro na conexão com o cliente {}'.format(cliente))
			break

		if data == b'':
			continue
		
		mensagem = data.decode("utf-8")
		resultado = criptar(mensagem)
		
		try:
			conn.send (str.encode (resultado, "UTF-8"))
		except:
			break

	print ("Fim da conexao com "+str(cliente))
	conn.close

s = socket ()
host = "0.0.0.0"
porta = 8729
s.bind ((host, porta))
s.listen (100)
nthr = 0

while True:
        (conn, cliente) = s.accept ()

        print ("Recebi a conexao de "+str(cliente))
        nthr += 1
        print ("Criando thread "+str(nthr))
        t = Thread(target=atende,args=(conn, cliente,))
        t.start()