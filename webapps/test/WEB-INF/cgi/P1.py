import math
from math import*
import cgi, cgitb
def set_value(name, value):
    name = value
def set_vertex(name, x, y):
    name = Point(x,y)
def get_value(name):
    return name
def get_all():
    return {a1, a2, a3, s1, s2, s3, s4, s5, s6, s7, h1, h2, h3, L1, L2, L3, L4, radius, diameter, circumference, p, art, arc, ar1, ar2, ar3, ar4}

form = cgi.FieldStorage()
if form.getvalue('a1'):
    a1=form.getvalue('a1')
else:
    a1=''
if form.getvalue('a2'):
    a2=form.getvalue('a2')
else:
    a2=''
if form.getvalue('a3'):
    a3=form.getvalue('a3')
else:
    a3=''
if form.getvalue('s1'):
    s1=form.getvalue('s1')
else:
    s1=''
if form.getvalue('s2'):
    s2=form.getvalue('s2')
else:
    s2=''
if form.getvalue('s3'):
    s3=form.getvalue('s3')
else:
    s3=''
if form.getvalue('s4'):
    s4=form.getvalue('s4')
else:
    s4=''
if form.getvalue('s5'):
    s5=form.getvalue('s5')
else:
    s5=''
if form.getvalue('s6'):
    s6=form.getvalue('s6')
else:
    s6=''
if form.getvalue('s7'):
    s7=form.getvalue('s7')
else:
    s7=''
if form.getvalue('h1'):
    h1=form.getvalue('h1')
else:
    h1=''
if form.getvalue('h2'):
    h2=form.getvalue('h2')
else:
    h2=''
if form.getvalue('h3'):
    h3=form.getvalue('h3')
else:
    h3=''
if form.getvalue('L1'):
    L1=form.getvalue('L1')
else:
    L1=''
if form.getvalue('L2'):
    L2=form.getvalue('L2')
else:
    L2=''
if form.getvalue('L3'):
    L3=form.getvalue('L3')
else:
    L3=''
if form.getvalue('radius'):
    radius=form.getvalue('radius')
else:
    radius=''
if form.getvalue('diameter'):
    diameter=form.getvalue('diameter')
else:
    diameter=''
if form.getvalue('circumference'):
    circumference=form.getvalue('circumference')
else:
    circumference=''
if form.getvalue('art'):
    art=form.getvalue('art')
else:
    art=''
if form.getvalue('arc'):
    arc=form.getvalue('arc')
else:
    arc=''
if form.getvalue('p'):
    p=form.getvalue('p')
else:
    p=''
if form.getvalue('ar1'):
    ar1=form.getvalue('ar1')
else:
    ar1=''
if form.getvalue('ar2'):
    ar2=form.getvalue('ar2')
else:
    ar2=''
if form.getvalue('ar3'):
    ar3=form.getvalue('ar3')
else:
    ar3=''
if form.getvalue('ar4'):
    ar4=form.getvalue('ar4')
else:
    ar4=''

    
#SSS
if s1 != '' and s2 != '' and s3 != '' and a1 == '' and a2 == '' and a3 == '':
    a1 = round(math.degrees(math.acos(round((math.pow(float(s2),2) + math.pow(float(s3),2) - math.pow(float(s1),2))/(2*float(s2)*float(s3)),2))),2)
    a2 = round(math.degrees(math.acos(round((math.pow(float(s1),2) + math.pow(float(s3),2) - math.pow(float(s2),2))/(2*float(s1)*float(s3)),2))),2)
    a3 = 180 - round(float(a1),2) - round(float(a2),2)

if s4 != '' and s5 != '' and s6 != '' and a4 == '' and a5 == '' and a6 == '':
    a4 = round(math.degrees(math.acos(round((math.pow(float(s5),2) + math.pow(float(s6),2) - math.pow(float(s4),2))/(2*float(s5)*float(s6)),2))),2)
    a5 = round(math.degrees(math.acos(round((math.pow(float(s4),2) + math.pow(float(s6),2) - math.pow(float(s5),2))/(2*float(s4)*float(s6)),2))),2)
    a6 = 180 - round(float(a4),2) - round(float(a5),2)

#AAS
#solve for angle given two others
if a2 != '' and a3 != '' and a1 == '':
    a1 = 180 - round(float(a2),2) - round(float(a3),2)

