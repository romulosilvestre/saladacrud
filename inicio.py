from flask import Flask,render_template,request,flash,redirect,url_for
from crud import Crud
app = Flask(__name__)

app.secret_key = 'super secret key'

@app.route("/")
def mostrar_index():
    return render_template('index.html')

@app.route("/alovoce")
def alovoce():
    return render_template('alovoce.html')

@app.route("/salada")
def salada():
    return render_template('cadsalada.html')

@app.route("/cadsalada",methods=['POST','GET'])
def cad_salada():
    if request.method == 'POST':
        salada = request.form['salada']
        ingredientes = request.form['ingredientes']
        crud = Crud()
        crud.conectar()
        crud.inserir(salada,ingredientes)
        msg = "salada adicionada com sucesso!"
        return redirect(url_for('mostrar_index'))
    return render_template('cadsalada.html')


app.run(debug=True)

