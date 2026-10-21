from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    proyectos = [
        {"nombre": "Reciclar papel", "descripcion": "Reutiliza hojas y separa el papel para reducir residuos.", "icono": "📄"},
        {"nombre": "Ahorrar agua", "descripcion": "Cierra la llave mientras te cepillas los dientes y repara fugas.", "icono": "💧"},
        {"nombre": "Cuidar las plantas", "descripcion": "Riega las plantas con la cantidad necesaria y aprovecha el agua de lluvia.", "icono": "🌱"},
    ]
    return render_template("index.html", proyectos=proyectos)

if __name__ == "__main__":
    app.run(debug=True)