if a1 != '' and a3 != '' and a2 == '':
    a2 = 180 - round(float(a1),2) - round(float(a3),2)

if a1 != '' and a2 != '' and a3 == '':
    a3 = 180 - round(float(a1),2) - round(float(a2),2)

#solve for the sides
if s1 != '' and s2 == '' and s3 == '':
    s2 = round(math.sin(math.radians(float(a2)))*float(s1)/math.sin(math.radians(float(a1))),2)
    s3 = round(math.sin(math.radians(float(a3)))*float(s1)/math.sin(math.radians(float(a1))),2)

if s2 != '' and s1 == '' and s3 == '':
    s1 = round(math.sin(math.radians(float(a1)))*float(s2)/math.sin(math.radians(float(a2))),2)
    s3 = round(math.sin(math.radians(float(a3)))*float(s2)/math.sin(math.radians(float(a2))),2)

if s3 != '' and s1 == '' and s2 == '':
    s1 = round(math.sin(math.radians(float(a1)))*float(s3)/math.sin(math.radians(float(a3))),2)
    s2 = round(math.sin(math.radians(float(a2)))*float(s3)/math.sin(math.radians(float(a3))),2)

#ASA
#solve for angle given two others
if a2 != '' and a3 != '' and a1 == '':
    a1 = 180 - round(float(a2),2) - round(float(a3),2)

if a1 != '' and a3 != '' and a2 == '':
    a2 = 180 - round(float(a1),2) - round(float(a3),2)

if a1 != '' and a2 != '' and a3 == '':
    a3 = 180 - round(float(a1),2) - round(float(a2),2)
    ia3.setText(a3)
#solve for the sides
if s1 != '' and s2 == '' and s3 == '':
    s2 = math.sin(math.radians(float(a2)))*float(s1)/math.sin(math.radians(float(a1)))
    s3 = math.sin(math.radians(float(a3)))*float(s1)/math.sin(math.radians(float(a1)))

if s2 != '' and s1 == '' and s3 == '':
    s1 = math.sin(math.radians(float(a1)))*float(s2)/math.sin(math.radians(float(a2)))
    s3 = math.sin(math.radians(float(a3)))*float(s2)/math.sin(math.radians(float(a2)))

if s3 != '' and s1 == '' and s2 == '':
    s1 = math.sin(math.radians(float(a1)))*float(s3)/math.sin(math.radians(float(a3)))
    s2 = math.sin(math.radians(float(a2)))*float(s3)/math.sin(math.radians(float(a3)))

#SAS
if a1 != '' and a2 == '' and a3 == '' and s1 == '' and s2 != '' and s3 != '':
    s1 = round(math.sqrt(math.pow(float(s2),2)+math.pow(float(s3),2)-2*float(s2)*float(s3)*math.cos(math.radians(float(a1)))),2)

    if float(s2) > float(s3):
        a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
        a2 = 180 - float(a1) - float(a3)

    if float(s2) < float(s3):
        a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
        a3 = 180 - float(a1) - float(a2)

if a2 != '' and s1 == '' and s3 == '' and s1 != '' and s3 != '' and s2 == '':
    s2 = math.sqrt(math.pow(float(s1),2)+math.pow(float(s3),2)-2*float(s1)*float(s3)*math.cos(math.radians(float(a2))))

    if float(s1) > float(s3):
        a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a2)))/float(s2),2))),2)
        a1 = 180 - float(a2) - float(a3)

    if float(s1) < float(s3):
        a1 = math.degrees(math.asin(float(s1)*math.sin(math.radians(float(a2)))/float(s2)))
        a3 = 180 - float(a1) - float(a2)

if a3 != '' and s1 == '' and s2 == '' and s1 != '' and s2 != '' and s3 == '':
    s3 = math.sqrt(math.pow(float(s1),2)+math.pow(float(s2),2)-2*float(s1)*float(s2)*math.cos(math.radians(float(a3))))

    if float(s1) > float(s2):
        a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a3)))/float(s3),2))),2)
        a1 = 180 - float(a2) - float(a3)

    if float(s1) < float(s2):
        a1 = round(math.degrees(math.asin(round(float(s1)*math.sin(math.radians(float(a3)))/float(s3),2))),2)
        a2 = 180 - float(a1) - float(a3)

