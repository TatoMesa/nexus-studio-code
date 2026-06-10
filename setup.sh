#!/bin/bash
echo "=== Nexus Studio Code — Setup ==="
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
echo ""
echo "Crear superusuario:"
python manage.py createsuperuser
echo ""
echo "Listo! Ejecutar con: python manage.py runserver"
