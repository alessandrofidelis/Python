from socket import *
from threading import Thread
import re


def valida_cpf(cpf):
    if not cpf:
        return False

    print(cpf)
    cpf = re.sub('[^0-9]', '', cpf)
    print(cpf)

    novo_cpf = _calcula_digitos(cpf[:9])
    novo_cpf = _calcula_digitos(novo_cpf)

    if novo_cpf == cpf:
        return True
    return False


def _calcula_digitos(fatia_cpf):
    if not fatia_cpf:
        return False

    sequencia = fatia_cpf[0] * len(fatia_cpf)

    if sequencia == fatia_cpf:
        return False

    soma = 0
    for chave, multiplicador in enumerate(range(len(fatia_cpf) + 1, 1, -1)):
        soma += int(fatia_cpf[chave]) * multiplicador
    resto = 11 - (soma % 11)
    resto = resto if resto <= 9 else 0

    return fatia_cpf + str(resto)


def atende(conn, cliente):
    while True:
        data = conn.recv(4096)

        if not data or len(data) == 0:
            break

        cpf = data.decode("utf-8")
        validade = valida_cpf(cpf)

        if validade:
            resultado = "VÁLIDO"
        else:
            resultado = "INVÁLIDO"

        conn.send(str.encode(resultado, "UTF-8"))

    print("Fim da conexao com " + str(cliente))

    conn.close()


s = socket()

host = "0.0.0.0"
porta = 8729
s.bind((host, porta))
s.listen(10)
nthr = 0

while True:
    (conn, cliente) = s.accept()

    print("Recebi a conexao de " + str(cliente))
    nthr += 1
    print("Criando thread " + str(nthr))
    t = Thread(target=atende, args=(conn, cliente,))
    t.start()
