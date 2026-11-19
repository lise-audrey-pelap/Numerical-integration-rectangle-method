import numpy as np
import matplotlib.pyplot as plt

try: 
    a= float(input("Enter the lower limit of integration \n"))
    b= float(input(" Enter the upper limit of integration \n"))
    n= int(input("enter the number of points for your calculation \n"))
except ValueError:
    print('Please enter a valid value')  
    
#Initialization of the function
pas=0.000001
z= np.arange(a,b+pas,pas)
t=1/(1+z**2)
integralereel=np.pi/4

#calculation of the integral 
h= (b-a)/n
x=np.arange(a,b+h,h)
y=1/(1+x**2)
som= np.sum(y[0:n])
integrale=som*h

#calculation of the error
derive1=np.gradient(t,z)
positive =np.abs(derive1)
maximum=np.max(positive)
erreur=(((b-a)**2)*maximum)/(2*n)

#plotting of function
plt.subplot(1,2,2)
plt.plot(z,t,"g")
plt.plot(x,y,"o")
plt.title('$1/(1+x^2)$')
plt.xlabel('x')
plt.ylabel('y')

#rectangle curves
for i in range(0,n): #horizontal plot
    abscisseh=x[i:i+2]
    ordonneh=np.array([y[i],y[i]])
    plt.plot(abscisseh,ordonneh,"r--")
for i in range(0,n+1):  #vertical plot
    abscissev=np.array([x[i],x[i]])
    if y[i]<y[i-1]:
        ordonnev=np.array([0,y[i-1]])
    else:
        ordonnev=np.array([0,y[i]])
    plt.plot(abscissev,ordonnev,"r--")
    
plt.subplot(1,2,1)
plt.plot(z,derive1,'b')
plt.title('first derivative')    
plt.grid(True) 
plt.show()

print(f"the integral of this function from {a} to {b} is {integrale} \n The interpolation error is less than {erreur}")
print(f"The absolute error obtained is {integrale-integralereel}")