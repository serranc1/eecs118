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
    return {a1, a2, a3, a4, a5, a6, a7, a8, s1, s2, s3, s4, s5, s6, s7, s8, h1, h2, h3, h4, h5, h6, ar1, ar2, p1, p2}

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
if form.getvalue('a4'):
    a4=form.getvalue('a4')
else:
    a4=''
if form.getvalue('a5'):
    a5=form.getvalue('a5')
else:
    a5=''
if form.getvalue('a6'):
    a6=form.getvalue('a6')
else:
    a6=''
if form.getvalue('a7'):
    a7=form.getvalue('a7')
else:
    a7=''
if form.getvalue('a8'):
    a8=form.getvalue('a8')
else:
    a8=''
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
if form.getvalue('s8'):
    s8=form.getvalue('s8')
else:
    s8=''
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
if form.getvalue('h4'):
    h4=form.getvalue('h4')
else:
    h4=''
if form.getvalue('h5'):
    h5=form.getvalue('h5')
else:
    h5=''
if form.getvalue('h6'):
    h6=form.getvalue('h6')
else:
    h6=''
if form.getvalue('ar1'):
    ar1=form.getvalue('ar1')
else:
    ar1=''
if form.getvalue('ar2'):
    ar2=form.getvalue('ar2')
else:
    ar2=''
if form.getvalue('p1'):
    p1=form.getvalue('p1')
else:
    p1=''
if form.getvalue('p2'):
    p2=form.getvalue('p2')
else:
    p2=''
    
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
#Triangle 1
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

#Triangle 2
#solve for angle given two others
if a5 != '' and a6 != '' and a4 == '':
    a4 = 180 - round(float(a5),2) - round(float(a6),2)

if a4 != '' and a6 != '' and a5 == '':
    a5 = 180 - round(float(a4),2) - round(float(a6),2)

if a4 != '' and a5 != '' and a6 == '':
    a6 = 180 - round(float(a4),2) - round(float(a5),2)

#solve for the sides
if s4 != '' and s5 == '' and s6 == '':
    s5 = math.sin(math.radians(float(a5)))*float(s4)/math.sin(math.radians(float(a4)))
    s6 = math.sin(math.radians(float(a6)))*float(s4)/math.sin(math.radians(float(a4)))

if s5 != '' and s4 == '' and s6 == '':
    s4 = math.sin(math.radians(float(a4)))*float(s5)/math.sin(math.radians(float(a5)))
    s6 = math.sin(math.radians(float(a6)))*float(s5)/math.sin(math.radians(float(a5)))

if s6 != '' and s4 == '' and s5 == '':
    s4 = math.sin(math.radians(float(a4)))*float(s6)/math.sin(math.radians(float(a6)))
    s5 = math.sin(math.radians(float(a5)))*float(s6)/math.sin(math.radians(float(a6)))

#ASA
#Triangle 1
#solve for angle given two others
if a2 != '' and a3 != '' and a1 == '':
    a1 = 180 - round(float(a2),2) - round(float(a3),2)

if a1 != '' and a3 != '' and a2 == '':
    a2 = 180 - round(float(a1),2) - round(float(a3),2)

if a1 != '' and a2 != '' and a3 == '':
    a3 = 180 - round(float(a1),2) - round(float(a2),2)

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

#Triangle 2
#solve for angle given two others
if a5 != '' and a6 != '' and a4 == '':
    a4 = 180 - round(float(a5),2) - round(float(a6),2)

if a4 != '' and a6 != '' and a4 == '':
    a5 = 180 - round(float(a4),2) - round(float(a6),2)

if a4 != '' and a5 != '' and a6 == '':
    a6 = 180 - round(float(a4),2) - round(float(a5),2)

#solve for the sides
if s4 != '' and s5 == '' and s6 == '':
    s5 = math.sin(math.radians(float(a5)))*float(s4)/math.sin(math.radians(float(a4)))
    s6 = math.sin(math.radians(float(a6)))*float(s4)/math.sin(math.radians(float(a4)))

if s5 != '' and s4 == '' and s6 == '':
    s4 = math.sin(math.radians(float(a4)))*float(s5)/math.sin(math.radians(float(a5)))
    s6 = math.sin(math.radians(float(a6)))*float(s5)/math.sin(math.radians(float(a5)))

if s6 != '' and s4 == '' and s5 == '':
    s4 = math.sin(math.radians(float(a4)))*float(s6)/math.sin(math.radians(float(a6)))
    s5 = math.sin(math.radians(float(a5)))*float(s6)/math.sin(math.radians(float(a6)))

#SAS
#Triangle 1
if a1 != '' and a2 == '' and a3 == '' and s1 == '' and s2 != '' and s3 != '':
    s1 = round(math.sqrt(math.pow(float(s2),2)+math.pow(float(s3),2)-2*float(s2)*float(s3)*math.cos(math.radians(float(a1)))),2)
    is1.setText(s1)
    if float(s2) > float(s3):
        a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
        a2 = 180 - float(a1) - float(a3)

    if float(s2) < float(s3):
        a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
        a3 = 180 - float(a1) - float(a2)

