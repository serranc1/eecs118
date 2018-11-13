import graphics
from graphics import*
import time
from time import*
def set_value(name, value):
    name = value
def set_vertex(name, x, y):
    name = Point[x,y]
def get_value(name):
    return name
def get_all():
    return {a1, a2, a3, a4, a5, a6, a7, a8, s1, s2, s3, s4, s5, s6, s7, s8, ar1, ar2}
def main():
    a1 = 0.0
    a2 = 0.0
    a3 = 0.0
    a4 = 0.0
    a5 = 0.0
    a6 = 0.0
    a7 = 0.0
    a8 = 0.0
    s1 = 0.0
    s2 = 0.0
    s3 = 0.0
    s4 = 0.0
    s5 = 0.0
    s6 = 0.0
    s7 = 0.0
    s8 = 0.0
    ar1 = 0.0
    ar2 = 0.0
    p1 = 0.0
    p2 = 0.0
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
    is1=Entry(Point(300,50),10)
    is2=Entry(Point(300,75),10)
    is3 = Entry(Point(300,100),10)
    is4 = Entry(Point(300,125),10)
    is5 = Entry(Point(300,150),10)
    is6 = Entry(Point(300,175),10)
    is7 = Entry(Point(300,200),10)
    is8 = Entry(Point(300,225),10)
    occ=Entry(Point(300,50),10)
    seat=Entry(Point(300,200),10)
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
    occ.draw(win)
    seat.draw(win)
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
            ar1=iar1.getText()
            ar2=iar2.getText()
            p1=ip1.getText()
            p1=ip2.getText()
            
        #if pressed quit
        if 650 <= response.getX()<= 725 and 150 <= response.getY()<= 175:       
            x=0

    
    win.close()
main()
