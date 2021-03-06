# -*- coding: utf-8 -*-
from bottle import *
import requests
from sys import argv
from urlparse import parse_qs
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
import json
import os

url_base = 'https://api.themoviedb.org/3'
client_id= os.environ["client_id"]
client_secret= os.environ["client_secret"]
key = os.environ["key"]
token_url = "https://accounts.spotify.com/api/token"
redirect_uri = 'https://mysoundata.herokuapp.com/callback'
scope = ['playlist-modify-public']



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
	url_playlists = "https://api.spotify.com/v1/search?q="+pelicula.replace(' ','%20')+"&type=playlist&market=US"
	r= requests.get(url_base+"/search/movie?api_key="+key+"&language=es&query="+pelicula)
	doc = r.json()
	if doc["total_results"] == 0:
		return template('NoExiste.tpl')
	else:
		datos = doc["results"][0]
		titulo = datos["title"]
		titulo2 = datos["original_title"]
		estreno = datos["release_date"]
		sinopsis = datos["overview"]
		pais = datos["original_language"]
		valoracion = datos["vote_average"]
		postersin = datos["poster_path"]
		poster = "https://image.tmdb.org/t/p/w500"+postersin
		return template('resultado.tpl',url_playlists=url_playlists,sinopsis=sinopsis,titulo=titulo,titulo2=titulo2,estreno=estreno,pais=pais,valoracion=valoracion,poster=poster)
		
@get('/login')
def LOGIN():
	if token_valido():
    		redirect("/")
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
  	redirect("/")	
	
@route('/lista',method='POST')
def list():
	if token_valido():
		url= request.forms.get("url")
		listas = requests.get(url)
		if listas.status_code == 200:
			playlists = []
			nombre = []
			listas = listas.json()
			for a in listas["playlists"]["items"]:
				playlists.append(a.get("external_urls").get("spotify"))
				nombre.append(a.get("name"))

			return template('playlist.tpl',playlists=playlists,nombre=nombre)
	else:
		redirect("/login")
@route('/static/<filepath:path>')
def server_static(filepath):
        return static_file(filepath, root='static') 

run(host='0.0.0.0',port=argv[1])
