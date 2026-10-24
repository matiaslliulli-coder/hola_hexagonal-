# Hola Hexagonal (Django + Arquitectura Hexagonal)

## Como levantarlo
1. Crear entorno virtual:   python -m venv venv
2. Activarlo:               venv\Scripts\activate   (Windows)  |  source venv/bin/activate (Linux/Mac)
3. Instalar Django:         pip install -r requirements.txt
4. Levantar el servidor:    python manage.py runserver
5. Probar en el navegador:  http://127.0.0.1:8000/saludar/matias/
   Respuesta:               {"mensaje": "hola MATIAS"}

## Otros endpoints
- POST http://127.0.0.1:8000/saludar/   con JSON {"nombre": "matias"}
- GET  http://127.0.0.1:8000/saludos/   historial de saludos (en memoria)

## Tests
python manage.py test
