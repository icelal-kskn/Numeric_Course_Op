import numpy as np

class Bracketing:

    def __init__(self,fn:callable,a:int,b:int,tol:float):
        self.__fn = fn
        self.__a = a
        self.__b = b
        self.__tol = tol
        self.bisection_answer = self.bisection(a,b,tol)
        self.false_position_answer = self.false_position(a,b,tol)
    
    def bisection(self,a:int,b:int,tol:float):
        if a > b :
            raise ValueError("B must bigger than A")
        
        i=0
        while True:
            if i>1e6:
                raise ValueError("Could not find the solution")
            i+=1

            fa=self.__fn(a)
            fb=self.__fn(b)

            if fa*fb>0:
                raise ValueError("The interval doees not contain a solution")
            
            c=(a+b)/2
            fc=self.__fn(c)

            if abs(fc)<tol or abs(b-a)<tol:
                return c
            else:
                if fa*fc<0:
                    b=c
                else:
                    a=c

            print(f"Bisection Iteration{i:6d}: a={a:4f}, b={b:4f}, c={c:4f}, f(c)={fc:4f}")

    def false_position(self,a:int,b:int,tol:float):
        if a > b:
            raise ValueError("B must be bigger than A") 

        i=0
        while True:
            if i>1e6:
                raise ValueError("Could not find the solution")
            
            i+=1
            fa=self.__fn(a)
            fb=self.__fn(b)

            if fa*fb>0:
                raise ValueError("The interval does not contain a solution")
            
            c= b - (fb*((b-a)/(fb-fa)))
            fc=self.__fn(c)

            if abs(fc)<tol or abs(b-a)<tol:
                return c
            else:
                if fa * fc<0:
                    b = c
                else:
                    a = c 
            
            print(f"False Position Iteration{i:6d}: a={a:4f}, b={b:4f}, c={c:4f}, f(c)={fc:8f}")

def f(x):
    return np.sin(x)/x



if __name__=="__main__":
    a= 1
    b= 50
    tol=1e-6
    bracketing = Bracketing(f,a,b,tol)

