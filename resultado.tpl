%include('header.tpl')
<p>Titulo: {{titulo}}</p>
<p>Titulo Original: {{titulo2}}</p>
% if poster!=" ":
	<a href="/"><img src= "{{poster}} alt="IMAGEN"/></a>
	<p>{{poster}}</p>
%else:
	<a href="/"><img src="/static/images/noposter.png" alt="IMAGEN"/></a>
%end
<p>Estreno: {{estreno}}</p>
<p>Calificacion: {{valoracion}}</p>
<p>Sinopsis: {{sinopsis}}</p>
<p>Pais: {{pais}}</p>
<nav class="right">
<form action="/lista" method="post">
<input type="hidden" name="url" value="{{!url_playlists}}">
<INPUT type="submit" value="Acceder a la lista de reproduccion">
</form>
</nav>
%include('foot.tpl')
