#--------------------------------------------------------
#			Serveur
#	Le but: Creation et execution du serveur en
#	traitant les methodes GET's. 
#--------------------------------------------------------
import os
import os.path
import http.server
import socketserver
import sqlite3
from urllib.parse import urlparse, parse_qs
import server
from server.julia import nomCreation
from server.serveur_SQL import *
from server import generic

# définition du handler
class RequestHandler(generic.RequestHandler):
	# Initialisation de la base de donnees
	baseBD = BD()		
	baseBD.initialisation()

	# Ajoute une image dans la base de donnees
	def ajouteImageBD(self,nom,couleur,taille1,taille2,imaginaire,reel,zoom,iterations):
		return self.baseBD.Ajouter_image(nom,couleur,taille1,taille2,imaginaire,reel,zoom,iterations)

	# Cherche dans la base de donnees si il limage a deja ete creee
	def chercheImageBD(self,couleur,taille1,taille2,imaginaire,reel,zoom,iterations):
		return self.baseBD.is_in(couleur,taille1,taille2,imaginaire,reel,zoom,iterations)

	# on surcharge la méthode qui traite les requêtes GET
	def do_GET(self):
		# traitement des informations recus
		self.init_params()
		# requete GET servide
		if(self.path_info[0] == "service"):
			self.__real = self.path_info[1]		# Il obtient la valeur de la partie reel
			self.__imag = self.path_info[2]		# Il obtient la valeur de la partie imaginaire
			self.__n_int = self.path_info[3]	# Il obtient la valeur du numero dinterations
			self.__colornumber = self.path_info[4]	# Il obtient la coleur choisie
			self.__zoom = int(self.path_info[5])	# Il obtient la valeur du Zoom
		
			# Creation du nom de limage
			self.__nom = server.julia.nomCreation(self.__real,self.__imag,self.__n_int,self.__colornumber,self.__zoom)

			# Information de la requete
			print("Resquest: Image\n-----------------------\nParameters:\nConstante: {}+i{}\nNumber of Interations: {}\nColor Number: {}\nZoom: {}x\n-----------------------".format(self.__real,self.__imag,self.__n_int,self.__colornumber,self.__zoom))
 
			# Cherche dans la base de donnees si limage a deja ete cree
			if(self.chercheImageBD(int(self.__colornumber),500,500,float(self.__imag),float(self.__real),int(self.__zoom),int(self.__n_int)) == True):
				print('-----------------------\nImage:{}\nRecovered from the database.\n-----------------------'.format(self.__nom))
				self.send_html("images/{}.png".format(server.julia.nomCreation(float(self.__real),float(self.__imag),int(self.__n_int),int(self.__colornumber),self.__zoom)))
			# Generation dune nouvelle image.
			else:
				print('-----------------------\nImage:{}\nCreation.\n-----------------------'.format(self.__nom))
				self.generation_image(float(self.__real),float(self.__imag),int(self.__n_int),self.__colornumber,self.__zoom).save("client/images/"+self.__nom+'.png','PNG')
				self.send_html("images/{}.png".format(self.__nom))
		# Envoie le page statique
		else:
			self.send_static()


#Initialisation du serveur
Handler = RequestHandler
PORT = 8080	# Port utilisee
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()
