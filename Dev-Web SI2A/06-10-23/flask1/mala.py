from flask import Flask, render_template, request

app = Flask(__name__)

"Quando o usuário abre uma página chamada /mala, recebe de volta a string “etiqueta de mala em construcao”"
@app.route('/mala', methods=['GET'])
def mala():
    return "Etiqueta de mala em construção"

@app.route('/gato', methods=['GET'])
@app.route('/cachorro', methods=['GET'])
def gato():
    return "Outro gato!"

@app.route('/mala2', methods=['GET'])
def mala2():
    if 'endereco' in request.args:
        print (len(request.args['endereco']))
    return render_template("mala.html") # templates/mala.html
    # um arquivo mala.hmtl na pasta templates


@app.route("/")
def main():
    return "acesse a url /pergunta"

@app.route("/frutaria")
def frutas():
    return "banana, abacaxi, melao"


if __name__ == '__main__':
    app.run(debug=True, port=5002)

