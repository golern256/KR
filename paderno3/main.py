import math as m
def calcL(L,N):
  return L*N

def calcPi(E,i,Ls,Tp):
  return E*(Ls*Tp)**i/m.factorial(i)


def main():
  Pd=0.975
  L=0.0045
  N=3
  Tp=4.5
  Trem=11
  Pnd= 1-Pd
  Pi=0
  Pm_min=0
  Pm_max=1
  i=0
  Ls = calcL(L, N)
  E=m.exp(-Ls*Tp)
  while(Pm_max>Pnd):
    Pi=calcPi(E,i,Ls,Tp)
    Pm_min+=Pi
    Pm_max=1-Pm_min
    i+=1
  print(i)
  print(Pm_max)



main()







