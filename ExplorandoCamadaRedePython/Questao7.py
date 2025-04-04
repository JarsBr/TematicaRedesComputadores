import subprocess
import platform

def obter_tabela_roteamento():
    so = platform.system()
    
    if so == "Windows":
        comando = ["route", "print"]
    else:
        comando = ["netstat", "-rn"]
    
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print(resultado.stdout)

obter_tabela_roteamento()