#SSA
#a1 is known
if a1 != '' and a2 == '' and a3 == '' and s1 != '' and s3 != '' and s2 == '':
    a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
    a2 = 180 - float(a1) - float(a3)

if a1 != '' and a2 == '' and a3 == '' and s1 != '' and s2 != '' and s3 == '':
    a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
    a3 = 180 - float(a1) - float(a2)

#a2 is known
if a2 != '' and a1 == '' and a3 == '' and s1 != '' and s2 != '' and s3 == '':
    a1 = round(math.degrees(math.asin(round(float(s1)*math.sin(math.radians(float(a2)))/float(s2),2))),2)
    a3 = 180 - float(a1) - float(a2)

if a2 != '' and a1 == '' and a3 == '' and s2 != '' and s3 != '' and s1 == '':
    a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a2)))/float(s2),2))),2)
    a1 = 180 - float(a2) - float(a3)

#a3 is known
if a3 != '' and a1 == '' and a2 == '' and s2 != '' and s3 != '' and s1 == '':
    a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a3)))/float(s3),2))),2)
    a1 = 180 - float(a2) - float(a3)

if a3 != '' and a1 == '' and a2 == '' and s1 != '' and s3 != '' and s2 == '':
    a1 = round(math.degrees(math.asin(round(float(s1)*math.sin(math.radians(float(a3)))/float(s3),2))),2)
    a2 = 180 - float(a1) - float(a3)



#solving for perimeter
if s1 != '' and s2 != '' and s3 != '':
    p = float(s1) + float(s2) + float(s3)


#solving for heights
#given one angle and 90 degrees, do AAS
if a2 != '' and s3 != '':
    h1 = round(round(float(s3),2)*math.sin(round(math.radians(float(a2)),2)),2)

if a3 != '' and s2 != '':
    h1 = round(round(float(s2),2)*math.sin(round(math.radians(float(a3)),2)),2)

if a1 != '' and s3 != '':
    h2 = round(round(float(s3),2)*math.sin(round(math.radians(float(a1)),2)),2)

if a3 != '' and s1 != '':
    h2 = round(round(float(s1),2)*math.sin(round(math.radians(float(a3)),2)),2)

if a1 != '' and s2 != '':
    h3 = round(round(float(s2),2)*math.sin(round(math.radians(float(a1)),2)),2)

if a2 != '' and s1 != '':
    h3 = round(round(float(s1),2)*math.sin(round(math.radians(float(a2)),2)),2)

#given area
if art != '' and s1 != '':
    h1 = 2 * round(float(art),2)/round(float(s1),2)

if art != '' and s2 != '':
    h2 = 2 * round(float(art),2)/round(float(s2),2)

if art != '' and s3 != '':
    h3 = 2 * round(float(art),2)/round(float(s3),2)

    
#solving for area of triangle
if s1 != '' and h1 != '' and art == '':
    art = 0.5 * round(float(s1),2) * round(float(h1),2)

if s2 != '' and h2 != '' and art == '':
    ar1 = 0.5 * round(float(s2),2) * round(float(h2),2)

if s3 != '' and h3 != '' and art == '':
    art = 0.5 * round(float(s3),2) * round(float(h3),2)


#solving for s4, s5, s6, s7
if s2 != '' and s7 != '':
    s6 = round(float(s2),2) - round(float(s7),2)

if s2 != '' and s6 != '':
    s7 = round(float(s2),2) - round(float(s6),2)

if s1 != '' and s5 != '':
    s4 = round(float(s1),2) - round(float(s5),2)

if s1 != '' and s4 != '':
    s5 = round(float(s1),2) - round(float(s4),2)


#solving for radius and diameter
if diameter != '' and radius == '':
    radius = round((float(diameter)/2),2)

if diameter == '' and radius != '':
    diameter = round((float(radius)*2),2)

if arc != '' and diameter == '' and radius == '':
    radius = round(math.sqrt(float(arc)/math.pi),2)
    diameter = round((float(radius)*2),2)


#solving for area of circle
if radius != '':
    arc = round((math.pi * math.pow(round(float(radius),2),2)),2)
if  ar1 != '' and ar2 != '' and ar3 != '':
    arc = round(float(ar1),2) + round(float(ar2),2) + round(float(ar3),2)
    
