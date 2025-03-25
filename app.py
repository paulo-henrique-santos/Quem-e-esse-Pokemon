from flask import Flask, render_template, request, redirect
import requests
import random

app = Flask(__name__)

nome = ""
imagem = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/facil', methods=['GET', 'POST'])
def facil():
    global nome
    global imagem
    if request.method == 'GET':
        aleatorio = random.randint(0, 151)
        API_ENDPOINT = f"https://pokeapi.co/api/v2/pokemon/{aleatorio}"
        response = requests.get(API_ENDPOINT)
        if response.status_code == 200:
            data = response.json()
            nome = data["forms"][0]["name"]
            imagem = data["sprites"]["other"]["official-artwork"]["front_default"]
            return render_template("facil.html", nome=nome, imagem=imagem)

        return render_template("facil.html", nome=nome, imagem=imagem)

        return "Erro ao buscar dados da API", 500

    if request.method == "POST":
        resposta = request.form.get("nome", "").strip().lower()

        if resposta:  # Só faz a verificação se algo foi digitado
            if resposta == nome.lower():
                msg = "✅ Você Acertou! 🎉"
                
            else:
                msg = f"❌ Errado! O nome é {nome.capitalize()}."
                

            return render_template("facil.html", nome=nome, imagem=imagem, msg=msg)

@app.route('/medio', methods=['GET', 'POST'])
def medio():
    global nome
    global imagem
    if request.method == 'GET':
        aleatorio = random.randint(0, 151)
        API_ENDPOINT = f"https://pokeapi.co/api/v2/pokemon/{aleatorio}"
        response = requests.get(API_ENDPOINT)
        if response.status_code == 200:
            data = response.json()
            nome = data["forms"][0]["name"]
            imagem = data["sprites"]["other"]["official-artwork"]["front_default"]
            return render_template("facil.html", nome=nome, imagem=imagem)

        return render_template("facil.html", nome=nome, imagem=imagem)

        return "Erro ao buscar dados da API", 500

    if request.method == "POST":
        resposta = request.form.get("nome", "").strip().lower()

        if resposta:  # Só faz a verificação se algo foi digitado
            if resposta == nome.lower():
                msg = "✅ Você Acertou! 🎉"
                
            else:
                msg = f"❌ Errado! O nome é {nome.capitalize()}."
                

            return render_template("facil.html", nome=nome, imagem=imagem, msg=msg)

@app.route('/dificil', methods=['GET', 'POST'])
def dificil():
    global nome
    global imagem
    if request.method == 'GET':
        aleatorio = random.randint(0, 151)
        API_ENDPOINT = f"https://pokeapi.co/api/v2/pokemon/{aleatorio}"
        response = requests.get(API_ENDPOINT)
        if response.status_code == 200:
            data = response.json()
            nome = data["forms"][0]["name"]
            imagem = data["sprites"]["other"]["official-artwork"]["front_default"]
            return render_template("facil.html", nome=nome, imagem=imagem)

        return render_template("facil.html", nome=nome, imagem=imagem)

        return "Erro ao buscar dados da API", 500

    if request.method == "POST":
        resposta = request.form.get("nome", "").strip().lower()

        if resposta:  # Só faz a verificação se algo foi digitado
            if resposta == nome.lower():
                msg = "✅ Você Acertou! 🎉"
                
            else:
                msg = f"❌ Errado! O nome é {nome.capitalize()}."
                

            return render_template("facil.html", nome=nome, imagem=imagem, msg=msg)


if __name__ == '__main__':
    app.run(debug=True)