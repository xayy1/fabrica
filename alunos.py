import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "escola"
)

cursor = conexao.cursor()

def inserir_aluno (nome,idade,email):
    sql = "INSERT INTO alunos (nome,idade,email) VALUES (%s,%s,%s)"
    cursor.execute(sql,(nome,idade,email))
    conexao.commit()
    print("Aluno inserido com sucesso!")

def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    for linha in cursor.fetchall():
        print(linha)

def deleter_aluno(id):
    sql = "DELETE FROM alunos WHERE id=%s"
    cursor.execute(sql,(id))
    conexao.commit()
    print("Aluno delatado com sucesso!")

def atualizar_aluno(id,novo_nome,nova_idade,novo_email):
    sql = "UPDATE alunos SET nome=%s, idade=%s, email=%s WHERE id=%s"
    cursor.execute(sql,(novo_nome,nova_idade,novo_email,id))
    conexao.commit()
    print("Aluno atualizado com sucesso!")

if __name__ == "__main__":

    #inserir_aluno("Rodrigo de Le",18,"rodrigo.dele@yahoo.com.br")
    #listar_alunos()
    #deletar_aluno(7)
    #atualizar_aluno(5,"Rodrigo de Lê",20,"rodrigo.de.le@gmail.com")

cursor.close()
conexao.close()
