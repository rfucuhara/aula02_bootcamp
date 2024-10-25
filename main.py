# Exemplo que causa TypeError
try:
    resultado = len('Rafael')
    print(resultado)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro
else:
    print("Ocorreu tudo bem")
finally:
    print("O importante é participar")