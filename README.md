# IUTEDE - Gestión de Tics

## Ejecutar la aplicación localmente

1. Abrir terminal en `c:\proyecto modelado`
2. Ejecutar el servidor con el entorno virtual:

```bat
run_local.bat
```

3. Acceder a la API en:

- http://127.0.0.1:8000
- Documentación OpenAPI: http://127.0.0.1:8000/docs
- Verificar servidor activo: http://127.0.0.1:8000/

## Alternativa usando Python directamente

```bat
".venv\Scripts\python.exe" main.py
```

## Ruta de login

- `POST /api/v1/auth/login`

Body ejemplo:

```json
{
  "nombre_usuario": "aser",
  "contrasena": "tu_contrasena"
}
```

Si el usuario existe y su nombre es `aser`, el campo `autorizado` devolverá `true`.

## Detener el servidor

- Presionar `CTRL+C` en la terminal donde corre la aplicación.
