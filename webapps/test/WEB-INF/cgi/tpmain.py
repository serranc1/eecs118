import cgi
#To access the website, go to http://127.0.0.1:8080/test/cgi-bin/tpmain.py
#To ensure that the webpage works, change the param-name in the cgi servlet in conf\web.xml in the tomcat folder to the directory where python.exe is (Ex: C:\Python34\python.exe)
#In the conf\context.xml file, modify the Context line to say <Context privileged="true">
#Make sure to put the files in the proper directories by following the hierarchy in eecs118-master
print("Content-Type: text/html")
print()
print("<form id='p1' method='post' action='http://127.0.0.1:8080/test/cgi-bin/Problem 1.py'>")
print("<input type='hidden' id='p1' name='p1' value='1'>")
print("<h4> 1. A triangle and a circle have three intersection points: <br />")
print("One intersection is on a vertex of the triangle, another intersection is on the adjacent side of the vertex, the third intersection is on opposite side of the vertex.</h4>")
print("<img src='http://127.0.0.1:8080/test/P1.png'> <br />")
print("<input type='submit' value='Solve'/> <br /> <br />")
print("</form>")
print("<form id='p2' method='post' action='http://127.0.0.1:8080/test/cgi-bin/Problem 2.py'>")
print("<input type='hidden' id='p2' name='p2' value='2'>")
print("<h4> 2. A triangle and a circle have four intersection points:  <br />")
print("Two intersections are two vertices of the triangle, two other intersections are on two sides.</h4>")
print("<img src='http://127.0.0.1:8080/test/P2.png'> <br />")
print("<input type='submit' value='Solve'/> <br /> <br />")
print("</form>")
print("<form id='p3' method='post' action='http://127.0.0.1:8080/test/cgi-bin/Problem 3.py'>")
print("<input type='hidden' id='p3' name='p3' value='3'>")
print("<h4> 3. Two triangles have one intersection point: <br />")
print("The intersection can be on a side or a vertex.</h4>")
print("<img src='http://127.0.0.1:8080/test/P3.png'> <br />")
print("<input type='submit' value='Solve'/> <br /> <br />")
print("</form>")
