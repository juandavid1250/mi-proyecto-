# IUTEDE - Gestión de Tics

## Configuración de Base de Datos

Antes de ejecutar la aplicación, configura el archivo `.env` con tus credenciales de MySQL:

```env
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=iutede_db
```

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

## Detener el servidor

- Presiona `CTRL+C` en la terminal donde corre la aplicación
- O en VS Code, presiona el botón de detener en la barra de depuración

## Dependencias Instaladas

- fastapi 0.136.1
- uvicorn 0.47.0
- PyMySQL 1.2.0
- python-dotenv 1.2.2
- SQLAlchemy 2.0.49
- pydantic 2.13.4
