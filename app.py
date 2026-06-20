#iportando as bibliotecas
from agno.knowledge.chunking import markdown
from flask import Flask, jsonify, request
from flask_cors import CORS

from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv

#leitura da chave de api
load_dotenv()

#criar o app
app = Flask(__name__)

#habilitar o CORS
CORS(app)

#criar  o agente
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="ocê é um agente virtual do Hotel Travesseiro Nervoso, slogan: Aqui até a insônia dorme"
    "Você responde de forma clara e humorada, informações sobre quartos,serviços, reservas e preços"
    "Quarto Standard ($500), Quarto Deluxe ($700), Quarto Suíte Presidencial ($1000)"
    "Serviços oferecidos: Academia, Café da Manhã, Lavanderia, Restaurante, Piscina"
    "Não inclua icones em markdown nas respostas, como: ##, **",
markdown=True
)

@app.route("/", methods=["GET"])
def testar():
    return jsonify({"mensage": "API funcionando"})

#criar a rota e o metodos POST
@app.route("/chat", methods=["POST"])
def pergunta():
    dados= request.get_json()
    pergunta = dados["pergunta"]

    resposta = agente.run(pergunta)
    return jsonify({"resposta":resposta.content})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)