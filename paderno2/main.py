import matplotlib.pyplot as plt

import math

import numpy as np

def createK(T1,T2):
  return (1/T2 - 1/T1)/math.log(T1/T2), math.log(T1/T2)

def createYpr(a,b,k,delta,t):
  return math.log(b/(1-a))/delta + k*t


def createYbr(a,b,k,delta,t):
  return math.log((1-b)/a)/delta + k*t


def printDelta(y,y_pr,y_br):
  print("Приемочная",abs(y_pr-y))
  print("Броковка",abs(y_br-y))


def calcDelta(y,y_pr,y_br):
  return (abs(y_pr-y)-abs(y_br-y))

def drawGraph(a,b,T1,T2,lenght=1000):
  Ypr=[]
  Ybr=[]
  k,delta=createK(T1,T2)
  t=np.arange(lenght)
  for i in range(lenght):
    Ypr.append(createYpr(a,b,k,delta,t[i]))
    Ybr.append(createYbr(a,b,k,delta,t[i]))

  #добалвение испытаний на График
  N=[2,2,5]
  T=[300,500,800]
  # проекции точек
  Np_pr = [createYpr(a, b, k, delta, T[0]), createYpr(a, b, k, delta, T[1]), createYpr(a, b, k, delta, T[2])]
  Np_br = [createYbr(a, b, k, delta, T[0]), createYbr(a, b, k, delta, T[1]), createYbr(a, b, k, delta, T[2])]
  plt.plot(t, Ypr,color='black', linewidth=2)
  plt.plot(t, Ybr,color='black',linewidth=2)
  plt.scatter(T,N,s=100, c='black')
  plt.scatter(T,Np_pr,s=100, c='black')
  plt.scatter(T, Np_br, s=100, c='black')
  #for i in range(len(T)):
   # plt.vlines(T[i],Np_pr[i],Np_br[i],colors='black', linestyle = '--')

  for i in range(len(N)):
    print(calcDelta(N[i],Np_pr[i],Np_br[i]))
  # Подпись Графиков
  placeN=int(0.95*lenght)
  plt.text(t[placeN],Ypr[len(Ypr)-1],"1",fontsize=16)
  plt.text(t[placeN],Ybr[len(Ybr)-1],"2",fontsize=16)
  placeN = int(0.3 * lenght)
  plt.text(t[placeN],7, "Nbr", fontsize=16)
  placeN = int(0.85 * lenght)
  #plt.text(t[placeN], -2, "Npr", fontsize=16)
  plt.text(t[placeN], 0.5, "Npr", fontsize=16)

#Подпись точек
  for i in range(len(N)):
    plt.text(T[i]+5, N[i]+0.2, i+1, fontsize=14)
  plt.ylim(0)
  plt.xlim(0,lenght)
  plt.grid()
  plt.xlabel("Время(часы)", fontsize=16)
  plt.ylabel("Количество отказов",fontsize=16)
  plt.show()



#def deltaY


a=0.15
b=0.2
T1=220
T2=140

drawGraph(a,b,T1,T2)



