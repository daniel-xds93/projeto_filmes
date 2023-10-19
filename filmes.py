from flask import Flask, render_template, request

# A linha abaixo eu crio uma classe
class Filme:
    # a linha abaixo define o que será carregado 
    # na inicialização da classe
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

filme01 = Filme("Tropa de Elite", '160 min.')
filme02 = Filme("Avatar", "180 min.")
filme03 = Filme("Rei leão", '145 min.')

# a linha abaixo é uma lista com as informações dos filmes
listaFilmes = [filme01, filme02, filme03]


# a linha abaixo eu inicio a variavel 
# responsavel por conter o projeto
app = Flask(__name__)




@app.route("/ola") # app.route() -> cria uma rota de acesso
def inicia():
    return "<h1>Essa é a estrutura flask</h1>"

@app.route("/lista")
def lista():
    #listaFilmes = ["Matrix", "Divertidamente", 
    #               "Se beber não case", "O sucessor"]

    
    
    return render_template("lista.html", 
                           titulo = "Lista de Filmes e Séries",
                           todosFilmes = listaFilmes)

# a rota abaixo é para renderizar a tela novo.html
@app.route('/novo')
def cadastro():
    return render_template('novo.html')

# a rota abaixo cria o vinculo entre os dados digitados
# e a lista
@app.route('/criar', methods=['POST', ])
def cadastra_registro(): # método para receber os dados digitatos
    titulo = request.form['titulo'] 
    # request vai pegar o que o usuario digitou
    duracao = request.form['duracao']

    # a variavel abaixo apenas  cria um novo filme
    addFilme = Filme(titulo, duracao)

    # abaixo eu adiciono o filme cadastrano na lista
    listaFilmes.append(addFilme)

    return render_template("lista.html", 
                           titulo = "Lista de Filmes e Séries",
                           todosFilmes = listaFilmes)


# o comando dentro do run não pode subir para produção
app.run() # 