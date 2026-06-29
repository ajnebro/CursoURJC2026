"""
Verificación del entorno para el curso de Optimización Multiobjetivo.
Ejecutar con: python check_env.py
"""

import sys
import subprocess
import importlib

MIN_PYTHON = (3, 11)
MIN_JAVA = 21

REQUIRED_PACKAGES = [
    ("pandas", "1.5.0"),
    ("numpy", "1.21.0"),
    ("scipy", "1.9.0"),
    ("sklearn", "1.8.0"),
    ("matplotlib", "3.5.0"),
    ("seaborn", "0.11.0"),
    ("yaml", "6.0"),
    ("plotly", "5.0.0"),
    ("tqdm", "4.64.0"),
]

OK = "\033[92m OK\033[0m"
FAIL = "\033[91m FALLO\033[0m"


def check_python():
    ver = sys.version_info[:2]
    status = OK if ver >= MIN_PYTHON else FAIL
    print(f"Python {sys.version.split()[0]}{status}  (mínimo {MIN_PYTHON[0]}.{MIN_PYTHON[1]})")
    return ver >= MIN_PYTHON


def check_java():
    try:
        result = subprocess.run(
            ["java", "-version"],
            capture_output=True, text=True
        )
        output = result.stderr or result.stdout
        # "java version "21.0.1"" o 'openjdk version "21"'
        import re
        match = re.search(r'"(\d+)', output)
        if match:
            major = int(match.group(1))
            status = OK if major >= MIN_JAVA else FAIL
            print(f"Java {major}{status}  (mínimo {MIN_JAVA})")
            return major >= MIN_JAVA
        print(f"Java (versión no reconocida){FAIL}")
        return False
    except FileNotFoundError:
        print(f"Java no encontrado{FAIL}")
        return False


def check_packages():
    all_ok = True
    for module, min_ver in REQUIRED_PACKAGES:
        display = "scikit-learn" if module == "sklearn" else ("PyYAML" if module == "yaml" else module)
        try:
            mod = importlib.import_module(module)
            ver = getattr(mod, "__version__", "?")
            print(f"  {display} {ver}{OK}")
        except ImportError:
            print(f"  {display}{FAIL}")
            all_ok = False
    return all_ok


def main():
    print("=" * 50)
    print("Verificación del entorno")
    print("=" * 50)

    results = []
    results.append(check_python())
    results.append(check_java())

    print("\nPaquetes Python:")
    results.append(check_packages())

    print("=" * 50)
    if all(results):
        print("Entorno listo para el curso.")
    else:
        print("Hay elementos pendientes. Revisa los errores anteriores.")
    print("=" * 50)


if __name__ == "__main__":
    main()
