import pandas as pd
import requests
import json
import os 
from flask import (Flask, render_template, request, redirect, 
                   url_for, session, flash)
from functools import wraps

# --- Configuración de la App ---
app = Flask(__name__)
# Esta 'llave secreta' es OBLIGATORIA para que 'session' funcione
app.secret_key = 'tu_llave_secreta_puede_ser_cualquier_texto' 

# --- Configuración del Portal ---
URL_API_PORTAL = 'https://portal.tecnologico.edu/api/v1/alumnos'
API_KEY = 'tu_llave_secreta_del_api'

# --- Login Simple (Para un admin interno, no necesita base de datos) ---
USUARIO_VALIDO = "admin_ite"
PASSWORD_VALIDO = "tecnologico2025"


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('Por favor, inicia sesión para acceder a esta página.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- Rutas de la Aplicación ---

@app.route('/')
def index():
    if 'logged_in' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        password = request.form['password']
        
        # Valida el usuario y contraseña
        if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
            session['logged_in'] = True
            session['username'] = usuario
            flash('¡Inicio de sesión exitoso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
            
    # Si es GET (solo cargar la página) o el login falló
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required  # <-- Esta página está protegida
def dashboard():
    # Pasa el nombre de usuario a la plantilla
    return render_template('dashboard.html', username=session['username'])


# --- Lógica del Proyecto (Modificada para la App Web) ---

@app.route('/procesar_excel', methods=['POST'])
@login_required # También protegido
def procesar_excel():
    # 1. Verificar que se subió un archivo
    if 'excel_file' not in request.files:
        flash('No se seleccionó ningún archivo.', 'danger')
        return redirect(url_for('dashboard'))
        
    archivo = request.files['excel_file']
    
    if archivo.filename == '':
        flash('Nombre de archivo vacío.', 'danger')
        return redirect(url_for('dashboard'))
        
    if archivo and archivo.filename.endswith('.xlsx'):
        try:
            # 2. Leer el Excel directamente desde el archivo subido
            df_alumnos = pd.read_excel(archivo)
            df_alumnos = df_alumnos.dropna(how='all')
            
            if df_alumnos.empty:
                flash('El archivo Excel está vacío o no tiene datos.', 'warning')
                return redirect(url_for('dashboard'))

            # 3. Procesar los datos (aquí va tu lógica de 'enviar_datos_al_portal')
            print(f"Iniciando procesamiento de {len(df_alumnos)} registros...")
            exitosos = 0
            fallidos = 0

            for persona in df_alumnos.to_dict('records'):
                datos_para_api = {
                    'nombre': persona.get('Nombre Alumno'), # Cambia por tus columnas reales
                    'numeroControl': persona.get('No. de Control'),
                    'carrera': persona.get('Carrera'),
                    'proyecto': persona.get('Nombre Proyecto Servicio') # Ejemplo
                    # ... etc.
                }
                
                if enviar_datos_al_portal(datos_para_api):
                    exitosos += 1
                else:
                    fallidos += 1
            
            flash(f'Proceso completado: {exitosos} exitosos, {fallidos} fallidos.', 'success')
            
        except Exception as e:
            flash(f'Error al procesar el archivo: {e}', 'danger')
            
        return redirect(url_for('dashboard'))
    else:
        flash('Formato de archivo no válido. Sube un .xlsx', 'danger')
        return redirect(url_for('dashboard'))

def enviar_datos_al_portal(datos_persona):
    """
    Esta es la misma función de la respuesta anterior.
    Envía los datos de UNA persona al portal usando un API REST.
    """
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    datos_json = json.dumps(datos_persona)
    
    try:
        response = requests.post(URL_API_PORTAL, data=datos_json, headers=headers, timeout=10)
        
        if response.status_code == 200 or response.status_code == 201:
            print(f"  -> Éxito: {datos_persona.get('nombre')}")
            return True
        else:
            print(f"  -> ERROR: {datos_persona.get('nombre')}. Código: {response.status_code} | {response.text}")
            return False
    except Exception as e:
        print(f"  -> ERROR de conexión: {e}")
        return False


# --- Iniciar la Aplicación ---
if __name__ == '__main__':
    # 'debug=True' permite ver cambios sin reiniciar el servidor (solo para desarrollo)
    app.run(debug=True, port=5000)