from flask import Flask  #importa a biblioteca

app = Flask(__name__) #cria a aplicação

@app.route('/') #define a rota - caminho da página
def home(): #cria a função que executa a página
    return 'Hello World!' #imprime Olá na tela 

@app.route('/contato')
def contato():
    return 'Telefone: 11 973207061 \n Endereço: Santana de Parnaiba'

if __name__ == '__main__':
    app.run(debug=True)