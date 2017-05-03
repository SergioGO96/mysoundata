# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import os

url_base = 'http://www.omdbapi.com/?t='

pelicula= raw_input("pelicula: ")

r= requests.get(url_base+pelicula)
doc = r.json()
print doc