#solving for circumference
if diameter != '':
    circumference = round((float(diameter)*math.pi),2)
if  L1 != '' and L2 != '' and L3 != '': 
    circumference = round(float(L1),2) + round(float(L2),2) + round(float(L3),2)
    
#solving for arc lengths
if L2 != '' and L3 != '' and circumference != '':
    L1 = round(float(circumference),2) - round(float(L2),2) - round(float(L3),2)
if L1 != '' and L3 != '' and circumference != '':
    L2 = round(float(circumference),2) - round(float(L1),2) - round(float(L3),2)
if L1 != '' and L2 != '' and circumference != '':
    L3 = round(float(circumference),2) - round(float(L1),2) - round(float(L2),2)

#solving for partial areas
if ar2 != '' and ar3 != '' and arc != '':
    ar1 = round(float(arc),2) - round(float(ar2),2) - round(float(ar3),2)
if ar1 != '' and ar3 != '' and arc != '':
    ar2 = round(float(arc),2) - round(float(ar1),2) - round(float(ar3),2)
if ar1 != '' and ar2 != '' and arc != '':
    ar3 = round(float(arc),2) - round(float(ar1),2) - round(float(ar2),2)
if ar4 != '' and art != '':
    ar3 = round(float(art),2) - round(float(ar4),2)
if ar3 != '' and art != '':
    ar4 = round(float(art),2) - round(float(ar3),2)

print("Content-Type: text/html")
print()
print("<form id='p1' method='post'>")
print("<input type='hidden' id='p1' name='p1' value='2'>")
print("<h4> 1. A triangle and a circle have three intersection points:  <br />")
print("One intersection is on a vertex of the triangle, another intersection is on the adjacent side of the vertex, the third intersection is on opposite side of the vertex.</h4>")
print("<img src='P1.png'> <br />")
print("a1: <input name='a1' type='text' value=%s> <br /> <br />" % (a1))
print("a2: <input name='a2' type='text' value=%s> <br /> <br />" % (a2))
print("a3: <input name='a3' type='text' value=%s> <br /> <br />" % (a3))
print("s1: <input name='s1' type='text' value=%s> <br /> <br />" % (s1))
print("s2: <input name='s2' type='text' value=%s> <br /> <br />" % (s2))
print("s3: <input name='s3' type='text' value=%s> <br /> <br />" % (s3))
print("s4: <input name='s4' type='text' value=%s> <br /> <br />" % (s4))
print("s5: <input name='s5' type='text' value=%s> <br /> <br />" % (s5))
print("s6: <input name='s6' type='text' value=%s> <br /> <br />" % (s6))
print("s7: <input name='s7' type='text' value=%s> <br /> <br />" % (s7))
print("h1: <input name='h1' type='text' value=%s> <br /> <br />" % (h1))
print("h2: <input name='h2' type='text' value=%s> <br /> <br />" % (h2))
print("h3: <input name='h3' type='text' value=%s> <br /> <br />" % (h3))
print("L1: <input name='L1' type='text' value=%s> <br /> <br />" % (L1))
print("L2: <input name='L2' type='text' value=%s> <br /> <br />" % (L2))
print("L3: <input name='L3' type='text' value=%s> <br /> <br />" % (L3))
print("radius: <input name='radius' type='text' value=%s> <br /> <br />" % (radius))
print("diameter: <input name='diameter' type='text' value=%s> <br /> <br />" % (diameter))
print("circumference: <input name='circumference' type='text' value=%s> <br /> <br />" % (circumference))
print("art: <input name='art' type='text' value=%s> <br /> <br />" % (art))
print("arc: <input name='arc' type='text' value=%s> <br /> <br />" % (arc))
print("p: <input name='p' type='text' value=%s> <br /> <br />" % (p))
print("ar1: <input name='ar1' type='text' value=%s> <br /> <br />" % (ar1))
print("ar2: <input name='ar2' type='text' value=%s> <br /> <br />" % (ar2))
print("ar3: <input name='ar3' type='text' value=%s> <br /> <br />" % (ar3))
print("ar4: <input name='ar4' type='text' value=%s> <br /> <br />" % (ar4))
print("<input type='submit' value='Solve'/> <br /> <br />")
print("</form>")


