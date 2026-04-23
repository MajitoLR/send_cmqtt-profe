import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# ------------------ MQTT ------------------
values = 0.0
act1="OFF"

def on_publish(client,userdata,result):
    print("el dato ha sido publicado \n")

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

broker="157.230.214.127"
port=1883
client1= paho.Client("GIT-MJ")
client1.on_message = on_message

# ------------------ ESTILO ROSADO ------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #FAD1E6, #F3B6D4);
    font-family: 'Segoe UI', sans-serif;
}

/* Espacio arriba */
.block-container {
    padding-top: 4rem;
}

/* Título */
h1 {
    text-align: center;
    color: #7A2E5E;
    font-weight: 800;
    margin-bottom: 25px;
}

/* Elimina bloques vacíos blancos */
div[data-testid="stMarkdownContainer"]:empty {
    display: none;
}

/* Tarjeta */
.card {
    background: white;
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 10px 25px rgba(214, 51, 132, 0.25);
    max-width: 500px;
    margin: auto;
    text-align: center;
}

/* Subbloques */
.block {
    background: #FCE4F1;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 15px;
    color: #5A2A4D;
    font-size: 14px;
}

/* Botones */
.stButton>button {
    background: #F472B6;
    color: white;
    border-radius: 15px;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton>button:hover {
    background: #EC4899;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ------------------ UI ------------------
st.title("💗 Control MQTT Inteligente")

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
<div class="block">
Controla dispositivos en tiempo real mediante MQTT.
</div>

<div class="block">
Puedes encender o apagar el sistema 🔌 y enviar valores analógicos.
</div>

<div class="block">
Conectado a Wokwi para simular el comportamiento en vivo.
</div>
""", unsafe_allow_html=True)

# ------------------ INFO PYTHON ------------------
st.write("🧠 Versión de Python:", platform.python_version())

# ------------------ BOTONES ON/OFF ------------------
col1, col2 = st.columns(2)

with col1:
    if st.button('🟢 ON'):
        act1="ON"
        client1= paho.Client("GIT-MJ")                           
        client1.on_publish = on_publish                          
        client1.connect(broker,port)  
        message =json.dumps({"Act1":act1})
        client1.publish("cmqtt_s", message)

with col2:
    if st.button('🔴 OFF'):
        act1="OFF"
        client1= paho.Client("GIT-MJ")                           
        client1.on_publish = on_publish                          
        client1.connect(broker,port)  
        message =json.dumps({"Act1":act1})
        client1.publish("cmqtt_s", message)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------ SLIDER ------------------
values = st.slider('🎚️ Ajusta el valor',0.0, 100.0)
st.write('Valor seleccionado:', values)

# ------------------ ENVÍO ANALÓGICO ------------------
if st.button('📡 Enviar valor'):
    client1= paho.Client("GIT-MJ")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Analog": float(values)})
    client1.publish("cmqtt_a", message)

st.markdown('</div>', unsafe_allow_html=True)
