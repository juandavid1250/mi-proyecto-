# IUTEDE - Gestión de Tics

## Configuración de Base de Datos

### Desarrollo Local
Configura el archivo `.env` con tu conexión a PostgreSQL:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/iutede_db
```

### Producción (Render)
Render proporcionará automáticamente la variable `DATABASE_URL`. No necesitas configurarla manualmente.

## Ejecutar la aplicación localmente

### Opción 1: Desde PowerShell (Recomendado)

1. Abrir PowerShell en la carpeta del proyecto: `c:\proyecto modelado`
2. Activar el entorno virtual:
```powershell
.\.venv\Scripts\Activate.ps1
```

3. Ejecutar el servidor:
```powershell
python -m uvicorn main:app --reload
```

### Opción 2: Desde Visual Studio Code

1. Presiona `F5` o ve a Run and Debug
2. Selecciona "Python: FastAPI Uvicorn"
3. La aplicación se iniciará automáticamente

### Opción 3: Desde CMD

```cmd
.venv\Scripts\python.exe -m uvicorn main:app --reload
```

## Inicializar la Base de Datos

Antes de ejecutar la aplicación por primera vez, inicializa las tablas:

```powershell
python init_db.py
```

## Acceder a la API

Una vez iniciado el servidor, accede a:

- **API Principal**: http://127.0.0.1:8000
- **Documentación Swagger UI**: http://127.0.0.1:8000/docs (Recomendado para probar)
- **Documentación ReDoc**: http://127.0.0.1:8000/redoc
- **Health Check**: http://127.0.0.1:8000/health

## Endpoints Disponibles

### Roles
- `GET /api/v1/roles/` - Listar todos los roles
- `GET /api/v1/roles/{id_rol}` - Obtener un rol por ID
- `POST /api/v1/roles/` - Crear un nuevo rol
- `DELETE /api/v1/roles/{id_rol}` - Eliminar un rol

### Usuarios
- `GET /api/v1/usuarios/` - Listar todos los usuarios
- `GET /api/v1/usuarios/{id_usuario}` - Obtener un usuario por ID
- `POST /api/v1/usuarios/` - Crear un nuevo usuario
- `DELETE /api/v1/usuarios/{id_usuario}` - Eliminar un usuario
- `PUT /api/v1/usuarios/{id_usuario}` - Actualizar un usuario

### Auth
- `POST /api/v1/auth/login` - Autenticar usuario

## Despliegue en Render

### Pasos para desplegar:

1. **Crear cuenta en Render**: https://render.com

2. **Crear nuevo Web Service**:
   - Conecta tu repositorio de GitHub
   - Render detectará automáticamente que es una aplicación Python

3. **Configurar el Web Service**:
   - **Nombre**: iutede-backend
   - **Región**: Selecciona la más cercana a tus usuarios
   - **Branch**: main
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python init_db.py`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

4. **Configurar Base de Datos PostgreSQL**:
   - Crea un nuevo PostgreSQL Database en Render
   - Render proporcionará la variable `DATABASE_URL` automáticamente
   - Asegúrate de que el Web Service tenga acceso a la base de datos

5. **Variables de Entorno**:
   - Render proporcionará `DATABASE_URL` automáticamente desde la base de datos PostgreSQL
   - No necesitas configurar variables adicionales

6. **Desplegar**:
   - Haz clic en "Create Web Service"
   - Render construirá y desplegará tu aplicación
   - Espera a que el estado sea "Live"

7. **Acceder a la aplicación**:
   - Render proporcionará una URL pública
   - La documentación estará disponible en: `https://tu-url.render.com/docs`

## Detener el servidor

- Presiona `CTRL+C` en la terminal donde corre la aplicación
- O en VS Code, presiona el botón de detener en la barra de depuración

## Dependencias

- fastapi==0.136.1
- uvicorn==0.47.0
- sqlalchemy==2.0.49
- pydantic==2.13.4
- python-dotenv==1.2.2
- psycopg2-binary==2.9.9
