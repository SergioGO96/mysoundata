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
		valoracion = doc["imdbRating"]
		poster = doc["Poster"]
		if doc["Poster"]=="N/A":
			return template('resultadosin.tpl',titulo=titulo,estreno=estreno,calificacion=calificacion,duracion=duracion,genero=genero,director=director,guionistas=guionistas,actores=actores,pais=pais,valoracion=valoracion,poster=poster)
		else:
			poster = doc["Poster"]
			return template('resultado.tpl',titulo=titulo,estreno=estreno,calificacion=calificacion,duracion=duracion,genero=genero,director=director,guionistas=guionistas,actores=actores,pais=pais,valoracion=valoracion,poster=poster)
@get('/login')
def LOGIN():
	if token_valido():
   		 redirect("/listas")
  	else:
    	response.set_cookie("token", '',max_age=0)
    	oauth2 = OAuth2Session(client_id, redirect_uri=redirect_uri,scope=scope)
   	authorization_url, state = oauth2.authorization_url('https://accounts.spotify.com/authorize/')
   	response.set_cookie("oauth_state", state)
   	redirect(authorization_url)

		
@route('/static/<filepath:path>')
def server_static(filepath):
        return static_file(filepath, root='static') 

run(host='0.0.0.0',port=argv[1])
