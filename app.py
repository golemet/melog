from transformers import pipeline
from flask import Flask, request

# Especifica el modelo español
model_name = "flax-community/gpt-2-spanish"

# Inicializa el pipeline. device=-1 usa la CPU por defecto, que es lo más común en contenedores.
# Si tienes GPU y Docker configurado para usarla (con nvidia-docker), puedes cambiar a device=0.
generator = pipeline('text-generation', model=model_name, device=-1)

def gpt(texto):
    generated_text = generator(texto, do_sample=True, pad_token_id=50256, max_length=30)[0]["generated_text"]
    return generated_text

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta de inicio (GET)
@app.route('/', methods=['GET'])
def inicio():
    return "Golemet API Flask"

@app.route('/golemet')
def procesar_cadena():
    texto_recibido = request.args.get('cadena', '???')
    texto_generado = gpt(texto_recibido)
    return f"☞ {texto_generado}"

# Ejecutar la aplicación
if __name__ == '__main__':
    # Se ejecuta en 0.0.0.0 para ser accesible fuera del localhost del contenedor
    app.run(host='0.0.0.0', port=5000)
