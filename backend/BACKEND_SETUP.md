# Backend de Autenticación con Flask

Un backend simple y funcional para login y registro de usuarios usando Flask.

## 📁 Estructura del Proyecto

```
├── app.py              # Aplicación Flask con los endpoints
├── models.py           # Modelo de Usuario
├── test.py            # Pruebas unitarias
├── requirements.txt   # Dependencias
└── users.db           # Base de datos SQLite (se crea automáticamente)
```

## 🛠️ Instalación

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## 📋 Endpoints

### 1. Registrar Usuario
**POST** `/api/register`

**Body:**
```json
{
  "username": "diego",
  "email": "diego@example.com",
  "password": "password123"
}
```

**Respuesta (201):**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "diego",
    "email": "diego@example.com"
  }
}
```

---

### 2. Login (con username)
**POST** `/api/login`

**Body:**
```json
{
  "username": "diego",
  "password": "password123"
}
```

**Respuesta (200):**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "diego",
    "email": "diego@example.com"
  }
}
```

---

### 3. Login (con email)
**POST** `/api/login`

**Body:**
```json
{
  "email": "diego@example.com",
  "password": "password123"
}
```

**Respuesta (200):** (igual que con username)

---

### 4. Obtener Usuario
**GET** `/api/users/{id}`

**Respuesta (200):**
```json
{
  "id": 1,
  "username": "diego",
  "email": "diego@example.com"
}
```

---

### 5. Health Check
**GET** `/health`

**Respuesta (200):**
```json
{
  "status": "ok"
}
```

## ✅ Pruebas Unitarias

Ejecutar todas las pruebas:
```bash
python -m pytest test.py -v
```

O con unittest:
```bash
python -m unittest test.py -v
```

### Tipos de Pruebas Incluidas

**Registro:**
- ✓ Registro exitoso
- ✓ Campos faltantes
- ✓ Contraseña muy corta
- ✓ Username duplicado
- ✓ Email duplicado
- ✓ Sin datos

**Login:**
- ✓ Login exitoso con username
- ✓ Login exitoso con email
- ✓ Contraseña incorrecta
- ✓ Usuario no existe
- ✓ Contraseña faltante
- ✓ Sin credenciales
- ✓ Sin datos

**Usuario:**
- ✓ Obtener usuario por ID
- ✓ Usuario no encontrado

**Health:**
- ✓ Health check endpoint

## 🔒 Características Seguridad

- ✅ Contraseñas encriptadas con Werkzeug
- ✅ Validación de campos requeridos
- ✅ Validación de longitud de contraseña (mínimo 6 caracteres)
- ✅ Prevención de duplicados (username y email)
- ✅ Códigos HTTP apropiados (201, 400, 401, 409, 404)

## 📝 Ejemplo con cURL

### Registrar:
```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"diego","email":"diego@example.com","password":"password123"}'
```

### Login:
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"diego","password":"password123"}'
```

### Obtener usuario:
```bash
curl http://localhost:5000/api/users/1
```

## 🚀 Mejoras Futuras

- [ ] JWT tokens para mantener sesiones
- [ ] Validación de email (enviar código de confirmación)
- [ ] Reset de contraseña
- [ ] Rate limiting
- [ ] Logging
- [ ] Docker support
