#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Project name : Backup_git.py
Authors(s) : dossantosjdf@gmail.com
Python version : 3.9

Version : 0
Description :
Ce programme va permettre de cloner
tous les depots publiques sur GitHub.

Limits :
Ce script fonctionne seulement dans un environnement Linux.
Le clone de depots privé ou les wiki ne sont pas intégrés.
"""

# -------------------------------------
#  Imports
# -------------------------------------
import requests

import subprocess

# -------------------------------------
#  Global variables
# -------------------------------------
REPO_URL = 'https://api.github.com/users/DOSSANTOSDaniel/repos'

# -------------------------------------
#  Functions
# -------------------------------------


# -------------------------------------
#  Main
# -------------------------------------

list_repos = []

print("Début du script !")

req_jison = requests.api.get(REPO_URL)
for repo in req_jison.json():
    list_repos.append("git@github.com:"+repo['full_name']+".git")

if subprocess.run('command -v git > /dev/null', shell=True, check=True):
    git_dir_bak = "/home/daniel/git_backup/"
    subprocess.run(["mkdir", f"{git_dir_bak}"], capture_output=True)

    for rep in list_repos:
        subprocess.run(["git", "-C", f"{git_dir_bak}", "clone", f"{rep}"], capture_output=True)
        print(f"Clone de {rep} terminé !")
else:
    print("Git, n'est pas installé sur votre ordinateur : \n")
    print("Installation de git sur Debian/Ubuntu : # apt-get install git ")
    print("Installation de git sur CentOS/Fedora : # dnf install git ")

print("Fin du Script")
