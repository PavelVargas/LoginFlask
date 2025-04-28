import os
from flask import Flask ,render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



   

@app.route("/Loguear", methods=["POST","GET"])
def Loguear():
    if request.method == "POST":
        User = request.form["User"]
        Password = request.form["Password"]
        if User and Password:
            usuarios = [{"user":"Jonatan","password":"123"},
                        {"user":"Jonatan2","password":"1234"}]

            for user in usuarios:
                if user["user"] == User and user["password"] == Password:
                    return "Hola "+ User
            return "Usuario Incorrecto"


            
        else:
            return "Porfavor compete los campos"
    else:
        return"Metodo no es POST"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa el puerto de Railway
    app.run(host='0.0.0.0', port=port)
