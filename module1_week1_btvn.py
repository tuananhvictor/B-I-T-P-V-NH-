# -*- coding: utf-8 -*-
"""MODULE1-WEEK1-BTVN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VKhpfJxjs82PCQ2UtLI3AZHg0E6r34HN

CÂU 1 TỰ LUẬN
"""

data = ['tp','tn','fp','fn'] #Chứa các tên để gọi
data1 = []# Chứa các giá trị ứng với 'data'
for i in data:
  print(i,'data?4')
  try:
    n = int(input())
    if n <0:
      print('tp and fp and fn must be greater than zera')
      break
    data1.append(n)

  except ValueError:
    print(i,'must be int ')
    break
Precision = data1[0]/(data1[0]+data1[2])
Recall = data1[0]/((data1[0])+data1[3])
print('Precision:',Precision)
print('Recall:',Recall)
print('F1-score:',2*((Precision*Recall)/(Precision+Recall)))

"""CÂU 2 TỰ LUẬN"""

import math

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        print(f'n must be a number')
        return False

def relu(n):
    return max(0, n)

def sigmoid(n):
    return 1 / (1 + math.exp(-n))

def ELU(n, a=0.01):
    if n <= 0:
        return a * (math.exp(n) - 1)
    else:
        return n

functions = {'sigmoid': sigmoid, 'relu': relu, 'ELU': ELU}

while True:
    n = input("Enter a number: ")
    if not is_number(n):
        break
    print(f"Available function: sigmoid, relu, ELU")
    command = input(f'Function:')
    if command not in functions:
      print(command,'is not supported')
    for key, value in functions.items():
        if key == command:
            print(functions[key](float(n)))
            break
    command1 = input(f'Continue the program?')
    if command1 == 'stop':
        break

"""CÂU 3 TỰ LUẬN"""

import random as rd
def mae(n):
  mae = []
  for j,k in zip(data,data1):
    mae.append(abs(j-k))
  return sum(mae)*(1/n)
def mse(n):
  mse = []
  for j,k in zip(data,data1):
    mse.append(abs(j-k))
  return (1/n)*(j-k)**2
try:
  n = int(input(f'Sample:'))
except ValueError:
  print('n must be int')

data = []
data1 = []
for i in range(n):
  data.append(rd.uniform(0,10))
  predict = rd.uniform(0,10)
  data1.append(predict)
  print(data,data1)
command= input('Available loss function: mae, mse')
if command == 'mae':
  print(mae(n))
elif command == 'mse':
  print(mse(n))

"""CÂU 4 TỰ LUẬN"""

import math

def giaithua(n):
  tich = 1
  if n ==0:
    return 0
  elif n!=0:
    for i in range(1,n+1):
      tich = tich*i
    return tich
def sina(x,n):
  sin = ((-1)**n)*((x**(2*n+1))/ giaithua(2*n+1))
  sina = []
  for i in range(n+1):
    sina.append(sin)
  return sum(sina)
def cosa(x,n):
  cos = ((-1)**n)*((x**(2*n))/ giaithua(n*2))
  cosa = []
  for i in range(n):
    cosa.append(cos)
  return sum(cosa)
def sinh(x,n):
  sinh = (x**(2*n+1))/ giaithua(n*2+1)
  sinha = []
  for i in range(n+1):
    sinha.append(sinh)
  return sum(sinha)
def cosh(x,n):
  cosh =(x**(2*n))/ giaithua(n*2)
  cosha=[]
  for i in range(n):
    cosha.append(cosh)
  return sum(cosha)

x = math.radians(float(input()))
n = int(input())
print(sina(x,n))
print(cosa(x,n))
print(sinh(x,n))
print(cosh(x,n))

"""CÂU 5 TỰ LUẬN"""

import math
def meandiffroot(y1,y2,n,p):
  return (math.pow(y1,1/n)-math.pow(y2,1/n))**p

y1 = float(input())
y2 = float(input())
n = int(input())
p = int(input())
print(meandiffroot(y1,y2,n,p))