% include('header.tpl')
	<div class="wrapper row3">
    <main class="container clear"> 
      <div class="group btmspace-80">
        <article>
      		<h3> Playlists </h3>
		<ol>
      		%for a,b in zip(playlists,nombre):
   			<li><a href="{{a}}"> {{b}}</a></li>
			
      		 %end
		 </ol>
	</article>
	</div>
     </main>
     </div>
% include('foot.tpl')
