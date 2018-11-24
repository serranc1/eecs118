import graphics
from graphics import*
import time
from time import*
import math
from math import*
import cgi
def set_value(name, value):
    name = value
def set_vertex(name, x, y):
    name = Point(x,y)
def get_value(name):
    return name
def get_all():
    return {a1, a2, a3, s1, s2, s3, s4, s5, s6, s7, h1, h2, h3, L1, L2, L3, L4, radius, diameter, circumference, p, art, arc, ar1}
def main():
    win = GraphWin("Problem Set R #1", 800, 500)
    ia1=Entry(Point(150,50),10)
    ia2=Entry(Point(150,75),10)
    ia3 = Entry(Point(150,100),10)
    is1 = Entry(Point(150,125),10)
    is2 = Entry(Point(150,150),10)
    is3 = Entry(Point(150,175),10)
    is4 = Entry(Point(150,200),10)
    is5 = Entry(Point(150,225),10)
    is6 = Entry(Point(150,250),10)
    is7 = Entry(Point(150,275),10)
    ih1 = Entry(Point(150,300),10)
    ih2 = Entry(Point(150,325),10)
    ih3 = Entry(Point(150,350),10)
    iL1 = Entry(Point(300,50),10)
    iL2 = Entry(Point(300,75),10)
    iL3 = Entry(Point(300,100),10)
    iradius = Entry(Point(300,125),10)
    idiameter = Entry(Point(300,150),10)
    icircumference = Entry(Point(300,175),10)
    ip = Entry(Point(300,200),10)
    iart = Entry(Point(300,225),10)
    iarc = Entry(Point(300,250),10)
    iar1 = Entry(Point(300,275),10)
    rect=Rectangle(Point(50,25),Point(750,450)).draw(win)
    ia1.draw(win)
    ia2.draw(win)
    ia3.draw(win)
    is1.draw(win)
    is2.draw(win)
    is3.draw(win)
    is4.draw(win)
    is5.draw(win)
    is6.draw(win)
    is7.draw(win)
    ih1.draw(win)
    ih2.draw(win)
    ih3.draw(win)
    iL1.draw(win)
    iL2.draw(win)
    iL3.draw(win)
    iradius.draw(win)
    idiameter.draw(win)
    icircumference.draw(win)
    ip.draw(win)
    iart.draw(win)
    iarc.draw(win)
    iar1.draw(win)
    Text(Point(80,50),"a1").draw(win)
    Text(Point(80,75),"a2").draw(win)
    Text(Point(80,100),"a3").draw(win)
    Text(Point(80,125),"s1").draw(win)
    Text(Point(80,150),"s2").draw(win)
    Text(Point(80,175),"s3").draw(win)
    Text(Point(80,200),"s4").draw(win)
    Text(Point(80,225),"s5").draw(win)
    Text(Point(80,250),"s6").draw(win)
    Text(Point(80,275),"s7").draw(win)
    Text(Point(80,300),"h1").draw(win)
    Text(Point(80,325),"h2").draw(win)
    Text(Point(80,350),"h3").draw(win)
    Text(Point(230,50),"L1").draw(win)
    Text(Point(230,75),"L2").draw(win)
    Text(Point(230,100),"L3").draw(win)
    Text(Point(230,125),"r").draw(win)
    Text(Point(230,150),"d").draw(win)
    Text(Point(230,175),"c").draw(win)
    Text(Point(230,200),"p").draw(win)
    Text(Point(230,225),"art").draw(win)
    Text(Point(230,250),"arc").draw(win)
    Text(Point(230,275),"ar1").draw(win)
    Solve=Rectangle(Point(650,100),Point(725,125)).draw(win)
    Quit=Rectangle(Point(650,150),Point(725,175)).draw(win)
    Text(Point(675,112.5),"Solve").draw(win)
    Text(Point(675,162.5),"Quit").draw(win)
    Text(Point(400,10),"Input values to solve:").draw(win)
    diagram = Image(Point(500,200),"P1.png")
    diagram.draw(win)
    x=1
    while(x==1):
        response=win.getMouse()
        #if pressed solve
        if 650 <= response.getX()<= 725 and 100 <= response.getY()<= 125:
            a1=ia1.getText()
            a2=ia2.getText()
            a3=ia3.getText()
            s1=is1.getText()
            s2=is2.getText()
            s3=is3.getText()
            s4=is4.getText()
            s5=is5.getText()
            s6=is6.getText()
            s7=is7.getText()
            h1=ih1.getText()
            h2=ih2.getText()
            h3=ih3.getText()
            L1=iL1.getText()
            L2=iL2.getText()
            L3=iL3.getText()
            L4=iL4.getText()
            radius=iradius.getText()
            diameter=idiameter.getText()
            circumference=icircumference.getText()
            p=ip.getText()
            art=iart.getText()
            arc=iarc.getText()
            ar1=iar1.getText()
            ar2=iar2.getText()
            ar3=iar3.getText()
