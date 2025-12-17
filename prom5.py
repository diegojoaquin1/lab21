# Laboratorio Nro 22 Ejercicio 5
# Autor: [Tu Nombre]
# Colaboró: Gemini AI

from wsgiref.simple_server import make_server
import json

def app(environ, start_response):
    path = environ.get("PATH_INFO", "/")
    
    if path == "/":
        status = "200 OK"
        headers = [("Content-Type", "text/html; charset=utf-8")]
        respuesta = b"<h1>Bienvenido al Servidor Estatico</h1><p>Esta es la raiz.</p>"
    
    elif path == "/saludo":
        status = "200 OK"
        headers = [("Content-Type", "application/json")]
        data = {"msg": "Hola"}
        respuesta = json.dumps(data).encode("utf-8")
    
    else:
        status = "404 Not Found"
        headers = [("Content-Type", "text/plain")]
        respuesta = b"Ruta no encontrada"

    start_response(status, headers)
    return [respuesta]

server = make_server("localhost", 8000, app)
print("Servidor corriendo en http://localhost:8000")
print("Prueba / para HTML o /saludo para JSON")
server.serve_forever()