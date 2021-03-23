# Détection du système d'exploitation et vérification des droits de l’utilisateur courant

```python
# Importations
import os
import platform
import ctypes

# Fonctions
def super_win():
    win_user = ctypes.windll.shell32.IsUserAnAdmin()
    if win_user != 1:
        print("Merci d’exécuter le script avec les droits administrateur")
        exit(1)

def super_lin():
    lin_user = os.getuid()
    if lin_user != 0:
        print("Merci d’exécuter le script avec les droits root")
        exit(1)

# main
# Quel est l'OS ?
sys_os = platform.system()
if sys_os == 'Linux':
    print("OS : Linux")
    super_lin()
elif sys_os == 'Windows':
    print("OS : Windows")
    super_win()
else:
    print("OS non prit en charge !")
    exit(1)
```
