import tkinter as tk
from math import sin, cos
import math
import numpy as np

height = 800
width = 800
Scale=20
X0=width/4
Y0=height/2

def shift(M,dx,dy):
    T = np.matrix([[1,0,0],[0,1,0],[dx,dy,1]])
    return M * T

def printWindow(canvas, wind):
    canvas.delete("all")
    drawXYZ(canvas)
    canvas.create_line(wind[0, 0], wind[0, 1], wind[1, 0], wind[1, 1], width=2, fill="grey")
    canvas.create_line(wind[0, 0], wind[0, 1], wind[3, 0], wind[3, 1], width=2, fill="grey")
    canvas.create_line(wind[1, 0], wind[1, 1], wind[2, 0], wind[2, 1], width=2, fill="grey")
    canvas.create_line(wind[2, 0], wind[2, 1], wind[3, 0], wind[3, 1], width=2, fill="grey")

def printPoly(canvas,M,dx,dy,color):
    y_min, y_max = fyM(M)
    x_min, x_max = fxM(M)
    pol=shift(M,-x_min+dx,-y_min+dy)
    for i in range(len(pol)-1):
        canvas.create_line(pol[i, 0], pol[i, 1], pol[i+1, 0], pol[i+1, 1], width=2, fill="grey")
    fillLine(canvas,pol,color)

def moveWindow(canvas,M1,M2, stepX, stepY):
    stepX = Scale*(int(stepX.get())-2.5)
    stepY = -Scale* (int(stepY.get())-2.5)
    M1=shift(M1,stepX,stepY)
    printWindow(canvas,M1)
    for i in range(len(M2)-1):
        canvas.create_line(M2[i, 0], M2[i, 1], M2[i+1, 0], M2[i+1, 1], width=2, fill="grey")
    return M1

def fyM(M):
    M = np.array(M)
    return np.min(M[:,1]), np.max(M[:,1])

def fxM(M):
    M = np.array(M)
    return np.min(M[:,0]), np.max(M[:,0])

def fillLine(canvas,M,color):
    y_min, y_max = fyM(M)
    x_min, x_max = fxM(M)
    def findC(canvas, M, y_min, y_max, x_min, x_max, color):
        point=[]
        M=np.array(M)
        for i in np.arange(y_min+0.5,y_max,0.1):
            for j in range(len(M)-1):
              x,y=findCross(x_min-10,i,x_max,i,M[j][0],M[j][1],M[j+1][0],M[j+1][1])
              if (x!=None and y!=None):
                  if(checkEntry(M,x,y)):
                    point.append([x,y,j])
            if(len(point)>1):
                canvas.create_line(point[0][0],point[0][1],point[1][0],point[1][1],width=2, fill=color)
            point=[]

        print(point)
    findC(canvas,M,y_min,y_max,x_min,x_max, color)

def createLine(x1,y1,x2,y2):
    b=(x1*y2-x2*y1)/(x1-x2)
    k=(y1-b)/x1
    return k, b

def Fs(x1,y1,x2,y2,xs,ys):
    F=np.matrix([[xs-x1, ys-y1],[x2-x1, y2-y1]])
    return np.linalg.det(F)

def checkEntry(M,x,y):
    for i in range(len(M)-1):
        sign=Fs(M[i][0],M[i][1],M[i+1][0],M[i+1][1],x,y)
        if(sign>0):
            return False
    return True


def workCircle(canvas,window, polyhendron,x,y):
    window=moveWindow(canvas,window,polyhendron,x,y)
    polyhPoint=polyhendron.copy()
    window=window.copy()
    window=np.array(window)
    polyhPoint=np.array(polyhPoint)
    window=np.append(window,[[window[0][0],window[0][1],1]],axis=0)
    points = []
    s_prev=0

    for k in range(4):
        for i in range(len(polyhPoint)):
            s =Fs(window[k][0],window[k][1],window[k+1][0],window[k+1][1],polyhPoint[i][0],polyhPoint[i][1])
            if (i>0):
                if (s>0 and s_prev>0):
                    continue
                elif(s<=0 and s_prev<=0):
                    points.append([polyhPoint[i][0], polyhPoint[i][1],1])

                elif(s_prev>=0 and s<=0):
                    X,Y= findCross(window[k][0],window[k][1],
                        window[k+1][0],
                        window[k+1][1],
                        polyhPoint[i-1][0],
                        polyhPoint[i-1][1],
                        polyhPoint[i][0],
                        polyhPoint[i][1])

                    points.append([X,Y,1])
                    points.append([polyhPoint[i][0],polyhPoint[i][1],1])


                elif(s_prev<=0 and s >=0):
                    X, Y = findCross(
                        window[k][0],
                        window[k][1],
                        window[k+1][0],
                        window[k+1][1], polyhPoint[i - 1][0], polyhPoint[i - 1][1], polyhPoint[i][0], polyhPoint[i][1])
                    points.append([X, Y,1])

            s_prev=s
        polyhPoint=np.array(points).copy()
        polyhPoint = np.append(polyhPoint, [[polyhPoint[0][0],polyhPoint[0][1],1]], axis=0)
        points=[]
    fillLine(canvas,polyhendron,"blue")
    fillLine(canvas, polyhPoint, "red")
    printPoly(canvas,polyhPoint,Scale*10,Scale*25, "red")
    printPoly(canvas, polyhendron, Scale * 20, Scale * 25, "blue")

