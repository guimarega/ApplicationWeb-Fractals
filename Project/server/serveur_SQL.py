#------------------------------------------------------------
#	MODULO - SERVEUR SQL
#	Le but: Ce module a une classe BD lequel a le but 
#	de creer et gerer les images de l'ensemble de
#	julia dans une base de donnes SQLite
#
#	Methodes: La classe contient les methodes:
#		- __init__
#		- initialisation
#		- Ajouter_image
#		- is_in
#
#	Variavle:# conn
#		 # c
#------------------------------------------------------------

import ctypes
import sqlite3
import webbrowser
import http.server
import socketserver
from PIL import Image
from urllib.parse import urlparse, parse_qs

class BD:
	def __init__(self):
	# Creation de la connection avec le fichier .sqlite et du cursor
		self.__conn = sqlite3.connect('Julia.sqlite')
		self.__c = self.__conn.cursor()
	
	def initialisation(self):
	# Initialisation de la table de donnes
		print("Initialisation - SQLite")
		#On crée la table si elle n'existe pas encore.
		self.__c.execute("DROP TABLE IF EXISTS images_julia")
		self.__c.execute("""CREATE TABLE images_julia (Nom TEXT, Couleur INTEGER, taille1 REAL, taille2 REAL,\
             	Imaginaire REAL, Reel REAL, Zoom INTEGER, iterations INTEGER)""")
		self.__conn.commit()       ## nom_image de la forme: "taille1;taille2;Imaginaire;Reel;Zoom;interations;Couleur"
		return None

	#Fonction pour ajouter les paramètres d'une fractale dans la base de données après lui avoir donné un nom
	def Ajouter_image(self,nom,couleur,taille1,taille2,imaginaire,reel,zoom,iterations):
		image= (nom,couleur,taille1,taille2,imaginaire,reel,zoom,iterations)
		self.__c.execute('INSERT INTO images_julia VALUES (?, ?, ?, ?, ?, ?, ?, ?)',image)
		self.__conn.commit()
		return True

	#Fonction qui permet de recercher si une fractale est déjà présente dans la base de données : 
	#Si elle est présente, on renverra son nom. Si elle n'est pas présente, on va la génerer puis l'ajouter
	#avec la fonction Ajouter_image à notre base de données, puis on renverra son nom.
	def is_in(self,couleur,taille1,taille2,imaginaire,reel,zoom,iterations):
		bol = True
		self.__c.execute('SELECT * FROM images_julia WHERE couleur=? AND taille1=? AND taille2=? AND imaginaire=? AND reel=? AND zoom=? AND iterations=?',(couleur,taille1,taille2,imaginaire,reel,zoom,iterations))
		r=self.__c.fetchone()
		if r==None: #si les paramètres de notre factale n'existent pas dans notre base de données
			nom='%i_%f_%f_%f_%f_%i_%i'%(couleur,taille1,taille2,imaginaire,reel,zoom,iterations)
			self.Ajouter_image(nom,couleur,taille1,taille2,imaginaire,reel,zoom,iterations) #ajout à la base de données
			self.__c.execute('SELECT DISTINCT Nom FROM images_julia WHERE couleur="%i" and taille1="%i" and taille2=%i  and imaginaire=%i and reel=%i and zoom=%i and iterations=%i'%(couleur,taille1,taille2,imaginaire,reel,zoom,iterations))        
			bol = False
		ads=self.__c.fetchone()
		return bol  ##renvoie si limage est ou non trouve dans la base de donnees
