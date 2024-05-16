from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')

app = Flask(__name__)
CORS(app)
client = OpenAI(api_key=API_KEY)

# Consulta a la API para obtener datos de experiencias o salas
def consultar_api(tipo):
    url = "https://dreamlab-api.azurewebsites.net/"
    if tipo == "experiencias":
        url += "experiencias"
    elif tipo == "salas":
        url += "salas"
    else:
        return "Error en el tipo de tabla a consultar"

    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()

        texto = ""
        for item in datos:
            if 'idExperiencia' in item:
                texto += f"Tipo: Experiencia, Id: {item['idExperiencia']}, {item['nombre']}: {item['descripcion']}. \n"
            elif 'idSala' in item:
                texto += f"Tipo: Sala, Id: {item['idSala']}, {item['nombre']}: {item['descripcion']}. \n"

        return texto
    else:
        return "Error al obtener los datos de la API."

# Consulta recomendaciones a chatgpt
def preguntar(prompt):
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    model="gpt-3.5-turbo")

    return response.choices[0].message.content.strip()

@app.route('/recomendar', methods=['POST'])
def recomendar():
    data = request.get_json()
    user_input = data['prompt']
    # Definición de instrucciones
    Instrucciones = "Instrucciones: Eres un asistente virtual que solamente recomienda algunos de las siguiente salas y/o experiencias en un laboratorio dependiendo de lo que el usuario diga y la descripción del lugar. Las experiencias son:\n"
    Instrucciones += str(consultar_api("experiencias")) 
    Instrucciones += "\n Las salas son:\n"
    Instrucciones += str(consultar_api("salas")) 
    Instrucciones += "Es importante que solo respondas con el Tipo y el Id de las 3 recomendaciones que más se acerquen a lo que pide el usuario a manera de lista de recomendaciones, con el siguiente formato (usando un ejemplo): 1. Tipo: experiencias, Id: 1, Hackers Event y así sucesivamente con las 3, el tipo debe estar en minusculas y en plural (osea solo -experiencias- o -salas-). También es importante que siempre des 3 recomendaciones, PERO es mucho más importante que cuando ninguna experiencia o sala del catálogo es cercana a lo que pide el usuario debes regresar una sola respuesta con lo siguiente _0. Tipo: Error, Id: 0_. SOLO PUEDES HACER UNA RESPUESTA A LA VEZ, es decir no puedes responder por el usuario. Recuerda que si ninguna sala o experiencia es una buena recomendación para el usuario entonces responde _0. Tipo: Error, Id: 0_ \n"

    conversacion = Instrucciones
    conversacion += "\nUsuario: " + user_input + "\nAI:" 
    response = preguntar(conversacion)
    # print("response: ", response)
    return jsonify({"processed_text": response})

@app.route('/', methods=['GET'])
def healthCheck():
    return jsonify({"processed_text": "Todo bien, todo correcto:)"})

if __name__ == '__main__':
    app.run(debug=True) # Ejecutar la aplicación Flask en modo debug para facilitar el desarrollo