def findCross(x1,y1,x2,y2,x3,y3,x4,y4):

    def Fx(k, b, x):
        return k * x + b

    def invFx(k, b, y):
        return (y - b) / k

    def findX(k1, b1, k2, b2):
        return (b2 - b1) / (k1 - k2)

    if(y1==y2 and y3==y4):
        return None, None
    elif (x1 == x2 and y3 == y4):
        return x1, y3
    elif (x3 == x4 and y1 == y2):
        return x3, y1
    elif(x1==x2 and y3!=y4):
        k,b=createLine(x3,y3,x4,y4)
        return x1, Fx(k,b,x1)
    elif(x3==x4 and y1!=y2):
        k, b = createLine(x1, y1, x2, y2)
        return x1, Fx(k, b, x3)
    elif(y1==y2 and x3!=x4):
        k, b = createLine(x3, y3, x4, y4)
        return invFx(k, b, y1), y1
    elif (y3 == y4 and x1 != x2):
        k, b = createLine(x1, y1, x2, y2)
        return invFx(k, b, y3), y3
    else:
        k1, b1 = createLine(x1, y1, x2, y2)
        k2, b2= createLine(x3, y3, x4, y4)
        X = findX(k1,b1,k2,b2)
        return X, Fx(k1,b1,X)



def createPolyhedron(canvas,period=Scale):
    pol = np.matrix([[5, 10, 1],
                    [10, 15, 1],
                    [15, 15, 1],
                    [19, 10, 1],
                    [15, 5, 1],
                    [10, 5, 1],
                    [5, 10, 1]])
    pol = shapeScale(pol, period)
    pol = mirrorX(pol)
    pol = shift(pol, X0, Y0)
    for i in range(len(pol)-1):
        canvas.create_line(pol[i, 0], pol[i, 1], pol[i+1, 0], pol[i+1, 1], width=2, fill="grey")

    return pol

def mirrorX(M):
    T = np.matrix([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
    return M*T

def shapeScale(M,period):
    T=np.matrix([[period,0,0],[0,period,0],[0,0,1]])
    return M*T

def T180(M, dx, dy):
    T = np.matrix([[-1,0,0],[0,-1,0],[0,0,1]])
    return shift(shift(M,-dx,-dy)*T,dx,dy)

def T90(M, dx, dy):
    T = np.matrix([[0,1,0],[-1,0,0],[0,0,1]])
    return shift(shift(M,-dx,-dy)*T,dx,dy)

def createWindow(canvas,period=Scale):
    wind=np.matrix([[1,1,1],[1,5,1],[5,5,1],[5,1,1]])
    wind = shapeScale(wind,period)
    wind = mirrorX(wind)
    wind = shift(wind,X0,Y0)
    printWindow(canvas,wind)
    return wind

def drawOXY(y, canvas, name, dx,dy):
    canvas.create_line(y[0, 0], y[0, 1], y[1, 0], y[1, 1], width=2, fill="grey")
    for i in range(2, len(y), 2):
        canvas.create_line(y[i, 0], y[i, 1], y[i + 1, 0], y[i + 1, 1], width=2, fill="grey")
        canvas.create_text(y[i, 0] - dx, y[i, 1]+ dy, text=str(int((i) / 2)))
    canvas.create_text(y[1, 0] - dx, y[1, 1] + 10, text=name, font=("DejavuSansLight", 15,"bold"))

def createCord(length=height/2, period=Scale, arrow=10):
    m = np.matrix([[0, 0, 1],
                   [0, length,1]])
    for i in range(1, round(length // period)):
        m = np.vstack([m, [-arrow / 2, i * period, 1]])
        m = np.vstack([m, [arrow / 2, i * period, 1]])
    return shift(m,X0, Y0)

def drawXYZ(canvas, length=height/2, period=Scale):
    y = createCord(length,period)
    y= T180(y,X0, Y0)
    x=T90(y,X0, Y0)
    drawOXY(y,canvas,'Y', 15, 0)
    drawOXY(x, canvas, 'X', 0, 15)
    canvas.create_text(y[0, 0] - 8, y[0, 1], text=str(0))


def main():
    window = tk.Tk()
    window.title('Отсечение многоугольника')
    canvas = tk.Canvas(window, width=width, height=height, bg="white", cursor="pencil")
    M1 = createWindow(canvas)
    M2 = createPolyhedron(canvas)
    drawXYZ(canvas, length=height / 2, period=20)
    tk.Label(text="Координата по X:").grid(column=0, row=0, sticky="nw")
    tk.Label(text="Координата по Y:").grid(column=0, row=1, sticky="nw")
    x = tk.Entry(width=4)
    y = tk.Entry(width=4)
    x.grid(column=1, row=0, sticky="nw")
    y.grid(column=1, row=1, sticky="nw")
    upB = tk.Button(window, text="Изменить")
    upB.config(command=lambda: moveWindow(canvas,M1,M2, x, y))
    upB.grid(column=0, row=2, sticky="nw", columnspan=1, padx=30)
    cutB = tk.Button(window, text="Отсечь ")
    cutB.config(command=lambda:workCircle(canvas,np.array(M1),np.array(M2), x, y))
    cutB.grid(column=0, row=3, sticky="nw", columnspan=1, padx=30)
    canvas.grid(row=0, column=3, sticky='nw',rowspan=30)
    window.mainloop()

main()