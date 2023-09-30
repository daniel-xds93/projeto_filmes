from flask import Flask, render_template

# a linha abaixo eu inicio a variavel 
# responsavel por conter o projeto
app = Flask(__name__)

@app.route("/ola") # app.route() -> cria uma rota de acesso
def inicia():
    return "<h1>Essa é a estrutura flask</h1>"

@app.route("/lista")
def lista():
    listaFilmes = ["Matrix", "Divertidamente", 
                   "Se beber não case", "O sucessor"]
    
    return render_template("lista.html", 
                           titulo = "Lista de Filmes e Séries",
                           todosFilmes = listaFilmes)

# o comando dentro do run não pode subir para produção
app.run() # 