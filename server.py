import http.server
import socketserver
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


class MonHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("appel de l'url :",self.path)
        #on découpe l'url en url et parametres
        url = self.path.split("?")

        #On crée un dictionnaire pour récupérer les paramètres
        mondicoparam = dict()
        if len(url)>1 :
            parametres = url[1].split("&")
            # On remplit un dictionnaire avec les parametres
            mondicoparam = dict()
            for unparametre in parametres:
                par_valeur = unparametre.split('=')
                mondicoparam[par_valeur[0]] = par_valeur[1]
                
        print(mondicoparam)
        
        if url[0] == "/mapage.html" and len(mondicoparam)>=1:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytearray("<html><body>","latin-1"))
            self.wfile.write(bytearray("Rendez-vous sur <a href='templates/widget.html'> la page Pole Emploi</a> pour faire une recherche. Les mots clés interessants dans votre CV sont <br>","latin-1"))
            #On ouvre le fichier texte pour comparer aux valeurs du dictionnaire
            with open('templates/wordscv.txt','r') as file:
                listecompetences = file.readlines()
                for unecompetence in listecompetences:
                    # Nettoyage du saut de ligne pour comparer les valeurs
                    if  unecompetence.rstrip('\n') in mondicoparam.values():
                        self.wfile.write(bytearray(unecompetence.rstrip('\n'),"utf8"))
                        self.wfile.write(bytearray("<br>","utf8"))

            self.wfile.write(bytearray("</body></html>","utf8"))
        elif self.path == "/":
            print("protection du répertoire")
            self.send_response(404)
        else :
            http.server.SimpleHTTPRequestHandler.do_GET(self)


fichierHTML = os.path.dirname(os.path.realpath(__file__))+"\mapage.html"
fichierAPI = os.path.dirname(os.path.realpath(__file__))+"\metros.json"

PORT = 8080
#Handler = http.server.SimpleHTTPRequestHandler            

# Astuce MonHandler est appelé en paramètre
with socketserver.TCPServer(("", PORT), MonHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
