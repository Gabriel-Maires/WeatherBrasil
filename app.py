from flask import Flask, render_template, request, flash
import requests

def resultado(lat, lon):
    api_key = "" # Inserir uma chave da API válida. 
    OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "exclude": "hourly,minutely,daily"
    }

    response = requests.get(OWM_Endpoint, params=weather_params)

    response.raise_for_status()
    data_json = response.json()
    clima_atual = data_json["current"]["weather"][0]["id"]

    if int(clima_atual) >= 200 and int(clima_atual) <= 232:
        retorno = "Melhor pegar um guarda chuva! Tempestade!"
    elif int(clima_atual) >= 500 and int(clima_atual) <= 531:
        retorno = "Melhor pegar um guarda chuva! Está Chovendo!"
    elif int(clima_atual) >= 600 and int(clima_atual) <= 622:
        retorno = "É natal? Pois está nevando!!!"
    elif int(clima_atual) > 781 and int(clima_atual)<= 800:
        retorno = "Está tudo limpo! Ótimo para sair de casa!"
    elif int(clima_atual) >= 801:
        retorno = "Está nublado!"
    return retorno

app = Flask(__name__)
app.secret_key = "samhow"

@app.route("/home")
def home():
    flash("Seu resultado irá aparecer aqui!")
    return render_template("index.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    flash(resultado(lat=float(str(request.form["input1"])), lon=float(str(request.form["input2"]))))
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True,port=5001)