# Project Sistema de consorcio backend

# cd sistema-consorcio-backend

# py -m venv venv

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass (en caso de que no deje ejecutar el activate)

# para windows (./venv/Scripts/activate) para linux source /venv/bin/activate

#  pip freeze > requirements.txt (utilizar cuando se instalen nuevos packages)

# pip install -r requirements.txt


# Sistema de Consorcio Backend

Este proyecto es el backend del sistema de consorcio. A continuación, se detallan los pasos necesarios para configurar el entorno de desarrollo en Windows y Linux.

## Requisitos Previos

- Python instalado en tu sistema.
- Acceso a la terminal de comandos (CMD, PowerShell en Windows o Bash en Linux).

## Pasos para Configurar el Entorno

### 1. Clonar el Repositorio

Clona el repositorio en tu máquina local con el siguiente comando:

```bash
git clone https://github.com/augustomachuca1991/sistema-consorcio-backend.git
```

### 2. Accede a directorio

Después de clonar el repositorio, navega al directorio del proyecto con

```bash
cd sistema-consorcio-backend
```

### 3. Crear un Entorno Virtual

Para aislar las dependencias del proyecto, es recomendable crear un entorno virtual.

- **Windows**

```bash
py -m venv venv
```

- En caso de que no se permita la ejecución del script activate, puedes cambiar la política de ejecución de PowerShell temporalmente con:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

- **Linux**

```bash
python3 -m venv venv
```

### 4. Activar el Entorno Virtual

Activa el entorno virtual para que Python use las dependencias correctas del proyecto.

- **Windows**

```bash
./venv/Scripts/activate
```
- **Linux**

```bash
source venv/bin/activate
```

### 5. Instalar Dependencias

Instala todas las dependencias necesarias usando el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

### 6. Actualizar el Archivo requirements.txt

Cada vez que instales nuevos paquetes, asegúrate de actualizar el archivo requirements.txt para que las dependencias estén actualizadas:

```bash
pip freeze > requirements.txt
```


- **Notas Adicionales**
  - Activación del entorno virtual: Recuerda activar el entorno virtual cada vez que trabajes en el proyecto para que se carguen las dependencias correctamente.
  - Solución de problemas en Windows: Si tienes problemas con la activación del entorno virtual, verifica que la política de ejecución de scripts esté configurada correctamente (consulta el paso 3 para más detalles).
