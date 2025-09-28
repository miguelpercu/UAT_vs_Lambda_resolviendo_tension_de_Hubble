# check_uat_dependencies.py
"""
VERIFICADOR DE DEPENDENCIAS UAT
Ejecute este script para verificar si tiene todas las dependencias necesarias
para replicar los estudios del Unified Applicable Time Framework
"""

import sys
import importlib

def check_dependency(package_name, import_name=None, min_version=None):
    """Verifica una dependencia específica"""
    if import_name is None:
        import_name = package_name
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', '✓')
        
        if min_version and version != '✓':
            # Conversión básica de versiones
            current_ver = tuple(map(int, version.split('.')[:3]))
            min_ver = tuple(map(int, min_version.split('.')[:3]))
            
            if current_ver >= min_ver:
                status = f"✓ {version} (>= {min_version})"
            else:
                status = f"⚠ {version} (se recomienda {min_version}+)"
        else:
            status = f"✓ {version}" if version != '✓' else "✓"
            
        print(f"  {package_name:15} {status}")
        return True
        
    except ImportError:
        print(f"  {package_name:15} ✗ NO INSTALADO")
        return False

def main():
    print("🔍 VERIFICACIÓN DE DEPENDENCIAS - MARCO UAT")
    print("=" * 50)
    
    # Información del sistema
    print(f"Python: {sys.version}")
    print()
    
    # Dependencias requeridas (basado en análisis de código UAT)
    print("DEPENDENCIAS REQUERIDAS:")
    print("-" * 30)
    
    required_deps = [
        ("numpy", "numpy", "1.19.0"),
        ("pandas", "pandas", "1.3.0"), 
        ("matplotlib", "matplotlib", "3.3.0"),
        ("scipy", "scipy", "1.6.0"),
    ]
    
    all_required_ok = True
    for package, import_name, min_ver in required_deps:
        if not check_dependency(package, import_name, min_ver):
            all_required_ok = False
    
    # Dependencias opcionales
    print("\nDEPENDENCIAS OPCIONALES:")
    print("-" * 30)
    
    optional_deps = [
        ("seaborn", "seaborn", "0.11.0"),
        ("astropy", "astropy", "4.3.0"),
        ("corner", "corner", "2.2.0"),
    ]
    
    for package, import_name, min_ver in optional_deps:
        check_dependency(package, import_name, min_ver)
    
    # Comandos de instalación
    print("\n📦 COMANDOS DE INSTALACIÓN:")
    print("-" * 30)
    
    print("Si faltan dependencias, ejecute:")
    print()
    print("Con pip:")
    print("  pip install numpy pandas matplotlib scipy seaborn astropy corner")
    print()
    print("Con conda:")
    print("  conda install numpy pandas matplotlib scipy seaborn astropy corner -c conda-forge")
    
    # Verificación final
    print("\n" + "=" * 50)
    if all_required_ok:
        print("🎉 ¡TODAS LAS DEPENDENCIAS REQUERIDAS ESTÁN INSTALADAS!")
        print("Puede replicar los estudios UAT sin problemas")
    else:
        print("⚠️  FALTAN ALGUNAS DEPENDENCIAS REQUERIDAS")
        print("Ejecute los comandos de instalación mostrados arriba")
    
    print("\n📚 REPOSITORIOS UAT:")
    print("- Primer estudio: https://github.com/miguelpercu/uat_explicacion_con_datos_reales")
    print("- Último estudio:  https://github.com/miguelpercu/UAT_vs_Lambda_resolviendo_tension_de_Hubble")

if __name__ == "__main__":
    main()
