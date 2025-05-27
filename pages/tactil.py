import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("MDGit25")
client1.on_message = on_message



st.title("Cerradura Táctil")

if st.button('Open'):
    act1="Abre"
    client1= paho.Client("MDGit25")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"gesto":act1})
    ret= client1.publish("MDCasa", message)
    st.image("open.png")
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('Lock'):
    act1="Cierra"
    client1= paho.Client("MDGit25")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"gesto":act1})
    ret= client1.publish("MDCasa", message)
    st.image("lock.png", width=200)
  
    
else:
    st.write('')
