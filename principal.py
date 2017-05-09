# -*- coding: utf-8 -*-
from bottle import *
import requests
from sys import argv
from urlparse import parse_qs
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
import json

url_base = 'http://www.omdbapi.com/?t='
client_id='d9afcb301391465dbc1ea87d231c4dcc'
client_secret='7657feabd24541688c96c08c6c9098b6'
token_url = "https://accounts.spotify.com/api/token"
redirect_uri = 'https://mysoundata.herokuapp.com/callback'
scope = ['playlist-read-private', 'playlist-read-collaborative','playlist-modify-public']

def token_valido():
  token=request.get_cookie("token", secret='some-secret-key')
  if token:
    token_ok = True
    try:
      oauth2 = OAuth2Session(client_id, token=token)
      r = oauth2.get('https://www.googleapis.com/oauth2/v1/userinfo')
    except TokenExpiredError as e:
      token_ok = False
  else:
    token_ok = False
  return token_ok

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
    		redirect("/principal")
 	else:
    		response.set_cookie("token", '',max_age=0)
    		oauth2 = OAuth2Session(client_id, redirect_uri=redirect_uri,scope=scope)
    		authorization_url, state = oauth2.authorization_url('https://accounts.spotify.com/authorize/')
    		response.set_cookie("oauth_state", state)
    		redirect(authorization_url)

@get('/callback')
def get_token():
  	oauth2 = OAuth2Session(client_id, state=request.cookies.oauth_state,redirect_uri=redirect_uri)
  	token = oauth2.fetch_token(token_url, client_secret=client_secret,authorization_response=request.url)
 	response.set_cookie("token", token,secret='some-secret-key')
  	redirect("/principal")

@get('/principal')
def personal():
	return template('principal.tpl')

@get('/logout')
def salir():
	response.set_cookie("token", '',max_age=0)
    	redirect('/login')
	
@route('/lista',method='POST')
def listas():
	url_lista = request.forms.get('nombre')
	token = request.get_cookie("token", secret='some-secret-key')
	tokens = token["token_type"]+" "+token["access_token"]
	headers = {"Accept":"aplication/json","Authorization":tokens}
	canciones = requests.get(url_lista, headers=headers)
	if canciones.status_code == 200:
		canciones = canciones.json()
		lista_canciones = []
		for cancion in canciones['items']:
			nombre_cancion = cancion["track"]["name"]+" - "+cancion["track"]["artists"][0]["name"]
	return template('canciones.tpl',lista_canciones=lista_canciones)
		
@route('/static/<filepath:path>')
def server_static(filepath):
        return static_file(filepath, root='static') 

run(host='0.0.0.0',port=argv[1])
