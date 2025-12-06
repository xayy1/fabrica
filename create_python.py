from db import conexao_banco # importa conexao com o banco 

nome = 'Xayane Dias'
telefone = '11 97070-7070'
email = 'xayanedias@gmail.com'
data_nascimento = '2007-06-27'
senha = '19022024'

conexao = conexao_banco() # inicia a conexao com o banco 

if conexao.is_connected(): #testar a conexao 
    cursor = conexao.cursor()

    sql = """
    INSERT INTO cliente(nome,telefone,email,data_nascimento,senha)
        VALUES(%s,%s,%s,%s,%s)
    """

    dados = (nome,telefone,email,data_nascimento,senha)

    #execução da gravação
    cursor.execute(sql,dados) 
    conexao.commit()

    #fechar a conexao com o banco
    cursor.close()
    conexao.close()

else:
    print("Falha de conexão com o banco")