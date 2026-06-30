
# Optimización Multiobjetivo con Algoritmos Evolutivos: Fundamentos y Aspectos Prácticos

## Escuela de Verano Universidad Rey Juan Carlos. Aranjuez. 1 julio 2026

### Material de apoyo

* [Sesión 1: Introducción a la optimización multiobjetivo con algoritmos evolutivos](transparencias/Escuela%20de%20Verano-URJC-2026.Sesion%201.pdf)
* [Sesión 2: Algoritmos representativos y comparación de rendimiento](transparencias/Escuela%20de%20Verano-URJC-2026.Sesion%202.pdf)
* [Taller 1: Optimización Multi-Objectivo con jMetal](transparencias/Escuela%20de%20Verano-URJC-2026.Taller%201.pdf)
* [Taller 2: Configuración automática de algoritmos y uso de Inteligencia Artificial Generativa](transparencias/Escuela%20de%20Verano-URJC-2026.Taller%202.pdf)

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

### Referencias

#### Algoritmos clásicos

* **PAES** — Knowles, J.D., Corne, D.W. (1999). The Pareto archived evolution strategy: a new baseline algorithm for Pareto multiobjective optimisation. *Proceedings of the 1999 Congress on Evolutionary Computation (CEC 1999)*, vol. 1, pp. 98–105. IEEE. https://doi.org/10.1109/CEC.1999.781913

* **NSGA-II** — Deb, K., Pratap, A., Agarwal, S., Meyarivan, T. (2002). A fast and elitist multiobjective genetic algorithm: NSGA-II. *IEEE Transactions on Evolutionary Computation*, 6(2), 182–197. https://doi.org/10.1109/4235.996017

* **SMS-EMOA** — Beume, N., Naujoks, B., Emmerich, M. (2007). SMS-EMOA: Multiobjective selection based on dominated hypervolume. *European Journal of Operational Research*, 181(3), 1653–1669. https://doi.org/10.1016/j.ejor.2006.08.008

* **MOEA/D** — Zhang, Q., Li, H. (2007). MOEA/D: A multiobjective evolutionary algorithm based on decomposition. *IEEE Transactions on Evolutionary Computation*, 11(6), 712–731. https://doi.org/10.1109/TEVC.2007.892759

#### Frameworks

* **jMetal** — Durillo, J.J., Nebro, A.J. (2011). jMetal: A Java framework for multi-objective optimization. *Advances in Engineering Software*, 42(10), 760–771. https://doi.org/10.1016/j.advengsoft.2011.05.014

* **jMetal 5** — Nebro, A.J., Durillo, J.J., Vergne, M. (2015). Redesigning the jMetal multi-objective optimization framework. *Proceedings of the Companion Publication of the 2015 Annual Conference on Genetic and Evolutionary Computation (GECCO Companion '15)*, pp. 1093–1100. ACM. https://doi.org/10.1145/2739482.2768462

* **Evolver** — Aldana-Martín, J.F., Durillo, J.J., Nebro, A.J. (2023). Evolver: Meta-optimizing multi-objective metaheuristics. *SoftwareX*, 24, 101551. https://doi.org/10.1016/j.softx.2023.101551

