# -*- coding: utf-8 -*-
from bottle import *
import requests
from sys import argv
from urlparse import parse_qs
import json
url_base = 'http://www.omdbapi.com/?t='
key= "379aa02bced1074f7164c9f4d83c10a9"

@route('/', method="get")
def formularioinicio():
	return template('formularioinicio.tpl')

@route('/index',method="post")
def inicio():
	pelicula = request.forms.get('pelicula')
	r= requests.get(url_base+pelicula)
	doc = r.json()
	if doc["Response"] == "False":
		return template('NoExiste.tpl')
	else:
		titulo = doc["Title"]
		estreno = doc["Released"]
		calificacion = doc["Rated"]
		duracion = doc["Runtime"]
		genero = doc["Genre"]
		director = doc["Director"]
		guionistas = doc["Writer"]
		actores = doc["Actors"]
		pais = doc["Country"]
		Produccion = doc["Production"]
		web = doc["Website"]
		valoracion = doc["imdbRating"]
		recaudacion = doc["BoxOffice"]
		if doc["Poster"]=="N/A":
			return template('resultadosin.tpl',titulo=titulo,estreno=estreno,calificacion=calificacion,duracion=duracion,genero=genero,director=director,guionistas=guionistas,actores=actores,pais=pais,Produccion=Produccion,web=web,valoracion=valoracion,recaudacion=recaudacion,poster=poster)
		else:
			poster = doc["Poster"]
			return template('resultado.tpl',titulo=titulo,estreno=estreno,calificacion=calificacion,duracion=duracion,genero=genero,director=director,guionistas=guionistas,actores=actores,pais=pais,Produccion=Produccion,web=web,valoracion=valoracion,recaudacion=recaudacion,poster=poster)

@route('/static/<filepath:path>')
def server_static(filepath):
        return static_file(filepath, root='static') 

run(host='0.0.0.0',port=argv[1])
