import graphics
from graphics import*
import time
from time import*
import math
from math import*
def set_value(name, value):
    name = value
def set_vertex(name, x, y):
    name = Point[x,y]
def get_value(name):
    return name
def get_all():
    return {a1, a2, a3, a4, a5, a6, a7, a8, s1, s2, s3, s4, s5, s6, s7, s8, ar1, ar2}
def main():
    win = GraphWin("Problem Set R #3", 800, 500)
    ia1=Entry(Point(150,50),10)
    ia2=Entry(Point(150,75),10)
    ia3 = Entry(Point(150,100),10)
    ia4 = Entry(Point(150,125),10)
    ia5 = Entry(Point(150,150),10)
    ia6 = Entry(Point(150,175),10)
    ia7 = Entry(Point(150,200),10)
    ia8 = Entry(Point(150,225),10)
    iar1 = Entry(Point(150,250),10)
    iar2 = Entry(Point(150,275),10)
    ip1 = Entry(Point(150,300),10)
    ip2 = Entry(Point(150,325),10)
    is1 = Entry(Point(300,50),10)
    is2 = Entry(Point(300,75),10)
    is3 = Entry(Point(300,100),10)
    is4 = Entry(Point(300,125),10)
    is5 = Entry(Point(300,150),10)
    is6 = Entry(Point(300,175),10)
    is7 = Entry(Point(300,200),10)
    is8 = Entry(Point(300,225),10)
    ih1 = Entry(Point(300,250),10)
    ih2 = Entry(Point(300,275),10)
    ih3 = Entry(Point(300,300),10)
    ih4 = Entry(Point(300,325),10)
    ih5 = Entry(Point(300,350),10)
    ih6 = Entry(Point(300,375),10)
    rect=Rectangle(Point(50,25),Point(750,450)).draw(win)
    ia1.draw(win)
    ia2.draw(win)
    ia3.draw(win)
    ia4.draw(win)
    ia5.draw(win)
    ia6.draw(win)
    ia7.draw(win)
    ia8.draw(win)
    is1.draw(win)
    is2.draw(win)
    is3.draw(win)
    is4.draw(win)
    is5.draw(win)
    is6.draw(win)
    is7.draw(win)
    is8.draw(win)
    iar1.draw(win)
    iar2.draw(win)
    ip1.draw(win)
    ip2.draw(win)
    ih1.draw(win)
    ih2.draw(win)
    ih3.draw(win)
    ih4.draw(win)
    ih5.draw(win)
    ih6.draw(win)
    Text(Point(80,50),"a1").draw(win)
    Text(Point(80,75),"a2").draw(win)
    Text(Point(80,100),"a3").draw(win)
    Text(Point(80,125),"a4").draw(win)
    Text(Point(80,150),"a5").draw(win)
    Text(Point(80,175),"a6").draw(win)
    Text(Point(80,200),"a7").draw(win)
    Text(Point(80,225),"a8").draw(win)
    Text(Point(80,250),"ar1").draw(win)
    Text(Point(80,275),"ar2").draw(win)
    Text(Point(80,300),"p1").draw(win)
    Text(Point(80,325),"p2").draw(win)
    Text(Point(230,50),"s1").draw(win)
    Text(Point(230,75),"s2").draw(win)
    Text(Point(230,100),"s3").draw(win)
    Text(Point(230,125),"s4").draw(win)
    Text(Point(230,150),"s5").draw(win)
    Text(Point(230,175),"s6").draw(win)
    Text(Point(230,200),"s7").draw(win)
    Text(Point(230,225),"s8").draw(win)
    Text(Point(230,250),"h1").draw(win)
    Text(Point(230,275),"h2").draw(win)
    Text(Point(230,300),"h3").draw(win)
    Text(Point(230,325),"h4").draw(win)
    Text(Point(230,350),"h5").draw(win)
    Text(Point(230,375),"h6").draw(win)
    Solve=Rectangle(Point(650,100),Point(725,125)).draw(win)
    Quit=Rectangle(Point(650,150),Point(725,175)).draw(win)
    Text(Point(675,112.5),"Solve").draw(win)
    Text(Point(675,162.5),"Quit").draw(win)
    Text(Point(400,10),"Input values to solve:").draw(win)
    x=1
    while(x==1):
        response=win.getMouse()
        #if pressed solve
        if 650 <= response.getX()<= 725 and 100 <= response.getY()<= 125:
            a1=ia1.getText()
            a2=ia2.getText()
            a3=ia3.getText()
            a4=ia4.getText()
            a5=ia5.getText()
            a6=ia6.getText()
            a7=ia7.getText()
            a8=ia8.getText()
            s1=is1.getText()
            s2=is2.getText()
            s3=is3.getText()
            s4=is4.getText()
            s5=is5.getText()
            s6=is6.getText()
            s7=is7.getText()
            s8=is8.getText()
            h1=ih1.getText()
            h2=ih2.getText()
            h3=ih3.getText()
            h4=ih4.getText()
            h5=ih5.getText()
            h6=ih6.getText()
            ar1=iar1.getText()
            ar2=iar2.getText()
            p1=ip1.getText()
            p2=ip2.getText()
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
##            #check for invalid input values
##            if float(a1) + float(a2) + float(a3) != 180:
##                print('Invalid combination of angle values')
            
            #SSS
            if s1 != '' and s2 != '' and s3 != '':
                a1 = round(math.degrees(math.acos(round((math.pow(float(s2),2) + math.pow(float(s3),2) - math.pow(float(s1),2))/(2*float(s2)*float(s3)),2))),2)
                a2 = round(math.degrees(math.acos(round((math.pow(float(s1),2) + math.pow(float(s3),2) - math.pow(float(s2),2))/(2*float(s1)*float(s3)),2))),2)
                a3 = 180 - round(float(a1),2) - round(float(a2),2)
                ia1.setText(a1)
                ia2.setText(a2)
                ia3.setText(a3)
            if s4 != '' and s5 != '' and s6 != '':
                a4 = round(math.degrees(math.acos(round((math.pow(float(s5),2) + math.pow(float(s6),2) - math.pow(float(s4),2))/(2*float(s5)*float(s6)),2))),2)
                a5 = round(math.degrees(math.acos(round((math.pow(float(s4),2) + math.pow(float(s6),2) - math.pow(float(s5),2))/(2*float(s4)*float(s6)),2))),2)
                a6 = 180 - round(float(a4),2) - round(float(a5),2)
                ia4.setText(a4)
                ia5.setText(a5)
                ia6.setText(a6)
            #AAS
            #Triangle 1
            #solve for angle given two others
            if a2 != '' and a3 != '':
                a1 = 180 - round(float(a2),2) - round(float(a3),2)
                ia1.setText(a1)
            if a1 != '' and a3 != '':
                a2 = 180 - round(float(a1),2) - round(float(a3),2)
                ia2.setText(a2)
            if a1 != '' and a2 != '':
                a3 = 180 - round(float(a1),2) - round(float(a2),2)
                ia3.setText(a3)
            #solve for the sides
            if s1 != '':
                s2 = round(math.sin(math.radians(float(a2)))*float(s1)/math.sin(math.radians(float(a1))),2)
                s3 = round(math.sin(math.radians(float(a3)))*float(s1)/math.sin(math.radians(float(a1))),2)
                is2.setText(s2)
                is3.setText(s3)
            if s2 != '':
                s1 = round(math.sin(math.radians(float(a1)))*float(s2)/math.sin(math.radians(float(a2))),2)
                s3 = round(math.sin(math.radians(float(a3)))*float(s2)/math.sin(math.radians(float(a2))),2)
                is1.setText(s1)
                is3.setText(s3)
            if s3 != '':
                s1 = round(math.sin(math.radians(float(a1)))*float(s3)/math.sin(math.radians(float(a3))),2)
                s2 = round(math.sin(math.radians(float(a2)))*float(s3)/math.sin(math.radians(float(a3))),2)
                is1.setText(s1)
                is2.setText(s2)
            #Triangle 2
            #solve for angle given two others
            if a5 != '' and a6 != '':
                a4 = 180 - round(float(a5),2) - round(float(a6),2)
                ia4.setText(a4)
            if a4 != '' and a6 != '':
                a5 = 180 - round(float(a4),2) - round(float(a6),2)
                ia5.setText(a5)
            if a4 != '' and a5 != '':
                a6 = 180 - round(float(a4),2) - round(float(a5),2)
                ia6.setText(a6)
            #solve for the sides
            if s4 != '':
                s5 = math.sin(math.radians(float(a5)))*float(s4)/math.sin(math.radians(float(a4)))
                s6 = math.sin(math.radians(float(a6)))*float(s4)/math.sin(math.radians(float(a4)))
                is5.setText(s5)
                is6.setText(s6)
            if s5 != '':
                s4 = math.sin(math.radians(float(a4)))*float(s5)/math.sin(math.radians(float(a5)))
                s6 = math.sin(math.radians(float(a6)))*float(s5)/math.sin(math.radians(float(a5)))
                is4.setText(s4)
                is6.setText(s6)
            if s6 != '':
                s4 = math.sin(math.radians(float(a4)))*float(s6)/math.sin(math.radians(float(a6)))
                s5 = math.sin(math.radians(float(a5)))*float(s6)/math.sin(math.radians(float(a6)))
                is4.setText(s4)
                is5.setText(s5)
            #ASA
            #Triangle 1
            #solve for angle given two others
            if a2 != '' and a3 != '':
                a1 = 180 - round(float(a2),2) - round(float(a3),2)
                ia1.setText(a1)
            if a1 != '' and a3 != '':
                a2 = 180 - round(float(a1),2) - round(float(a3),2)
                ia2.setText(a2)
            if a1 != '' and a2 != '':
                a3 = 180 - round(float(a1),2) - round(float(a2),2)
                ia3.setText(a3)
            #solve for the sides
            if s1 != '':
                s2 = math.sin(math.radians(float(a2)))*float(s1)/math.sin(math.radians(float(a1)))
                s3 = math.sin(math.radians(float(a3)))*float(s1)/math.sin(math.radians(float(a1)))
                is2.setText(s2)
                is3.setText(s3)
            if s2 != '':
                s1 = math.sin(math.radians(float(a1)))*float(s2)/math.sin(math.radians(float(a2)))
                s3 = math.sin(math.radians(float(a3)))*float(s2)/math.sin(math.radians(float(a2)))
                is1.setText(s1)
                is3.setText(s3)
            if s3 != '':
                s1 = math.sin(math.radians(float(a1)))*float(s3)/math.sin(math.radians(float(a3)))
                s2 = math.sin(math.radians(float(a2)))*float(s3)/math.sin(math.radians(float(a3)))
                is1.setText(s1)
                is2.setText(s2)
            #Triangle 2
            #solve for angle given two others
            if a5 != '' and a6 != '':
                a4 = 180 - round(float(a5),2) - round(float(a6),2)
                ia4.setText(a4)
            if a4 != '' and a6 != '':
                a5 = 180 - round(float(a4),2) - round(float(a6),2)
                ia5.setText(a5)
            if a4 != '' and a5 != '':
                a6 = 180 - round(float(a4),2) - round(float(a5),2)
                ia6.setText(a6)
            #solve for the sides
            if s4 != '':
                s5 = math.sin(math.radians(float(a5)))*float(s4)/math.sin(math.radians(float(a4)))
                s6 = math.sin(math.radians(float(a6)))*float(s4)/math.sin(math.radians(float(a4)))
                is5.setText(s5)
                is6.setText(s6)
            if s5 != '':
                s4 = math.sin(math.radians(float(a4)))*float(s5)/math.sin(math.radians(float(a5)))
                s6 = math.sin(math.radians(float(a6)))*float(s5)/math.sin(math.radians(float(a5)))
                is4.setText(s4)
                is6.setText(s6)
            if s6 != '':
                s4 = math.sin(math.radians(float(a4)))*float(s6)/math.sin(math.radians(float(a6)))
                s5 = math.sin(math.radians(float(a5)))*float(s6)/math.sin(math.radians(float(a6)))
                is4.setText(s4)
                is5.setText(s5)
            #SAS
            #Triangle 1
            if a1 != '' and s2 != '' and s3 != '':
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
            if a2 != '' and s1 != '' and s3 != '':
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
            if a3 != '' and s1 != '' and s2 != '':
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
            #Triangle 2
            if a4 != '' and s5 != '' and s6 != '':
                s4 = round(math.sqrt(math.pow(float(s5),2)+math.pow(float(s6),2)-2*float(s5)*float(s6)*math.cos(math.radians(float(a4)))),2)
                is4.setText(s4)
                if float(s5) > float(s6):
                    a6 = round(math.degrees(math.asin(round(float(s6)*math.sin(math.radians(float(a4)))/float(s4),2))),2)
                    a5 = 180 - float(a4) - float(a6)
                    ia5.setText(s5)
                    ia6.setText(s6)
                if float(s5) < float(s6):
                    a5 = round(math.degrees(math.asin(round(float(s5)*math.sin(math.radians(float(a4)))/float(s4),2))),2)
                    a6 = 180 - float(a4) - float(a5)
                    ia5.setText(a5)
                    ia6.setText(a6)
            if a5 != '' and s4 != '' and s6 != '':
                s5 = round(math.sqrt(math.pow(float(s4),2)+math.pow(float(s6),2)-2*float(s4)*float(s6)*math.cos(math.radians(float(a5)))),2)
                is5.setText(s5)
                if float(s4) > float(s6):
                    a6 = round(math.degrees(math.asin(round(float(s6)*math.sin(math.radians(float(a5)))/float(s5),2))),2)
                    a4 = 180 - float(a5) - float(a6)
                    ia4.setText(a4)
                    ia6.setText(a6)
                if float(s4) < float(s6):
                    a4 = round(math.degrees(math.asin(round(float(s4)*math.sin(math.radians(float(a5)))/float(s5),2))),2)
                    a6 = 180 - float(a4) - float(a5)
                    ia4.setText(a4)
                    ia6.setText(a6)
            if a6 != '' and s4 != '' and s5 != '':
                s6 = round(math.sqrt(math.pow(float(s4),2)+math.pow(float(s5),2)-2*float(s4)*float(s5)*math.cos(math.radians(float(a6)))),2)
                is6.setText(s6)
                if float(s4) > float(s5):
                    a5 = round(math.degrees(math.asin(round(float(s5)*math.sin(math.radians(float(a6)))/float(s6),2))),2)
                    a4 = 180 - float(a5) - float(a6)
                    ia4.setText(a4)
                    ia5.setText(a5)
                if float(s4) < float(s5):
                    a4 = round(math.degrees(math.asin(round(float(s4)*math.sin(math.radians(float(a6)))/float(s6),2))),2)
                    a5 = 180 - float(a4) - float(a6)
                    ia4.setText(a4)
                    ia5.setText(a5)
            #SSA
            #Triangle 1
            #a1 is known
            if a1 != '' and s1 != '' and s3 != '':
                a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
                a2 = 180 - float(a1) - float(a3)
                ia3.setText(a3)
                ia2.setText(a2)
            if a1 != '' and s1 != '' and s2 != '':
                a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a1)))/float(s1),2))),2)
                a3 = 180 - float(a1) - float(a2)
                ia3.setText(a3)
                ia2.setText(a2)
            #a2 is known
            if a2 != '' and s1 != '' and s2 != '':
                a1 = round(math.degrees(math.asin(round(float(s1)*math.sin(math.radians(float(a2)))/float(s2),2))),2)
                a3 = 180 - float(a1) - float(a2)
                ia3.setText(a3)
                ia1.setText(a1)
            if a2 != '' and s2 != '' and s3 != '':
                a3 = round(math.degrees(math.asin(round(float(s3)*math.sin(math.radians(float(a2)))/float(s2),2))),2)
                a1 = 180 - float(a2) - float(a3)
                ia3.setText(a3)
                ia1.setText(a1)
            #a3 is known
            if a3 != '' and s2 != '' and s3 != '':
                a2 = round(math.degrees(math.asin(round(float(s2)*math.sin(math.radians(float(a3)))/float(s3),2))),2)
                a1 = 180 - float(a2) - float(a3)
                ia2.setText(a2)
                ia1.setText(a1)
            if a3 != '' and s1 != '' and s3 != '':
                a1 = round(math.degrees(math.asin(round(float(s1)*math.sin(math.radians(float(a3)))/float(s3),2))),2)
                a2 = 180 - float(a1) - float(a3)
                ia2.setText(a2)
                ia1.setText(a1)
            #Triangle 2
            #a4 is known
            if a4 != '' and s4 != '' and s5 != '':
                a5 = round(math.degrees(math.asin(round(float(s5)*math.sin(math.radians(float(a4)))/float(s4),2))),2)
                a6 = 180 - float(a4) - float(a5)
                ia5.setText(a5)
                ia6.setText(a6)
            if a4 != '' and s4 != '' and s6 != '':
                a6 = round(math.degrees(math.asin(round(float(s6)*math.sin(math.radians(float(a4)))/float(s4),2))),2)
                a5 = 180 - float(a4) - float(a6)
                ia5.setText(a5)
                ia6.setText(a6)
            #a5 is known
            if a5 != '' and s4 != '' and s5 != '':
                a4 = round(math.degrees(math.asin(round(float(s4)*math.sin(math.radians(float(a5)))/float(s5),2))),2)
                a6 = 180 - float(a4) - float(a5)
                ia4.setText(a4)
                ia6.setText(a6)
            if a5 != '' and s5 != '' and s6 != '':
                a6 = round(math.degrees(math.asin(round(float(s6)*math.sin(math.radians(float(a5)))/float(s5),2))),2)
                a4 = 180 - float(a5) - float(a6)
                ia4.setText(a4)
                ia6.setText(a6)
            #a6 is known    
            if a6 != '' and s4 != '' and s6 != '':
                a4 = round(math.degrees(math.asin(round(float(s4)*math.sin(math.radians(float(a6)))/float(s6),2))),2)
                a5 = 180 - float(a4) - float(a6)
                ia4.setText(a4)
                ia5.setText(a5)
            if a6 != '' and s5 != '' and s6 != '':
                a5 = round(math.degrees(math.asin(round(float(s5)*math.sin(math.radians(float(a6)))/float(s6),2))),2)
                a4 = 180 - float(a4) - float(a5)
                ia4.setText(a4)
                ia5.setText(a5)
            
            
            #solving for perimeter
            if s1 != '' and s2 != '' and s3 != '':
                p1 = float(s1) + float(s2) + float(s3)
                ip1.setText(p1)
            if s4 != '' and s5 != '' and s6 != '':
                p2 = float(s4) + float(s5) + float(s6)
                ip2.setText(p2)
            
            
            
        #if pressed quit
        if 650 <= response.getX()<= 725 and 150 <= response.getY()<= 175:       
            x=0

    
    win.close()
main()
