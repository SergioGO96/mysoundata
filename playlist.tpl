% include('header.tpl')
	<div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
      		<h3> Playlists </h3>
		<ol>
      		%for lista in listas["playlists"]:
      	 		<li><a href="{{lista["items"]["external_urls"]["spotify"][0]}}" >{{lista["name"][0]}}</a></li>
      		 %end
		 </ol>
	</article>
	</div>
     </main>
     </div>
% include('foot.tpl')