if a2 != '' and s1 == '' and s3 == '' and s1 != '' and s3 != '' and s2 == '':
    s2 = math.sqrt(math.pow(float(s1),2)+math.pow(float(s3),2)-2*float(s1)*float(s3)*math.cos(math.radians(float(a2))))
    is2.setText(s2)
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

#Triangle 2
if a4 != '' and a5 == '' and a6 == '' and s4 == '' and s5 != '' and s6 != '':
    s4 = round(math.sqrt(math.pow(float(s5),2)+math.pow(float(s6),2)-2*float(s5)*float(s6)*math.cos(math.radians(float(a4)))),2)

    if float(s5) > float(s6):
        a6 = round(math.degrees(math.asin(round(float(s6)*math.sin(math.radians(float(a4)))/float(s4),2))),2)
        a5 = 180 - float(a4) - float(a6)

    if float(s5) < float(s6):
        a5 = round(math.degrees(math.asin(round(float(s5)*math.sin(math.radians(float(a4)))/float(s4),2))),2)
        a6 = 180 - float(a4) - float(a5)

if a5 != '' and a4 == '' and a6 == '' and s4 != '' and s6 != '' and s5 == '':
    s5 = round(math.sqrt(math.pow(float(s4),2)+math.pow(float(s6),2)-2*float(s4)*float(s6)*math.cos(math.radians(float(a5)))),2)

    if float(s4) > float(s6):
        a6 = round(math.degrees(math.asin(round(float(s6)*math.sin(math.radians(float(a5)))/float(s5),2))),2)
        a4 = 180 - float(a5) - float(a6)

    if float(s4) < float(s6):
        a4 = round(math.degrees(math.asin(round(float(s4)*math.sin(math.radians(float(a5)))/float(s5),2))),2)
        a6 = 180 - float(a4) - float(a5)


if a6 != '' and a4 == '' and a5 == '' and s4 != '' and s5 != '' and s6 == '':
    s6 = round(math.sqrt(math.pow(float(s4),2)+math.pow(float(s5),2)-2*float(s4)*float(s5)*math.cos(math.radians(float(a6)))),2)

    if float(s4) > float(s5):
        a5 = round(math.degrees(math.asin(round(float(s5)*math.sin(math.radians(float(a6)))/float(s6),2))),2)
        a4 = 180 - float(a5) - float(a6)

    if float(s4) < float(s5):
        a4 = round(math.degrees(math.asin(round(float(s4)*math.sin(math.radians(float(a6)))/float(s6),2))),2)
        a5 = 180 - float(a4) - float(a6)

#SSA
#Triangle 1
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

#Triangle 2
#a4 is known
if a4 != '' and a5 == '' and a6 == '' and s4 != '' and s5 != '' and s6 == '':
    a5 = round(math.degrees(math.asin(round(float(s5)*math.sin(math.radians(float(a4)))/float(s4),2))),2)
    a6 = 180 - float(a4) - float(a5)

if a4 != '' and a5 == '' and a6 == '' and s4 != '' and s6 != '' and s5 == '':
    a6 = round(math.degrees(math.asin(round(float(s6)*math.sin(math.radians(float(a4)))/float(s4),2))),2)
    a5 = 180 - float(a4) - float(a6)

#a5 is known
if a5 != '' and a4 == '' and a6 == '' and s4 != '' and s5 != '' and s6 == '':
    a4 = round(math.degrees(math.asin(round(float(s4)*math.sin(math.radians(float(a5)))/float(s5),2))),2)
    a6 = 180 - float(a4) - float(a5)

if a5 != '' and a4 == '' and a6 == '' and s5 != '' and s6 != '' and s4 == '':
    a6 = round(math.degrees(math.asin(round(float(s6)*math.sin(math.radians(float(a5)))/float(s5),2))),2)
    a4 = 180 - float(a5) - float(a6)

#a6 is known    
if a6 != '' and a4 == '' and a5 == '' and s4 != '' and s6 != '' and s5 == '':
    a4 = round(math.degrees(math.asin(round(float(s4)*math.sin(math.radians(float(a6)))/float(s6),2))),2)
    a5 = 180 - float(a4) - float(a6)

if a6 != '' and a4 == '' and a5 == '' and s5 != '' and s6 != '' and s4 == '':
    a5 = round(math.degrees(math.asin(round(float(s5)*math.sin(math.radians(float(a6)))/float(s6),2))),2)
    a4 = 180 - float(a4) - float(a5)



#solving for perimeter
if s1 != '' and s2 != '' and s3 != '':
    p1 = float(s1) + float(s2) + float(s3)

if s4 != '' and s5 != '' and s6 != '':
    p2 = float(s4) + float(s5) + float(s6)

#solving sides with perimeter
if p1 != '' and s2 != '' and s3 != '':
    s1 = float(p1) - float(s2) - float(s3)
if p1 != '' and s1 != '' and s3 != '':
    s2 = float(p1) - float(s1) - float(s3)
if p1 != '' and s1 != '' and s2 != '':
    s3 = float(p1) - float(s1) - float(s2)
if p2 != '' and s5 != '' and s6 != '':
    s4 = float(p2) - float(s5) - float(s6)
