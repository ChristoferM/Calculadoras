from flask import Flask,render_template,redirect, url_for, request
app = Flask(__name__)

@app.route('/RutaEjemplo')
def hello_world():

    BackEndvar= "Varible Back"
    varInt= 0

    return render_template("ejemplo.html",FrontEndvar=BackEndvar,varInt=varInt)


    
if __name__=="__main__":
    app.run('0.0.0.0', 5000, debug=True)