%include('header.tpl')
<p>Titulo: {{titulo}}</p>
<a href="/"><img src="/static/images/noposter.png"/></a>
<p>Estreno: {{estreno}}</p>
<p>Calificacion: {{calificacion}}</p>
<p>Duracion: {{duracion}}</p>
<p>Genero: {{genero}}</p>
<p>Director: {{director}}</p>
<p>Guionistas: {{guionistas}}
<p>Actores: {{actores}}</p>
<p>Pais: {{pais}}</p>
<p>Valoracion: {{valoracion}}</p>
<p> {{url_playlists}}/p>
<nav class="right">
  <a href="/lista" class="button alt2">Acceder a la lista de reproduccion</a>
</nav>
%include('foot.tpl')
