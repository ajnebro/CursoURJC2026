
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

```bash
# venv
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# conda
conda create -n evolver python=3.11
conda activate evolver
pip install -r requirements.txt
```