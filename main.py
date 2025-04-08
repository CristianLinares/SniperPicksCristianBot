import requests
import time

BOT_TOKEN = "7992107638:AAFZYhfHfnSh8Ns4xEoIQHS3oRX7Jjw-DQc"
CHAT_ID = "1389305238"

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": texto,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)
    print("Enviado:", texto)

def analizar_y_enviar():
    # Aquí simulamos un pick fuerte (luego será real con fuentes deportivas)
    pick = (
        "*[Análisis automático]*\n"
        "*Tenis de mesa - Liga Pro Checa*\n"
        "*Partido:* Novy vs. Trsek\n"
        "*Pick:* Más de 75.5 puntos totales\n"
        "*Stake:* 8/10\n"
        "*Confianza:* Alta\n"
        "*Probabilidad estimada: 73%*"
    )
    enviar_mensaje(pick)

# Ciclo automático que revisa cada 5 minutos (300 segundos)
while True:
    analizar_y_enviar()
    time.sleep(300)
