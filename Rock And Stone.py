# ***************************************************
# *                 Rock And Stone
# *
# *Site par Arthur Bouvier
# *
# *En l'honneur de Karl
# ***************************************************


from flask import *
import time
import datetime
from datetime import *
import sqlite3
app = Flask(__name__, template_folder='staticFiles', static_folder='staticFiles')



# ***************************************************
# *valeurs
# ***************************************************

date_référence=date.fromisoformat('2023-03-01')
now = datetime.now()
months = (now.year - date_référence.year) * 12 + (now.month - date_référence.month)



name_connected=''
password_connected=''
is_connected=False
épée=''
métal=''

prix_cuivre=str(10+0.5*months)
prix_fer=str(20+1*months)
prix_acier=str(30+2*months)

prix_dague_cuivre=str((50+2*months))
prix_épée_une_main_cuivre=str((75+3*months))
prix_épée_deux_mains_cuivre=str((100+5*months))

prix_dague_fer=str((75+4*months))
prix_épée_une_main_fer=str((125+8*months))
prix_épée_une_main_acier=str((200+12*months))

prix_dague_acier=str((100+5*months))
prix_épée_deux_mains_fer=str((200+10*months))
prix_épée_deux_mains_acier=str((300+15*months))

if months%12==0:
    prix_dague_cuivre=str((50+2*months)//1.2)
    prix_épée_une_main_cuivre=str((75+3*months)//1.2)
    prix_épée_deux_mains_cuivre=str((100+5*months)//1.2)

    prix_dague_fer=str((75+4*months)//1.2)
    prix_épée_une_main_fer=str((125+8*months)//1.2)
    prix_épée_une_main_acier=str((200+12*months)//1.2)

    prix_dague_acier=str((100+5*months)//1.2)
    prix_épée_deux_mains_fer=str((200+10*months)//1.2)
    prix_épée_deux_mains_acier=str((300+15*months)//1.2)
# ***************************************************
# *user database
# ***************************************************


conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
result = cursor.fetchone()
if result is not None:
    print("")
else:
    conn.execute('''CREATE TABLE IF NOT EXISTS users
                (name TEXT NOT NULL,
                password TEXT NOT NULL)''')
conn.execute("INSERT INTO users (NAME,password) \
          VALUES ('hope','hope' )");
cursor = conn.execute("SELECT name,password from users")
conn.close()



# ***************************************************
# *sword database
# ***************************************************

conn = sqlite3.connect('sword.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='forged'")
result = cursor.fetchone()
if result is not None:
    print("")
else:
    conn.execute('''CREATE TABLE IF NOT EXISTS forged
                (lenght TEXT NOT NULL,
                metal TEXT NOT NULL,
                price INT NOT NULL)''')

cursor.execute("DELETE FROM forged;")

conn.execute("INSERT INTO forged (lenght,metal,price) \
          VALUES ('dague','cuivre', "+prix_dague_cuivre+" )");
conn.execute("INSERT INTO forged (lenght,metal,price) \
          VALUES ('épée une main','cuivre', "+prix_épée_une_main_cuivre+" )");
conn.execute("INSERT INTO forged (lenght,metal,price) \
          VALUES ('épée deux mains','cuivre', "+prix_épée_deux_mains_cuivre+" )");

conn.execute("INSERT INTO forged (lenght,metal,price) \
          VALUES ('dague','fer', "+prix_dague_fer+" )");
conn.execute("INSERT INTO forged (lenght,metal,price) \
          VALUES ('épée une main','fer', "+prix_épée_une_main_fer+" )");
conn.execute("INSERT INTO forged (lenght,metal,price) \
          VALUES ('épée deux mains','fer', "+prix_épée_deux_mains_fer+" )");

conn.execute("INSERT INTO forged (lenght,metal,price) \
          VALUES ('dague','acier', "+prix_dague_acier+" )");
conn.execute("INSERT INTO forged (lenght,metal,price) \
          VALUES ('épée une main','acier', "+prix_épée_une_main_acier+" )");
conn.execute("INSERT INTO forged (lenght,metal,price) \
          VALUES ('épée deux mains','acier', "+prix_épée_deux_mains_acier+" )");
conn.commit()
conn.close()










# ***************************************************
# *acceuil
# ***************************************************

@app.route("/")
def main():
    global is_connected
    print(is_connected)
    if is_connected==True:
        return '''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/css_home.css' />
            <title>acceuil</title>
        </head>
        <body>
            <h1>Bienvenue cher client chez Rock And Stone !</h1>
            <p>Vagabondez dans notre sublime <a href="/cité">cité</a> ou laissez nous vous diriger directement où vous le souhaitez.</p>
        </body>
        </html>'''
    if is_connected==False:
        return '''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/css_home.css' />
            <title>Home</title>
        </head>
        <body>
            <h1><a href=" /connect "style="color: red;">Déclinez votre identité !</a></h1>
        </body>
        </html>'''

# ***************************************************
# *connection
# ***************************************************

@app.route("/connect")
def connect():
    return '''
    <html lang="fr">
    <head>
        <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
        <link rel="stylesheet" href='/staticFiles/connect.css' />
        <title>Connection</title>
    </head>
    <body>
        <h2>Pour décliner votre identité, entrez dans l'URL http://127.0.0.1:5000/sign_in/votre_nom/votre_mot_de_passe</h2>
        <h2>Pour devenir client de la forge, entrez dans l'URL http://127.0.0.1:5000/sign_up/votre_nom/votre_mot_de_passe</h2>
    </body>
    </html>'''

@app.route("/cité")
def cité():
    global is_connected
    if is_connected==True:
        return '''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/cité.css' />
            <title>Cité naine</title>
        </head>
        <body>
            <h1>Bienvenue dans la cité des nains</h1>
            <p>Se déplacer vers la <a href="/forge">forge</a> ?</p>
            <p>Retourner à l' <a href="/">entrée</a> ?</p>
        </body>
        </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''

# ***************************************************
# *forge
# ***************************************************

@app.route("/forge")
def forge():
    global is_connected
    if is_connected==True:
        return '''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/forge.css' />
            <title>Forge</title>
        </head>
        <body>
            
            <h1>Vous êtes dans la forge de la cité</h1>
            <p>Retourner dans la <a href=" /cité ">cité</a> ?</p>
            <p>Passer <a href=" /commande ">commande</a> ?</p>
        </body>
        </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''
    
# ***************************************************
# *commande
# ***************************************************

@app.route("/commande")
def commande():
    global is_connected
    if is_connected==True:
        return '''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/commande.css' />
            <title>Commande</title>
        </head>
        <body>
            <h1>Que souhaitez vous faire forger ?</h1>
            <p><a href=' /forge '>Retourner dans la forge</button></a></p>
            <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
            <p><a href=' /dague '>Voir les dagues</button></a></p>
            <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
            <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            <p>    Suite à une grosse quantité de commandes et un approvisionnement en métaux plus faible, les commandes se limiteront à 3 épées en cuivre, 2 épées en fer et une épée en acier maximum.</p>
        </body>
        </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''

# ***************************************************
# *dague
# ***************************************************

@app.route("/dague")
def dague():
    global is_connected
    conn = sqlite3.connect('sword.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM forged WHERE lenght='dague'")
    data = cursor.fetchmany(3)
    if is_connected==True:
        return render_template('dague.html', data=data)
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''

# ***************************************************
# *épée une main
# ***************************************************

@app.route("/épée_une_main")
def épée_une_main():
    global is_connected
    conn = sqlite3.connect('sword.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM forged WHERE lenght='épée une main'")
    data = cursor.fetchmany(3)
    if is_connected==True:
        return render_template('épée_une_main.html', data=data)
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''
    
# ***************************************************
# *épée deux mains
# ***************************************************

@app.route("/épée_deux_mains")
def épée_deux_mains():
    global is_connected
    conn = sqlite3.connect('sword.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM forged WHERE lenght='épée deux mains'")
    data = cursor.fetchmany(3)
    if is_connected==True:
        return render_template('épée_deux_mains.html', data=data)
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''

# ***************************************************
# *commande d'épées
# *************************************************** 

@app.route("/dague_cuivre")
def dague_cuivre():
    global is_connected
    global name_connected
    global password_connected
    global prix_dague_cuivre
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute ("SELECT COUNT(*) FROM "+name_connected+'_'+password_connected+'_commande'+" WHERE metal LIKE 'cuivre';")
        number=cursor.fetchone()[0]
        if number<3:
            conn.execute('''CREATE TABLE IF NOT EXISTS '''+name_connected+'_'+password_connected+'_commande''''
                        (lenght TEXT NOT NULL,
                        metal TEXT NOT NULL,
                        price INT NOT NULL)''')
            print("Table created successfully")
            conn.execute("INSERT INTO "+name_connected+'_'+password_connected+'_commande'+" (lenght,metal,price) \
                    VALUES ('dague','cuivre', "+prix_dague_cuivre+" )");
            conn.commit()
            
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez commandé une dague en cuivre.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
        else:
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez déjà atteint la limite en épée en cuivre.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''
    

@app.route("/épée_une_main_cuivre")
def épée_une_main_cuivre():
    global prix_épée_une_main_cuivre
    global is_connected
    global name_connected
    global password_connected
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute ("SELECT COUNT(*) FROM "+name_connected+'_'+password_connected+'_commande'+" WHERE metal LIKE 'cuivre';")
        number=cursor.fetchone()[0]
        if number<3:
            conn.execute('''CREATE TABLE IF NOT EXISTS '''+name_connected+'_'+password_connected+'_commande''''
                        (lenght TEXT NOT NULL,
                        metal TEXT NOT NULL,
                        price INT NOT NULL)''')
            print("Table created successfully")
            conn.execute("INSERT INTO "+name_connected+'_'+password_connected+'_commande'+" (lenght,metal,price) \
                    VALUES ('épée une main','cuivre', "+prix_épée_une_main_cuivre+" )");
            conn.commit()
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez commandé une épée une main en cuivre.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
        else:
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez déjà atteint la limite en épée en cuivre.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''
    

@app.route("/épée_deux_mains_cuivre")
def épée_deux_mains_cuivre():
    global prix_épée_deux_mains_cuivre
    global is_connected
    global name_connected
    global password_connected
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute ("SELECT COUNT(*) FROM "+name_connected+'_'+password_connected+'_commande'+" WHERE metal LIKE 'cuivre';")
        number=cursor.fetchone()[0]
        if number<3:
            conn.execute('''CREATE TABLE IF NOT EXISTS '''+name_connected+'_'+password_connected+'_commande''''
                        (lenght TEXT NOT NULL,
                        metal TEXT NOT NULL,
                        price INT NOT NULL)''')
            print("Table created successfully")
            conn.execute("INSERT INTO "+name_connected+'_'+password_connected+'_commande'+" (lenght,metal,price) \
                    VALUES ('épée deux mains','cuivre', "+prix_épée_deux_mains_cuivre+" )");
            conn.commit()
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>vous avez commandé une épée deux mains en cuivre.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
        else:
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez déjà atteint la limite en épée en cuivre.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''


@app.route("/dague_fer")
def dague_fer():
    global prix_dague_fer
    global is_connected
    global name_connected
    global password_connected
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute ("SELECT COUNT(*) FROM "+name_connected+'_'+password_connected+'_commande'+" WHERE metal LIKE 'fer';")
        number=cursor.fetchone()[0]
        if number<2:
            conn.execute('''CREATE TABLE IF NOT EXISTS '''+name_connected+'_'+password_connected+'_commande''''
                        (lenght TEXT NOT NULL,
                        metal TEXT NOT NULL,
                        price INT NOT NULL)''')
            print("Table created successfully")
            conn.execute("INSERT INTO "+name_connected+'_'+password_connected+'_commande'+" (lenght,metal,price) \
                    VALUES ('dague','fer', "+prix_dague_fer+" )");
            conn.commit()
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>vous avez commandé une dague en fer.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
        else:
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez déjà atteint la limite en épée en fer.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''
    

@app.route("/épée_une_main_fer")
def épée_une_main_fer():
    global prix_épée_une_main_fer
    global is_connected
    global name_connected
    global password_connected
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute ("SELECT COUNT(*) FROM "+name_connected+'_'+password_connected+'_commande'+" WHERE metal LIKE 'fer';")
        number=cursor.fetchone()[0]
        if number<2:
            conn.execute('''CREATE TABLE IF NOT EXISTS '''+name_connected+'_'+password_connected+'_commande''''
                        (lenght TEXT NOT NULL,
                        metal TEXT NOT NULL,
                        price INT NOT NULL)''')
            print("Table created successfully")
            conn.execute("INSERT INTO "+name_connected+'_'+password_connected+'_commande'+" (lenght,metal,price) \
                    VALUES ('épée une main','fer', "+prix_épée_une_main_fer+" )");
            conn.commit()
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>vous avez commandé une épée une main en fer.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
        else:
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez déjà atteint la limite en épée en fer.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''
    

@app.route("/épée_deux_mains_fer")
def épée_deux_mains_fer():
    global prix_épée_deux_mains_fer
    global is_connected
    global name_connected
    global password_connected
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute ("SELECT COUNT(*) FROM "+name_connected+'_'+password_connected+'_commande'+" WHERE metal LIKE 'fer';")
        number=cursor.fetchone()[0]
        if number<2:
            conn.execute('''CREATE TABLE IF NOT EXISTS '''+name_connected+'_'+password_connected+'_commande''''
                        (lenght TEXT NOT NULL,
                        metal TEXT NOT NULL,
                        price INT NOT NULL)''')
            print("Table created successfully")
            conn.execute("INSERT INTO "+name_connected+'_'+password_connected+'_commande'+" (lenght,metal,price) \
                    VALUES ('épée deux mains','fer', "+prix_épée_deux_mains_fer+" )");
            conn.commit()
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>vous avez commandé une épée deux mains en fer.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
        else:
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez déjà atteint la limite en épée en fer.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''


@app.route("/dague_acier")
def dague_acier():
    global prix_dague_acier
    global is_connected
    global name_connected
    global password_connected
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute ("SELECT COUNT(*) FROM "+name_connected+'_'+password_connected+'_commande'+" WHERE metal LIKE 'acier';")
        number=cursor.fetchone()[0]
        if number<1:
            conn.execute('''CREATE TABLE IF NOT EXISTS '''+name_connected+'_'+password_connected+'_commande''''
                        (lenght TEXT NOT NULL,
                        metal TEXT NOT NULL,
                        price INT NOT NULL)''')
            print("Table created successfully")
            conn.execute("INSERT INTO "+name_connected+'_'+password_connected+'_commande'+" (lenght,metal,price) \
                    VALUES ('dague','acier', "+prix_dague_acier+" )");
            conn.commit()
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>vous avez commandé une dague en acier.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
        else:
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez déjà atteint la limite en épée en acier.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''
    

@app.route("/épée_une_main_acier")
def épée_une_main_acier():
    global prix_épée_une_main_acier
    global is_connected
    global name_connected
    global password_connected
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute ("SELECT COUNT(*) FROM "+name_connected+'_'+password_connected+'_commande'+" WHERE metal LIKE 'acier';")
        number=cursor.fetchone()[0]
        if number<1:
            conn.execute('''CREATE TABLE IF NOT EXISTS '''+name_connected+'_'+password_connected+'_commande''''
                        (lenght TEXT NOT NULL,
                        metal TEXT NOT NULL,
                        price INT NOT NULL)''')
            print("Table created successfully")
            conn.execute("INSERT INTO "+name_connected+'_'+password_connected+'_commande'+" (lenght,metal,price) \
                    VALUES ('épée une main','acier', "+prix_épée_une_main_acier+" )");
            conn.commit()
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>vous avez commandé une épée une main en acier.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
        else:
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez déjà atteint la limite en épée en acier.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''
    

@app.route("/épée_deux_mains_acier")
def épée_deux_mains_acier():
    global prix_épée_deux_mains_acier
    global is_connected
    global name_connected
    global password_connected
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute ("SELECT COUNT(*) FROM "+name_connected+'_'+password_connected+'_commande'+" WHERE metal LIKE 'acier';")
        number=cursor.fetchone()[0]
        if number<1:
            conn.execute('''CREATE TABLE IF NOT EXISTS '''+name_connected+'_'+password_connected+'_commande''''
                        (lenght TEXT NOT NULL,
                        metal TEXT NOT NULL,
                        price INT NOT NULL)''')
            print("Table created successfully")
            conn.execute("INSERT INTO "+name_connected+'_'+password_connected+'_commande'+" (lenght,metal,price) \
                    VALUES ('épée deux mains','acier', "+prix_épée_deux_mains_acier+" )");
            conn.commit()
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>vous avez commandé une épée deux mains en acier.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
        else:
            conn.close()
            return '''
            <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
            
            <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/commande.css' />
                <title>Commande</title>
            </head>
            <body>
                <h1>Vous avez déjà atteint la limite en épée en acier.</h1>
                <p><a href=' /forge '>Retourner dans la forge</button></a></p>
                <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
                <p><a href=' /dague '>Voir les dagues</button></a></p>
                <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
                <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
            </body>
            </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
                <nav>
                <ul>
                    <li><a href="/">Acceuil</a></li>
                    <li>
                    <a href="">Ventes</a>
                    <ul>
                        <li><a href="/cuivre">cuivre</a></li>
                        <li><a href="/fer">fer</a></li>
                        <li><a href="/acier">acier</a></li>
                    </ul>
                    </li>
                    <li><a href="">à propos</a></li>
                </ul>
                </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''

# ***************************************************
# *mes commandes
# ***************************************************

@app.route("/mes_commandes")
def mes_commandes():
    global is_connected
    global name_connected
    global password_connected
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM "+name_connected+'_'+password_connected+'_commande'+"")
        data = cursor.fetchall()
        return render_template('mes_commandes.html', data=data)
    else :
        return'''
        <html lang="fr">
            <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
                <nav>
                <ul>
                    <li><a href="/">Acceuil</a></li>
                    <li>
                    <a href="">Ventes</a>
                    <ul>
                        <li><a href="/cuivre">cuivre</a></li>
                        <li><a href="/fer">fer</a></li>
                        <li><a href="/acier">acier</a></li>
                    </ul>
                    </li>
                    <li><a href="">à propos</a></li>
                </ul>
                </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''


# ***************************************************
# *connection
# ***************************************************

@app.route('/sign_in/<user>/<password_user>')
def sign_in(user,password_user):
    global is_connected
    global name_connected
    global password_connected
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    name = user
    password = password_user
    cursor.execute("SELECT * FROM users WHERE name=? AND password=?", (name, password))
    result = cursor.fetchone()
    if result:
        name_connected=name
        password_connected=password
        conn.close()
        is_connected=True
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        conn.execute('''CREATE TABLE IF NOT EXISTS '''+name_connected+'_'+password_connected+'_commande''''
                    (lenght TEXT NOT NULL,
                    metal TEXT NOT NULL,
                    price INT NOT NULL)''')
        conn.close()
        
        return'''
        <html lang="fr">
            <head>
                <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
                <link rel="stylesheet" href='/staticFiles/connect.css' />
                <title>Connection</title>
            </head>
            <body>
                <h1>Vous pouvez <a href="/">entrer</a> '''+str(name)+''' '''+str(password)+'''</h1>
            </body>
        </html>
        '''
    else:
        conn.close()
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1>Vous n'ètes pas enregistré dans le registre sous ce nom ou avec ce mot de passe. <a href="/connect">Recommencez !</a></h1>
        </body>
        </html>
        '''
    
# ***************************************************
# *création nouveau client
# ***************************************************

@app.route('/sign_up/<user>/<password_user>')
def sign_up(user,password_user):
    global is_connected
    global name_connected
    global password_connected
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    name = user
    password = password_user
    cursor.execute("SELECT * FROM users WHERE name=? AND password=?", (name, password))
    result = cursor.fetchone()
    if result:
        conn.close()
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1>Cette personne existe déjà. <a href="/connect">Recommencez !</a></h1>
        </body>
        </html>
        '''
    else:
        conn = sqlite3.connect('user_database.db')
        conn.execute("INSERT INTO users (NAME,password) \
            VALUES (?,?)", (name, password));
        conn.commit()
        conn.close()
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1>Très bien '''+str(name)+''' '''+str(password)+''' il ne vous reste plus qu'à vous <a href="/connect">présenter</a></h1>
        </body>
        </html>
        '''
        
# ***************************************************
# *histoire
# ***************************************************

@app.route('/notre_histoire')
def notre_histoire():
    return '''
    <html lang="fr">
        <head>
        <title>Histoire</title>
        <link rel="stylesheet" href='/staticFiles/histoire.css' />
        <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <h1>L'histoire de Rock And Stone</h1>
        </head>
        <body>
            <p class="my-text">La forge Rock And Stone est une entreprise familiale héritée de nos ancêtres. Nous sommes les descendants d'une grande ligné de forgerons nains et nous avons amélioré nos techniques et notre forge au fil des générations de forgerons.</p>
            <p class="my-text">Notre ancêtre fondateur, Karl, a mis toute sa vie dans ce projet. Il n'a malheureusement pas eu l'opportunité de voir son entreprise grandir et devenir aussi populaire et signe de qualité. Karl a disparu lors de sa dernière expédition pour trouver un nouveau minerai capable de bouleverser le monde de la forge.</p>
            <p class="my-text">Aujourd'hui encore nous poursuivons le rêve de nos ancêtres et le transmettrons à notre descendance pour qu'elle puisse peut-être enfin trouver ce minerai qui nous obsède tant.</p>
            <p class="my-text">Nous sommes fiers de qui nous sommes et ferons de Rock And Stone la forge la plus imposante du monde. Pour Karl ! </p>
            <img src="/staticFiles/images/Rock_And_Stone.png" alt="image">
        </body>
    </html>'''


# ***************************************************
# *métal
# ***************************************************

@app.route('/métal')
def métal():
    global prix_cuivre
    global prix_fer
    global prix_acier
    return '''<html lang="fr">
        <head>
        <title>Métal</title>
        <link rel="stylesheet" href='/staticFiles/métal.css' />
        <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <h1>Voici les métaux que nous utilisons pour fabriquer nos épées.</h1>
        </head>
        <body>
            <div class="container">
                <img src="/staticFiles/images/cuivre.png" alt="image">
                <p>prix du lingot : '''+str(prix_cuivre)+'''</p>
                <p>Le cuivre est le métal le plus abordable que nous utilisons. Les épées en cuivre sont donc moins chères, mais beaucoup moins efficaces. </p>
            </div>
            <div class="container">
                <img src="/staticFiles/images/fer.png" alt="image">
                <p>prix du lingot : '''+str(prix_fer)+'''</p>
                <p>Le fer est le métal le plus commun au champ de bataille. Il est solide et tranchant, mais il est plus coûteux.
                </p>
            </div>
            <div class="container">
                <img src="/staticFiles/images/acier.png" alt="image">
                <p>prix du lingot : '''+str(prix_acier)+'''</p>
                <p>L'acier est le métal haut de gamme dans la forge. Une épée en acier sera la plus robuste, mais elle restera la plus chère. </p>
            </div>
        </body>
    </html>'''

# ***************************************************
# *suppression des commandes personelles
# ***************************************************
    
@app.route("/sup")
def sup():
    global is_connected
    global name_connected
    global password_connected
    if is_connected==True:
        conn = sqlite3.connect(name_connected+'_'+password_connected+'.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM "+str(name_connected)+'_'+str(password_connected)+'_commande'+";")
        conn.commit()
        conn.close()
        return '''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <link rel="stylesheet" href='/staticFiles/commande.css' />
            <title>Commande</title>
        </head>
        <body>
            <h1>Vous avez supprimé toutes vos commandes.</h1>
            <p><a href=' /forge '>Retourner dans la forge</button></a></p>
            <p><a href=' /mes_commandes '>Voir ses commandes</button></a></p>
            <p><a href=' /dague '>Voir les dagues</button></a></p>
            <p><a href=' /épée_une_main '>Voir les épées une main</button></a></p>
            <p><a href=' /épée_deux_mains '>Voir les épées deux mains</button></a></p>
        </body>
        </html>'''
    else :
        return'''
        <html lang="fr">
        <head>
            <link rel="stylesheet" href="/staticFiles/menu.css">
                <nav>
                <ul>
                    <li><a href="/">Acceuil</a></li>
                    <li>
                    <a href="">Ventes</a>
                    <ul>
                        <li><a href="/cuivre">cuivre</a></li>
                        <li><a href="/fer">fer</a></li>
                        <li><a href="/acier">acier</a></li>
                    </ul>
                    </li>
                    <li><a href="">à propos</a></li>
                </ul>
                </nav>
            <link rel="stylesheet" href='/staticFiles/connect.css' />
            <title>Connection</title>
        </head>
        <body>
            <h1><a href="/connect">Identifiez vous!</a></h1>
        </body>
        </html>
        '''


@app.route('/contact')
def contact():
    return '''
    <html lang="fr">
        <head>
        <title>contact</title>
        <link rel="stylesheet" href='/staticFiles/histoire.css' />
        <link rel="stylesheet" href="/staticFiles/menu.css">
        
        <nav>
        <ul>
            <li><a href="/">Acceuil</a></li>
            <li>
                <a href="">Ventes</a>
            <ul>
                <li><a href="/dague">dague</a></li>
                <li><a href="/épée_une_main">épée une main</a></li>
                <li><a href="/épée_deux_mains">épée deux mains</a></li>
            </ul>
            </li>
            <li><a href="">à propos</a>
            <ul>
                <li><a href="/notre_histoire">notre histoire</a></li>
                <li><a href="/métal">nos métaux</a></li>
                <li><a href="/contact">nous contacter</a></li>
            </ul>
            </li>
            <li><a href="/mes_commandes">Mon panier</a></li>
        </ul>
        </nav>
            <h1>Comment nous contacter ?</h1>
        </head>
        <body>
            <p class="my-text">Email : for_Karl@Rock_And_Stone.com </p>
            <p class="my-text">Téléphone : nous n'en avons pas </p>
            <img src="/staticFiles/images/Rock_And_Stone.png" alt="image">
        </body>
    </html>'''



if __name__ == "__main__":
    app.run(debug=True)

