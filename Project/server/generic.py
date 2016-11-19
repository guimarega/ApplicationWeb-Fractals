import http.server
import socketserver
import sqlite3
from urllib.parse import urlparse, parse_qs
from server.julia import *
from server.serveur_SQL import *

# définition du handler generique
class RequestHandler(http.server.SimpleHTTPRequestHandler):

	image_counter = 0
  	# sous-répertoire racine des documents statiques
	static_dir = '/client'
  	# version du serveur
	server_version = 'Projet/serveur.py/0.1'
	
	def generation_image(self,real,imag,n_int,color,zoom):
		self.__width = 500
		return fractale(int(color),self.__width,self.__width,real,imag,zoom,n_int)

        # on envoie le document statique demandé
	def send_static(self):
                # on modifie le chemin d'accès en insérant le répertoire préfixe
		self.path = self.static_dir + self.path
		# on calcule le nom de la méthode parent à appeler (do_GET ou do_HEAD)
		# à partir du verbe HTTP (GET ou HEAD)
		method = 'do_{}'.format(self.command)

		# on traite la requête via la classe parent
		getattr(http.server.SimpleHTTPRequestHandler,method)(self)

	def send_html(self,content):
		headers = [('Content-Type','text/html;charset=utf-8')]
		html = '<!DOCTYPE html><title>{}</title><meta charset="utf-8">{}'.format(self.path_info[0],content)
		self.send(html,headers)

	# on envoie la réponse
	def send(self,body,headers=[]):
		encoded = bytes(body, 'UTF-8')
		self.send_response(200)
		[self.send_header(*t) for t in headers]
		self.send_header('Content-Length',int(len(encoded)))
		self.end_headers()
		self.wfile.write(encoded)


	# on analyse la requête pour initialiser nos paramètres
	def init_params(self):
		# analyse de l'adresse
		info = urlparse(self.path)
		self.path_info = info.path.split('/')[1:]
		self.query_string = info.query
		self.params = parse_qs(info.query)

		# récupération du corps
		length = self.headers.get('Content-Length')
		ctype = self.headers.get('Content-Type')
		if length:
			self.body = str(self.rfile.read(int(length)),'utf-8')
		if ctype == 'application/x-www-form-urlencoded' :
			self.params = parse_qs(self.body)
		else:
			self.body = ''
		print(length,ctype,self.body, self.params)
