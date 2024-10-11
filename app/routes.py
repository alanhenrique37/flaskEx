from app import app
from flask import render_template
from flask import request
import requests
import json
link = "https://flasktintalan-default-rtdb.firebaseio.com/"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',titulo="")

@app.route('/contato')
def contato():
    return render_template('contato.html',titulo="ENTRE EM CONTATO!")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html',titulo="CADASTRO")

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados = {"cpf":cpf, "nome":nome, "telefone":telefone, "endereco":endereco}
        requisicao = requests.post(f'{link}/cadastro/.json', data = json.dumps(dados))
        return 'Cadastrado com Sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n +{e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        return dicionario


    except Exception as e:
        return f'Algo deu errado\n {e}'


@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        idCadastro= ""
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == 'oi':
                idCadastro = codigo
                return idCadastro
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome":"joão"}
        requisicao = requests.patch(f'{link}/cadastro/-O8miGRj3JAR8IIFe-Rx/.json', data = json.dumps(dados))
        return 'Atualizado com Sucesso!'
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastro/-O8miGRj3JAR8IIFe-Rx/.json')
        return "Excluido com Sucesso!"

    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/consultarNome')
def consultarNome():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        nomeCadastro= ""
        for nome in dicionario:
            nome = dicionario[nome]['nome']
            if nome == '123':
                nomeCadastro = nome
                return nomeCadastro
    except Exception as e:
        return f'Algo deu errado\n {e}'


@app.route('/atualizarNome')
def atualizarNome():
    try:
        dadosNome = {"nome":"jão"}
        requisicao = requests.patch(f'{link}/cadastro/-O8miGRj3JAR8IIFe-Rx/.json', data = json.dumps(dadosNome))
        return 'Atualizado com Sucesso!'
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/consultarEndereco')
def consultarEndereco():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        enderecoCadastro= ""
        for dad in dicionario:
            endereco = dicionario[dad]['endereco']
            if endereco == 'rua do carlos':
                enderecoCadastro = endereco
                return enderecoCadastro
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/atualizarEndereco')
def atualizarEndereco():
    try:
        dadosEndereco = {"endereco":"rua do alan"}
        requisicao = requests.patch(f'{link}/cadastro/-O8miGRj3JAR8IIFe-Rx/.json', data = json.dumps(dadosEndereco))
        return 'Atualizado com Sucesso!'
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/consultarCPF')
def consultarCPF():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        cpfCadastro = ""
        for das in dicionario:
            cpf = dicionario[das]['cpf']
            if cpf == '345':
                cpfCadastro = cpf
                return cpfCadastro
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/atualizarCpf')
def atualizarCpf():
    try:
        dadosCpf = {"cpf":"224399"}
        requisicao = requests.patch(f'{link}/cadastro/-O8miGRj3JAR8IIFe-Rx/.json', data = json.dumps(dadosCpf))
        return 'Atualizado com Sucesso!'
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/consultarTelefone')
def consultarTelefone():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        telefoneCadastro = ""
        for tele in dicionario:
            tele = dicionario[tele]['telefone']
            if tele == '2333':
                telefoneCadastro = tele
                return telefoneCadastro
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/atualizarTelefone')
def atualizarTelefone():
    try:
        dadosTelefone = {"telefone":"2324399"}
        requisicao = requests.patch(f'{link}/cadastro/-O8miGRj3JAR8IIFe-Rx/.json', data = json.dumps(dadosTelefone))
        return 'Atualizado com Sucesso!'
    except Exception as e:
        return f'Algo deu errado\n {e}'


