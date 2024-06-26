from flask import Flask, render_template, request
# essa linha de cima: vou usar a biblioteca flask
# nessa biblioteca, temos as variaveis Flask, render_template, request que eu quero

# pra poder usar tem que estar instalada, python -m pip install flask requests
# (ou, no linux e no mac: python3 -m pip install flask requests)

app = Flask(__name__)

@app.route('/pergunta', methods=['GET'])
def index():
    # quando o usuario envia o form, a url fica parecida com
    # localhost:5002/pergunta?idade=12
    # isso corresponde a um dicionario request.args {'idade':12}
    # portanto, 'idade' é uma das chaves (keys) do request.args
    
    
    print(dict(request.args))
    #http://localhost:5002/pergunta?idade=40&nome=Marcos
    #o print do request.args resulta: {'idade': '40', 'nome': 'Marcos'}
    #http://localhost:5002/pergunta?idade=40
    #o print do request.args resulta: {'idade': '40'}
    #http://localhost:5002/pergunta
    #o print do request.args resulta: {}

    # da onde vieram essas variaveis?
    # ou o usuário editou a url na mao, ou
    # um formulário especificou. A gente vê isso mais tarde
    # dica: <input type="text" name="idade">

   
    #ciclo com idade
    if 'idade' in request.args.keys():
        # se a url tinha a chave idade, o dicionario tb vai ter
        # se o dicionario tem, esse if executa 
        idade = request.args['idade']
        idade = int(idade) #tudo que um form envia sao strings
        #se quiser um numero, vai ter que converter
        idades_depois = [idade+1,idade+2,idade+3]
        # preenche o arquivo templates/idade.html com as variaveis idade e idades_depois
        return render_template('idade.html', 
                               idade=idade, 
                               idades_depois=idades_depois)
    
    #ciclo sem idade
    else:
        return render_template('form.html')

@app.route("/")
def main():
    return "acesse a url /pergunta"

@app.route("/frutaria")
def frutas():
    return "banana, abacaxi, melao"

if __name__ == '__main__':
    app.run(debug=True, port=5002)


# ciclo com idade enviada
# firefox                                                    # flask
# usuario aperta submit no form
#  firefox monta a URL, incluindo
#   as variaveis especificadas no form
#   <input type="text" name="idade"> tinha desenhado
#   uma caixinha, quando o usuario enviou,
#   o que ele digitou na caixinha foi pra variável
#   "idade"
#       - GET http://localhost:5002/pergunta?idade=12 ->     url="http://localhost:5002/pergunta?idade=12"
#                                                            request.args={"idade":"12"}
#                                                            html = '''sua idade é 12
#                                                                      <ul>
#                                                                         <li> 13 </li>
#                                                                         <li> 14 </li>
#                                                                      </ul>'''
#      <------------------------html--------------------
#firefox desenha
# o html

# ciclo sem idade
# firefox                                                    # flask
#   usuario digitou a url
#       ----- GET http://localhost:5002/pergunta------->     url="http://localhost:5002/pergunta"
#                                                            request.args={}
#                                                            html = '''<h1>Qual a sua idade?</h1>
#                                                                      <form method="GET" action="/pergunta">
#                                                                      <div>
#                                                                          <input type="text" name="idade">
#                                                                      </div>
#                                                                      <input type="submit" value="Submit">
#                                                                      </form>'''
#      <------------------------html--------------------
#firefox desenha
# o html

# funcao index versus funcao frutas:
# @app.route('/pergunta', methods=['GET'])
# def index():
# quando o usuário manda a url localhost:5002/pergunta,
# o flask executa a funcao index
# @app.route("/frutaria")
# def frutas():
# quando o usuário manda a url localhost:5002/frutaria,
# o flask executa a funcao frutas

