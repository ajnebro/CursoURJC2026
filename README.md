
# Optimización Multiobjetivo con Algoritmos Evolutivos: Fundamentos y Aspectos Prácticos

## Escuela de Verano Universidad Rey Juan Carlos. Aranjuez. 1 julio 2026

### Herramientas software
* Java JDK 21+
* Python 3.11+ (Anaconda Python)
* Entorno de desarrollo Java (IntelliJ Idea, Eclipse, Visual Studio Code)
* Recomendado: agente de IAG (ChatGPT, Claude, Codex, etc.)

### Paquetes software
* jMetal (https://github.com/jMetal/jMetal)

``` bash
git clone https://github.com/jMetal/jMetal
```

* Evolver (https://github.com/jMetal/Evolver)

``` bash
git clone https://github.com/jMetal/Evolver
```

* Entorno virtual Python

Requisitos: [requirements.txt](requirements.txt)

Crear y activar el entorno virtual antes de instalar:

**macOS / Linux:**

```bash
# venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# conda
conda create -n evolver python=3.11
conda activate evolver
pip install -r requirements.txt
```

**Windows (PowerShell):**

```powershell
# venv
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# conda
conda create -n evolver python=3.11
conda activate evolver
pip install -r requirements.txt
```

> Si PowerShell bloquea la ejecución de scripts, ejecutar primero:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### Verificación del entorno

Tras la instalación, ejecuta el siguiente script para comprobar que todo está correctamente configurado:

```bash
python check_env.py
```

El script verifica las versiones de Java y Python y la disponibilidad de los paquetes necesarios.