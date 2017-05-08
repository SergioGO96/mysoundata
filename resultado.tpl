%include('header.tpl')
<p>Titulo: {{titulo}}</p>
<a href="/"><img src={{poster}}/></a>
<p>Estreno: {{estreno}}</p>
<p>Calificacion: {{calificacion}}</p>
<p>Duracion: {{duracion}}</p>
<p>Genero: {{genero}}</p>
<p>Director: {{director}}</p>
<p>Guionistas: {{guionistas}}
<p>Actores: {{actores}}</p>
<p>Pais: {{pais}}</p>
<p>Valoracion: {{valoracion}}</p>
<nav class="right">
  <a href="/login" class="submit">Acceder a la lista de reproduccion</a>
</nav>
%include('foot.tpl')
