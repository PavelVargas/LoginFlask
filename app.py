import os
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

# Conexión a PostgreSQL en Railway
DATABASE_URL = os.environ.get('DATABASE_URL') or "postgresql://postgres:rySwamKWvHyDJVwYpHTdouOwkosOrXxr@postgres.railway.internal:5432/railway"

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Crear tabla si no existe
cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
""")
conn.commit()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Loguear", methods=["POST", "GET"])
def Loguear():
    if request.method == "POST":
        User = request.form["User"]
        Password = request.form["Password"]
        if User and Password:
            cur.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (User, Password))
            usuario = cur.fetchone()
            if usuario:
                return f"Hola {User}"
            else:
                return "Usuario Incorrecto"
        else:
            return "Por favor completa los campos"
    else:
        return "Método no es POST"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa el puerto de Railway
    app.run(host='0.0.0.0', port=port)
