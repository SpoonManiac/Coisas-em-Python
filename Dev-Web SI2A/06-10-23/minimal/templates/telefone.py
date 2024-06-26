#Valida telefone com ddd
#Verifica se o telefone tem 9 ou 8 caracteres
#Verifica se o ddd tem 2 caracteres


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/telefone")
def telefones():
    if 'ddd' in request.args:
        ddd      = request.args['ddd']
        telefone = request.args['tel']
        #telefone_valido = len(telefone) == 9 or len(telefone) == 8
        if len(telefone) == 8: telefone_valido = True
        elif len(telefone) == 9: telefone_valido = True
        else: telefone_valido = False
        ddd_valido = len(ddd) == 2
        if not telefone_valido and not ddd_valido:
            resposta = "telefone e ddd invalidos"
        elif not telefone_valido:
            resposta = "telefone invalido"
        elif not ddd_valido:
            resposta = "ddd valido"
        else:
            resposta = "telefone e ddd ok"
        return render_template("verifica_telefone.html",resultado_verificacao = resposta)
    return render_template("form_telefone.html")
#http://localhost:5002/telefone?ddd=11&tel=3333

if __name__ == '__main__':
    app.run(debug=True, port=5002)
