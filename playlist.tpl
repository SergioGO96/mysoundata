% include('header.tpl')
	<div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
      		<h3> Playlists </h3>
		<ol>
      		%for a in listas["playlists"]["items"]:
			b = a.get["external_urls"]
			c = a.get["name"]
   			<!-- <li><a href="a"> b</a></li> -->
			
      		 %end
		 </ol>
	</article>
	</div>
     </main>
     </div>
% include('foot.tpl')