##            set_value(a1,ia1.getText())
##            set_value(a2,ia2.getText())
##            set_value(a3,ia3.getText())
##            set_value(a4,ia1.getText())
##            set_value(a5,ia2.getText())
##            set_value(a6,ia3.getText())
##            set_value(a7,ia1.getText())
##            set_value(a8,ia2.getText())
##            set_value(s1,ia3.getText())
##            set_value(s2,ia1.getText())
##            set_value(s3,ia2.getText())
##            set_value(s4,ia3.getText())
##            set_value(s5,ia1.getText())
##            set_value(s6,ia2.getText())
##            set_value(s7,ia3.getText())
##            set_value(ar1,iar1.getText())
##            set_value(ar2,iar2.getText())
##            set_value(p1,ip1.getText())
##            set_value(p2,ip2.getText())
##            set_value(h1,ih1.getText())
##            set_value(h2,ih2.getText())
##            set_value(h3,ih3.getText())
##            set_value(h4,ih4.getText())
##            set_value(h5,ih5.getText())
##            set_value(h6,ih6.getText())
            
            #SSS
            if s1 != '' and s2 != '' and s3 != '' and a1 == '' and a2 == '' and a3 == '':
                a1 = round(math.degrees(math.acos(round((math.pow(float(s2),2) + math.pow(float(s3),2) - math.pow(float(s1),2))/(2*float(s2)*float(s3)),2))),2)
                a2 = round(math.degrees(math.acos(round((math.pow(float(s1),2) + math.pow(float(s3),2) - math.pow(float(s2),2))/(2*float(s1)*float(s3)),2))),2)
                a3 = 180 - round(float(a1),2) - round(float(a2),2)
                ia1.setText(a1)
                ia2.setText(a2)
                ia3.setText(a3)
            if s4 != '' and s5 != '' and s6 != '' and a4 == '' and a5 == '' and a6 == '':
                a4 = round(math.degrees(math.acos(round((math.pow(float(s5),2) + math.pow(float(s6),2) - math.pow(float(s4),2))/(2*float(s5)*float(s6)),2))),2)
                a5 = round(math.degrees(math.acos(round((math.pow(float(s4),2) + math.pow(float(s6),2) - math.pow(float(s5),2))/(2*float(s4)*float(s6)),2))),2)
                a6 = 180 - round(float(a4),2) - round(float(a5),2)
                ia4.setText(a4)
                ia5.setText(a5)
                ia6.setText(a6)
            #AAS
            #solve for angle given two others
            if a2 != '' and a3 != '' and a1 == '':
                a1 = 180 - round(float(a2),2) - round(float(a3),2)
                ia1.setText(a1)
            if a1 != '' and a3 != '' and a2 == '':
                a2 = 180 - round(float(a1),2) - round(float(a3),2)
                ia2.setText(a2)
            if a1 != '' and a2 != '' and a3 == '':
                a3 = 180 - round(float(a1),2) - round(float(a2),2)
                ia3.setText(a3)
            #solve for the sides
            if s1 != '' and s2 == '' and s3 == '':
                s2 = round(math.sin(math.radians(float(a2)))*float(s1)/math.sin(math.radians(float(a1))),2)
                s3 = round(math.sin(math.radians(float(a3)))*float(s1)/math.sin(math.radians(float(a1))),2)
                is2.setText(s2)
                is3.setText(s3)
            if s2 != '' and s1 == '' and s3 == '':
                s1 = round(math.sin(math.radians(float(a1)))*float(s2)/math.sin(math.radians(float(a2))),2)
                s3 = round(math.sin(math.radians(float(a3)))*float(s2)/math.sin(math.radians(float(a2))),2)
                is1.setText(s1)
                is3.setText(s3)
            if s3 != '' and s1 == '' and s2 == '':
                s1 = round(math.sin(math.radians(float(a1)))*float(s3)/math.sin(math.radians(float(a3))),2)
                s2 = round(math.sin(math.radians(float(a2)))*float(s3)/math.sin(math.radians(float(a3))),2)
                is1.setText(s1)
                is2.setText(s2)
            #ASA
            #solve for angle given two others
            if a2 != '' and a3 != '' and a1 == '':
                a1 = 180 - round(float(a2),2) - round(float(a3),2)
                ia1.setText(a1)
            if a1 != '' and a3 != '' and a2 == '':
                a2 = 180 - round(float(a1),2) - round(float(a3),2)
                ia2.setText(a2)
            if a1 != '' and a2 != '' and a3 == '':
                a3 = 180 - round(float(a1),2) - round(float(a2),2)
                ia3.setText(a3)
            #solve for the sides
            if s1 != '' and s2 == '' and s3 == '':
                s2 = math.sin(math.radians(float(a2)))*float(s1)/math.sin(math.radians(float(a1)))
                s3 = math.sin(math.radians(float(a3)))*float(s1)/math.sin(math.radians(float(a1)))
                is2.setText(s2)
                is3.setText(s3)
            if s2 != '' and s1 == '' and s3 == '':
                s1 = math.sin(math.radians(float(a1)))*float(s2)/math.sin(math.radians(float(a2)))
                s3 = math.sin(math.radians(float(a3)))*float(s2)/math.sin(math.radians(float(a2)))
                is1.setText(s1)
                is3.setText(s3)
            if s3 != '' and s1 == '' and s2 == '':
                s1 = math.sin(math.radians(float(a1)))*float(s3)/math.sin(math.radians(float(a3)))
                s2 = math.sin(math.radians(float(a2)))*float(s3)/math.sin(math.radians(float(a3)))
                is1.setText(s1)
                is2.setText(s2)
            #SAS
            if a1 != '' and a2 == '' and a3 == '' and s1 == '' and s2 != '' and s3 != '':
                s1 = round(math.sqrt(math.pow(float(s2),2)+math.pow(float(s3),2)-2*float(s2)*float(s3)*math.cos(math.radians(float(a1)))),2)
                is1.setText(s1)
                if float(s2) > float(s3):
                    a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
                    a2 = 180 - float(a1) - float(a3)
                    ia2.setText(a2)
                    ia3.setText(a3)
                if float(s2) < float(s3):
                    a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
                    a3 = 180 - float(a1) - float(a2)
                    ia2.setText(a2)
                    ia3.setText(a3)
            if a2 != '' and s1 == '' and s3 == '' and s1 != '' and s3 != '' and s2 == '':
                s2 = math.sqrt(math.pow(float(s1),2)+math.pow(float(s3),2)-2*float(s1)*float(s3)*math.cos(math.radians(float(a2))))
                is2.setText(s2)
                if float(s1) > float(s3):
                    a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a2)))/float(s2),2))),2)
                    a1 = 180 - float(a2) - float(a3)
                    ia1.setText(a1)
                    ia3.setText(a3)
                if float(s1) < float(s3):
                    a1 = math.degrees(math.asin(float(s1)*math.sin(math.radians(float(a2)))/float(s2)))
                    a3 = 180 - float(a1) - float(a2)
                    ia1.setText(a1)
                    ia3.setText(a3)
            if a3 != '' and s1 == '' and s2 == '' and s1 != '' and s2 != '' and s3 == '':
                s3 = math.sqrt(math.pow(float(s1),2)+math.pow(float(s2),2)-2*float(s1)*float(s2)*math.cos(math.radians(float(a3))))
                is3.setText(s3)
                if float(s1) > float(s2):
                    a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a3)))/float(s3),2))),2)
                    a1 = 180 - float(a2) - float(a3)
                    ia1.setText(a1)
                    ia2.setText(a2)
                if float(s1) < float(s2):
                    a1 = round(math.degrees(math.asin(round(float(s1)*math.sin(math.radians(float(a3)))/float(s3),2))),2)
                    a2 = 180 - float(a1) - float(a3)
                    ia1.setText(a1)
                    ia2.setText(a2)
            #SSA
            #a1 is known
            if a1 != '' and a2 == '' and a3 == '' and s1 != '' and s3 != '' and s2 == '':
                a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
                a2 = 180 - float(a1) - float(a3)
                ia3.setText(a3)
                ia2.setText(a2)
            if a1 != '' and a2 == '' and a3 == '' and s1 != '' and s2 != '' and s3 == '':
                a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
                a3 = 180 - float(a1) - float(a2)
                ia3.setText(a3)
                ia2.setText(a2)
            #a2 is known
            if a2 != '' and a1 == '' and a3 == '' and s1 != '' and s2 != '' and s3 == '':
                a1 = round(math.degrees(math.asin(round(float(s1)*math.sin(math.radians(float(a2)))/float(s2),2))),2)
                a3 = 180 - float(a1) - float(a2)
                ia3.setText(a3)
                ia1.setText(a1)
            if a2 != '' and a1 == '' and a3 == '' and s2 != '' and s3 != '' and s1 == '':
                a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a2)))/float(s2),2))),2)
                a1 = 180 - float(a2) - float(a3)
                ia3.setText(a3)
                ia1.setText(a1)
            #a3 is known
            if a3 != '' and a1 == '' and a2 == '' and s2 != '' and s3 != '' and s1 == '':
                a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a3)))/float(s3),2))),2)
                a1 = 180 - float(a2) - float(a3)
                ia2.setText(a2)
                ia1.setText(a1)
            if a3 != '' and a1 == '' and a2 == '' and s1 != '' and s3 != '' and s2 == '':
                a1 = round(math.degrees(math.asin(round(float(s1)*math.sin(math.radians(float(a3)))/float(s3),2))),2)
                a2 = 180 - float(a1) - float(a3)
                ia2.setText(a2)
                ia1.setText(a1)
            
            
            #solving for perimeter
            if s1 != '' and s2 != '' and s3 != '':
                p = float(s1) + float(s2) + float(s3)
                ip.setText(p)

            #solving for heights
            #given one angle and 90 degrees, do AAS
            if a2 != '' and s3 != '':
                h1 = round(round(float(s3),2)*math.sin(round(math.radians(float(a2)),2)),2)
                ih1.setText(h1)
            if a3 != '' and s2 != '':
                h1 = round(round(float(s2),2)*math.sin(round(math.radians(float(a3)),2)),2)
                ih1.setText(h1)
            if a1 != '' and s3 != '':
                h2 = round(round(float(s3),2)*math.sin(round(math.radians(float(a1)),2)),2)
                ih2.setText(h2)
            if a3 != '' and s1 != '':
                h2 = round(round(float(s1),2)*math.sin(round(math.radians(float(a3)),2)),2)
                ih2.setText(h2)
            if a1 != '' and s2 != '':
                h3 = round(round(float(s2),2)*math.sin(round(math.radians(float(a1)),2)),2)
                ih3.setText(h3)
            if a2 != '' and s1 != '':
                h3 = round(round(float(s1),2)*math.sin(round(math.radians(float(a2)),2)),2)
                ih3.setText(h3)
            #given area
            if art != '' and s1 != '':
                h1 = 2 * round(float(art),2)/round(float(s1),2)
                ih1.setText(h1)
            if art != '' and s2 != '':
                h2 = 2 * round(float(art),2)/round(float(s2),2)
                ih2.setText(h2)
            if art != '' and s3 != '':
                h3 = 2 * round(float(art),2)/round(float(s3),2)
                ih3.setText(h3)
                
            #solving for area of triangle
            if s1 != '' and h1 != '' and art == '':
                art = 0.5 * round(float(s1),2) * round(float(h1),2)
                iart.setText(art)
            if s2 != '' and h2 != '' and art == '':
                ar1 = 0.5 * round(float(s2),2) * round(float(h2),2)
                iart.setText(art)
            if s3 != '' and h3 != '' and art == '':
                art = 0.5 * round(float(s3),2) * round(float(h3),2)
                iart.setText(art)

            #solving for s4, s5, s6, s7
            if s2 != '' and s7 != '':
                s6 = round(float(s2),2) - round(float(s7),2)
                is6.setText(s6)
            if s2 != '' and s6 != '':
                s7 = round(float(s2),2) - round(float(s6),2)
                is7.setText(s7)
            if s1 != '' and s5 != '':
                s4 = round(float(s1),2) - round(float(s5),2)
                is6.setText(s6)
            if s1 != '' and s4 != '':
                s5 = round(float(s1),2) - round(float(s4),2)
                is5.setText(s5)
            
            #solving for radius and diameter
            if diameter != '' and radius == '':
                radius = round((float(diameter)/2),2)
                iradius.setText(radius)
            if diameter == '' and radius != '':
                diameter = round((float(radius)*2),2)
                idiameter.setText(diameter)
            if arc != '' and diameter == '' and radius == '':
                radius = round(math.sqrt(float(arc)/math.pi),2)
                diameter = round((float(radius)*2),2)
                iradius.setText(radius)
                idiameter.setText(diameter)

            #solving for area of circle
            if diameter != '' and radius == '':
                radius = round((float(diameter)/2),2)
                iradius.setText(radius)
            if radius != '':
                arc = round((math.pi * math.pow(round(float(radius),2),2)),2)
                iarc.setText(arc)
            
            #solving for arc lengths
            if L2 != '' and L3 != '' and circumference != '':
                L1 = round(float(circumference),2) - round(float(L2),2) - round(float(L3),2)
            if L1 != '' and L3 != '' and circumference != '':
                L2 = round(float(circumference),2) - round(float(L1),2) - round(float(L3),2)
            if L1 != '' and L2 != '' and circumference != '':
                L3 = round(float(circumference),2) - round(float(L1),2) - round(float(L2),2)

            #solving for circular segment areas
            if radius != '' and s6 != '':
                continue
        #if pressed quit
        if 650 <= response.getX()<= 725 and 150 <= response.getY()<= 175:       
            x=0

    
    win.close()
print("GUI currently not integrated with web interface.")
main()