if p2 != '' and s1 != '' and s3 != '':
    s5 = float(p2) - float(s4) - float(s6)
if p2 != '' and s1 != '' and s2 != '':
    s6 = float(p2) - float(s4) - float(s5)


#solving for heights
#Triangle 1
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

#Triangle 2
#given one angle and 90 degrees, do AAS
if a5 != '' and s6 != '':
    h4 = round(round(float(s6),2)*math.sin(round(math.radians(float(a5)),2)),2)

if a6 != '' and s5 != '':
    h4 = round(round(float(s5),2)*math.sin(round(math.radians(float(a6)),2)),2)

if a4 != '' and s6 != '':
    h5 = round(round(float(s6),2)*math.sin(round(math.radians(float(a4)),2)),2)

if a6 != '' and s4 != '':
    h5 = round(round(float(s4),2)*math.sin(round(math.radians(float(a6)),2)),2)

if a4 != '' and s5 != '':
    h6 = round(round(float(s5),2)*math.sin(round(math.radians(float(a4)),2)),2)

if a5 != '' and s4 != '':
    h6 = round(round(float(s4),2)*math.sin(round(math.radians(float(a5)),2)),2)


#solving for area
if s1 != '' and h1 != '':
    ar1 = 0.5 * round(float(s1),2) * round(float(h1),2)

if s2 != '' and h2 != '':
    ar1 = 0.5 * round(float(s2),2) * round(float(h2),2)

if s3 != '' and h3 != '':
    ar1 = 0.5 * round(float(s3),2) * round(float(h3),2)

if s4 != '' and h4 != '':
    ar2 = 0.5 * round(float(s4),2) * round(float(h4),2)

if s5 != '' and h6 != '':
    ar2 = 0.5 * round(float(s5),2) * round(float(h5),2)

if s6 != '' and h6 != '':
    ar2 = 0.5 * round(float(s6),2) * round(float(h6),2)



#solving for s7 and s8
if s4 != '' and s8 != '':
    s7 = round(float(s4),2) - round(float(s8),2)

if s4 != '' and s7 != '':
    s8 = round(float(s4),2) - round(float(s7),2)


#solving for a7 and a8
if a3 != '' and a8 != '' and a7:
    a7 = 180 - round(float(a3),2) - round(float(a8),2)

if a3 != '' and a7 != '':
    a8 = 180 - round(float(a3),2) - round(float(a7),2)       
print("Content-Type: text/html")
print()
print("<form id='p3' method='post'>")
print("<input type='hidden' id='p3' name='p3' value='3'>")
print("<h4> 3. Two triangles have one intersection point: <br />")
print("The intersection can be on a side or a vertex.</h4>")
print("<img src='P3.png'> <br />")
print("a1: <input name='a1' type='text' value=%s> <br /> <br />" % (a1))
print("a2: <input name='a2' type='text' value=%s> <br /> <br />" % (a2))
print("a3: <input name='a3' type='text' value=%s> <br /> <br />" % (a3))
print("a4: <input name='a4' type='text' value=%s> <br /> <br />" % (a4))
print("a5: <input name='a5' type='text' value=%s> <br /> <br />" % (a5))
print("a6: <input name='a6' type='text' value=%s> <br /> <br />" % (a6))
print("a7: <input name='a7' type='text' value=%s> <br /> <br />" % (a7))
print("a8: <input name='a8' type='text' value=%s> <br /> <br />" % (a8))
print("s1: <input name='s1' type='text' value=%s> <br /> <br />" % (s1))
print("s2: <input name='s2' type='text' value=%s> <br /> <br />" % (s2))
print("s3: <input name='s3' type='text' value=%s> <br /> <br />" % (s3))
print("s4: <input name='s4' type='text' value=%s> <br /> <br />" % (s4))
print("s5: <input name='s5' type='text' value=%s> <br /> <br />" % (s5))
print("s6: <input name='s6' type='text' value=%s> <br /> <br />" % (s6))
print("s7: <input name='s7' type='text' value=%s> <br /> <br />" % (s7))
print("s8: <input name='s8' type='text' value=%s> <br /> <br />" % (s8))
print("h1: <input name='h1' type='text' value=%s> <br /> <br />" % (h1))
print("h2: <input name='h2' type='text' value=%s> <br /> <br />" % (h2))
print("h3: <input name='h3' type='text' value=%s> <br /> <br />" % (h3))
print("h4: <input name='h4' type='text' value=%s> <br /> <br />" % (h4))
print("h5: <input name='h5' type='text' value=%s> <br /> <br />" % (h5))
print("h6: <input name='h6' type='text' value=%s> <br /> <br />" % (h6))
print("ar1: <input name='ar1' type='text' value=%s> <br /> <br />" % (ar1))
print("ar2: <input name='ar2' type='text' value=%s> <br /> <br />" % (ar2))
print("p1: <input name='p1' type='text' value=%s> <br /> <br />" % (p1))
print("p2: <input name='p2' type='text' value=%s> <br /> <br />" % (p2))
print("<input type='submit' value='Solve'/> <br /> <br />")
print("</form>")
