# SERVICE UNION TEC 🎓

**Sistema de Sincronización de Datos de Servicio Social - Instituto Tecnológico de Ensenada.**

## 📋 Descripción

**Service Union Tec** es una herramienta web diseñada para resolver la problemática de duplicidad de captura de datos en el departamento de Servicio Social. Permite a los administradores cargar archivos de Excel (`.xlsx`) con información de alumnos y sincronizarlos automáticamente con el portal institucional a través de una API segura.

### 🚀 Características Principales

* **Autenticación Segura:** Acceso restringido mediante login administrativo.
* **Procesamiento Masivo:** Lectura y validación de archivos Excel usando `pandas`.
* **Sincronización API:** Envío automático de datos al servidor central del ITE.
* **Feedback Inmediato:** Reportes visuales de éxito o fallo por cada registro procesado.
* **Interfaz Intuitiva:** Dashboard limpio y fácil de usar.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Framework Web:** Flask
* **Manipulación de Datos:** Pandas, Openpyxl
* **Peticiones HTTP:** Requests
* **Frontend:** HTML5, CSS3

## 📦 Instalación y Despliegue

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### Prerrequisitos
* Git
* Python 3.10 o superior
* Acceso a internet (para instalar paquetes y conectar con la API)

### Pasos

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/SERVICE_UNION_TEC.git](https://github.com/tu-usuario/SERVICE_UNION_TEC.git)
   cd SERVICE_UNION_TEC
``

2.  **Crear y activar un entorno virtual:**

    ```bash
    # En Windows
    python -m venv venv
    venv\Scripts\activate

    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuración:**
    Asegúrate de configurar las variables de entorno en `app.py` o en un archivo `.env` (si aplica):

      * `SECRET_KEY`
      * `API_URL`
      * `API_KEY`

5.  **Ejecutar el servidor:**

    ```bash
    python app.py
    ```

    Visita `http://127.0.0.1:5000` en tu navegador.

## 📂 Estructura del Proyecto

```text
SERVICE_UNION_TEC/
├── app.py                # Lógica principal y rutas
├── requirements.txt      # Dependencias del proyecto
├── templates/            # Plantillas HTML (Login, Dashboard)
├── static/               # Archivos CSS y Assets
└── README.md             # Documentación
```

## 📄 Formato del Excel

Para que la carga funcione, el archivo Excel debe contener las siguientes columnas exactas en la primera fila:

| Columna | Descripción |
| :--- | :--- |
| `Nombre Alumno` | Nombre completo del estudiante |
| `No. de Control` | Matrícula única |
| `Carrera` | Programa educativo |
| `Nombre Proyecto` | Título del servicio social |

## 🤝 Contribución

1.  Haz un Fork del proyecto.
2.  Crea una rama para tu funcionalidad (`git checkout -b feature/NuevaFuncionalidad`).
3.  Haz Commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`).
4.  Haz Push a la rama (`git push origin feature/NuevaFuncionalidad`).
5.  Abre un Pull Request.

## 📝 Licencia

Este proyecto es de uso exclusivo para fines académicos y administrativos del Instituto Tecnológico de Ensenada.

Desarrollado por  **Jesús Martínez Carmona**.

```
```
