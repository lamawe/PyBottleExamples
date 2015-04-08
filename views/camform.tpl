% include('beginhtml.tpl')
% include('mainmenu.tpl')
<div class="container"
   <form action="/camera" method="post">
   File Format: <select name="filetype">
                    <option value="jpg">JPG</option>
                    <option value="gif">GIF</option>
                    <option value="bmp">BMP</option>
                </select><br/>       
   <input value="Go" type="submit" />
   </form>
</div>
% include('endhtml.tpl')
