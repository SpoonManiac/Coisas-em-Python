from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/idade', methods=['GET'])
def index():
    return "alguns anos"

@app.route("/")
def main():
    return "acesse a url /pergunta"

@app.route("/frutaria")
def frutas():
    return "banana, abacaxi, melao"

'''
ciclo da fruta
firefox                                                      flask
    usuario digita "localhost:5002/frutaria"
                    ---- GET localhost:5002/frutaria --->    url="localhost:5002/frutaria"
                                                             vou executar a funcao frutas, por causa
                                                             do @app.route("/frutaria")
                                                             ela retornou "banana, abacaxi, melao"
                    <--- "banana, abacaxi, melao"--------
    o firefox desenha essa string

firefox
    usuario digita "localhost:5002/idade"
                    ---- GET localhost:5002/idade ------>    url="localhost:5002/idade"
                                                             vou executar a funcao frutas, por causa
                                                             do @app.route("/idade")
                                                             ela retornou "alguns anos"
                    <--- "alguns anos"--------
    o firefox desenha essa string
                                                             '''          

if __name__ == '__main__':
    app.run(debug=True, port=5002)

