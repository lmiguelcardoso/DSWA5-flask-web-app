# A very simple Flask Hello World app for you to get started with...
from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return """
    <h1>Avaliação contínua: Aula 030</h1>
    <ul>
    <li>
        <a href="/">Home</a>
    </li>
    <li><a href="/user/Fabio%20Teixeira/PT23820X/IFSP"> Identificação </a></li>
    <li><a href="/contextorequisicao"> Contexto da requisição </a></li>
    </ul>
    """

@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identificacao(nome,prontuario,instituicao):
    return f"""
  <h1>Avaliação contínua: Aula 030</h1>
  <h2>Aluno: {nome}</h2>
  <h2>Prontuário: {prontuario}</h2>
  <h2>Instituição: {instituicao}</h2>

  <p><a href="/">Voltar</a></p>
  """
     


@app.route('/contextorequisicao')
def contextoReq():
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    domain = request.url_root
    return f"""
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Seu navegador é: {user_agent}</h2>
    <h2>O Ip do computador remoto é: {ip}</h2>
    <h2>O O host da aplicação é: {domain}</h2>
    <p>
        <a href="/">Voltar</a>
    </p>
    """


