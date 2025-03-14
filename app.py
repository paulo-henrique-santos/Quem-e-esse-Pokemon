from flask import Flask, render_template, request, redirect
import requests
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    aleatorio = random.randint(1, 151)
    API_ENDPOINT = f"https://pokeapi.co/api/v2/pokemon/{aleatorio}"
    response = requests.get(API_ENDPOINT)
    if response.status_code == 200:
        data = response.json()
        nome = data["forms"][0]["name"]
        imagem = data["sprites"]["other"]["official-artwork"]["front_default"]

        msg = None  # Inicializa sem mensagem

        if request.method == "POST":
            resposta = request.form.get("res", "").strip().lower()

            if resposta:  # Só faz a verificação se algo foi digitado
                if resposta == nome.lower():
                    msg = "✅ Você Acertou! 🎉"
                else:
                    msg = f"❌ Errado! O nome correto era {nome.capitalize()}."

        return render_template("index.html", nome=nome, imagem=imagem, msg=msg)

    return "Erro ao buscar dados da API", 500

if __name__ == '__main__':
    app.run(debug=True)