# -*- coding: utf-8 -*-
from bottle import Bottle, route, run, request, template, default_app, static_file, get, post, response, redirect 
import requests
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
from urlparse import parse_qs
import json
url_base = 'http://www.omdbapi.com/?t='
key= "379aa02bced1074f7164c9f4d83c10a9"

@route('/index',method="get")
def inicio():
	pelicula= raw_input("pelicula: ")

r= requests.get(url_base+pelicula)
doc = r.json()
if doc["Response"] == "False":
	print "ERROR"
else:
	print "Titulo: " + doc["Title"]
	print "Estreno: " + doc["Released"]
	print "Calificacion de edad: " + doc["Rated"]
	print "Duracion: " + doc["Runtime"]
	print "Genero: " + doc["Genre"]
	print "Director: " + doc["Director"]
	print "Guionistas: " + doc["Writer"]
	print "Actores: " + doc["Actors"]
	print "Pais: " + doc["Country"]
	print "Produccion: " + doc["Production"]
	print "Pagina Web: " + doc["Website"]
	print "Valoracion: " + doc["imdbRating"]
	print "Recaudacion: " + doc["BoxOffice"]
	return ""