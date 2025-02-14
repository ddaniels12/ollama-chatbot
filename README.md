# Ollama Chatbot

Esta es una aplicación simple de chatbot usando la librería `langchain_ollama`.

## Requisitos

- Python 3.x
- Librería `langchain_ollama`
- Librería `langchain_core`

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/yourusername/ollama-chatbot.git
    cd ollama-chatbot
    ```

2. Instala las librerías requeridas:
    ```sh
    pip install langchain_ollama langchain_core
    ```

## Uso

Para activar el ambiente virtual:
```sh
.\chatbot\Scripts\activate.bat
```

Para iniciar el chatbot, ejecuta el siguiente comando en la terminal (cmd):
```sh
python main.py
```

Luego, abre tu navegador web y ve a `http://127.0.0.1:8000` para interactuar con el chatbot a través de la interfaz HTML.

## Cómo usar

- Escribe tu mensaje en el campo de texto y presiona el botón "Send" para interactuar con el chatbot.
- Las respuestas del chatbot aparecerán en el área de mensajes.

## Conexión desde otros dispositivos

Para conectarte desde otros dispositivos en la misma red WiFi, abre tu navegador web y ve a `http://<tu-ip-local>:8000`, donde `<tu-ip-local>` es la dirección IP de tu computadora en la red local.
