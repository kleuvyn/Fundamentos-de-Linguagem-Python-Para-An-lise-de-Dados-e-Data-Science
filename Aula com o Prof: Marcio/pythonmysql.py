# Utilizando python, conecte ao banco de dados

import mysql
import _mysql_connector


#  informações de conexão
dados_conexao = {
    "host": "seu_host",
    "user": "seu_usuario",
    "password": "sua_senha",
    "database": "seu_banco_de_dados"
}
#  estabelecer uma conexão
try:
    conexao = _mysql_connector.connect(**dados_conexao)
    if conexao.is_connected():
        print("Conexão bem-sucedida!")

        # Agora você pode executar consultas SQL usando o objeto 'conexao'

        # Exemplo de consulta SQL
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, idade FROM tabela_exemplo")

        # Recupere os resultados
        for (nome, idade) in cursor:
            print(f"Nome: {nome}, Idade: {idade}")

        # Feche o cursor
        cursor.close()

except mysql.connector.Error as erro:
    print(f"Erro na conexão: {erro}")

finally:
    # Certifique-se de fechar a conexão, independentemente do resultado
    if conexao.is_connected():
        conexao.close()