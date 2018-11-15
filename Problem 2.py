import graphics
from graphics import*
import time
from time import*
def set_value(name, value):
    name = value
def set_vertex(name, x, y):
    name = [x,y]
def get_value(name):
    return name
def get_all():
    return {a1, a2, a3, s1, s2, s3, s4, s5, s6, L1, L2, L3, L4, r1, ar1, ar2}
def main():
    win = GraphWin("Problem Set R #2", 800, 500)
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
            
            if a1 == '' and a2 != '' and a3 != '':
                a1 = 180 - int(a2) - int(a3)
                ia1.setText(a1)
            if a2 == ''  and a1 != ''  and a3 != '':
                a2 = 180 - int(a1) - int(a3)
                ia2.setText(a2)
            if a3 == '' and a1 != '' and a2 != '':
                a3 = 180 - int(a1) - int(a2)
                ia3.setText(a3)
            if a4 == '' and a5 != '' and a6 != '':
                a4 = 180 - int(a5) - int(a6)
                ia4.setText(a4)
            if a5 == '' and a4 != '' and a6 != '':
                a5 = 180 - int(a4) - int(a6)
                ia5.setText(a5)
            if a6 == '' and a4 != '' and a5 != '':
                a6 = 180 - int(a4) - int(a5)
                ia6.setText(a6)
            if int(a1) == 90 or int(a2) == 90 or int(a3) == 90:
                if s1 == '' and s2 != '' and s3 != '':
                    s1 = math.sqrt(math.pow(int(s2),2) + math.pow(int(s3),2))
                    is1.setText(s1)
                if s2 == '' and s1 != '' and s3 != '':
                    s2 = math.sqrt(math.pow(int(s1),2) + math.pow(int(s3),2))
                    is2.setText(s2)
                if s3 == '' and s1 != '' and s2 != '':
                    s3 = math.sqrt(math.pow(int(s1),2) + math.pow(int(s2),2))
                    is3.setText(s3)
                    
            if int(a4) == 90 or int(a5) == 90 or int(a6) == 90:
                if s4 == '' and s5 != '' and s6 != '':
                    s4 = math.sqrt(math.pow(int(s5),2) + math.pow(int(s6),2))
                    is4.setText(s4)
                if s5 == '' and s4 != '' and s6 != '':
                    s5 = math.sqrt(math.pow(int(s4),2) + math.pow(int(s6),2))
                    is5.setText(s5)
                if s6 == '' and s4 != '' and s5 != '':
                    s6 = math.sqrt(math.pow(int(s4),2) + math.pow(int(s5),2))
                    is6.setText(s6)
            
            if s1 != '' and s2 != '' and s3 != '':
                p1 = int(s1) + int(s2) + int(s3)
                ip1.setText(p1)
            if s4 != '' and s5 != '' and s6 != '':
                p2 = int(s4) + int(s5) + int(s6)
                ip2.setText(p2)
            
            
        #if pressed quit
        if 650 <= response.getX()<= 725 and 150 <= response.getY()<= 175:       
            x=0

    

    win.close()
main()
