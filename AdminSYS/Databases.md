# Administration de bases de données PostgreSQL
## Besoin
Installation de psycopg2-binary :
```bash
pip3 install psycopg2-binary
```

Connexion à la base de donnée et création d'une table :
```python
import psycopg2

#Information de connexion
host = "192.168.0.29"
dbname = "basetoto"
user = "toto"
password = "digital"
#sslmode = "require"

#construction de la connexion
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)
print("Connexion établie")

cursor = conn.cursor()

#créer un cursor
cur = conn.cursor()

#requête SQL
#création de la table élèves
req = "create table eleves (nom varchar(20), age int)"
insert into eleves (nom, age) values ('daniel', '32');
#exécuter la requête
cur.execute(req)

#envoyer la requête
conn.commit()

#fermer la connexion
conn.close
```

Affichage d'un retour de requête :
```python
import psycopg2

#Information de connexion
host = "192.168.0.29"
dbname = "basetoto"
user = "toto"
password = "digital"
#sslmode = "require"

#construction de la connexion
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)
print("Connexion établie")

cursor = conn.cursor()

#créer un cursor
cur = conn.cursor()

#la requête
#affichage des éléments de la table eleves
req = "select * from eleves"

#exécuter la requête
cur.execute(req)

#Affichage des données
res = cur.fetchall()

for row in res:
    print("nom : ",row[0])
    print("age : ",row[1])

#envoyer la requête
conn.commit()

#fermer la connexion
conn.close
```

Résultat :
```python
Connexion établie
nom :  daniel
age :  32
>>> 
```