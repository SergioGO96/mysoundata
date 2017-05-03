# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import os

url_base = 'http://www.omdbapi.com/?t='

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

