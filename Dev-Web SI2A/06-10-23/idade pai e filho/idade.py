from flask import Flask, render_template, request
# essa linha de cima: vou usar a biblioteca flask
# nessa biblioteca, temos as variaveis Flask, render_template, request que eu quero

# pra poder usar tem que estar instalada, python -m pip install flask requests
# (ou, no linux e no mac: python3 -m pip install flask requests)

app = Flask(__name__)

@app.route("/idades")
def idades():
    if ("idade_pai" in request.args):
        i_pai    = request.args['idade_pai']
        i_pessoa = request.args['idade_pessoa']
        diferenca = int(i_pai)-int(i_pessoa)
        if diferenca < 0:
            return "Seu pai provavelmente é mais velho que você! Tente novamente"
        return render_template("idade_pai_respondido.html",
                               i_pai = i_pai,
                               idade_filho = i_pessoa,
                               diferenca = diferenca)
    return render_template("idade_pai.html")


if __name__ == '__main__':
    app.run(debug=True, port=5002)
