from sympy import symbols,Eq,sin,cos,tan,sec,csc,cot,asin,acos,atan,acot,log,exp,ln


#Note that trigonometric functions lose their domain of definition if the inverse is taken. //Write frontend
def isolate_x(equation):
    left_side = equation.lhs
    right_side = equation.rhs

    x_terms = [i for i in left_side.as_ordered_terms() if i.has(x) ]  
    right_side = x_terms[0]
    left_side = x_terms[0] - left_side 
    
    inverse_map = {
        sin: asin,
        cos: acos,
        tan: atan,
        cot: acot,
        sec: lambda x: acos(1/x),  # Special handling for sec
        csc: lambda x: asin(1/x),   # Special handling for csc
        asin: sin,
        acos: cos,
        atan: tan,
        acot: cot,
        log: exp,
        exp:log
    }

    patience = 10
    while not right_side.is_Atom :
        patience -=1
        if patience < 0:
            print("Not Enough Patience for this equation")
            break

        if right_side.is_Mul: 
            args = right_side.args
            if any(arg.is_Rational and arg.denominator == 1 for arg in args): #dividing 
                left_side = (left_side / right_side.args[0])
                if left_side != 0:
                    left_side = 1/left_side
                right_side, _  = right_side.args[1].as_base_exp()

            else: #multiplication
                for i in range(1,len(args)):
                    right_side = right_side / args[i] 
                    left_side = left_side / args[i]
        
        elif right_side.is_Pow:
            base,exponent = right_side.as_base_exp()
            right_side = base
            left_side = left_side ** (1 / exponent)
             
        
        elif right_side.is_Function: #trigh not supported
            if right_side.func in inverse_map:  
                inverse_func = inverse_map[right_side.func]
                right_side = right_side.args[0]
                left_side = inverse_func(left_side)
            else:
                raise NotImplementedError(f"Cannot isolate {right_side}")

        else:
            raise NotImplementedError(f"Cannot isolate {right_side}")


    return left_side, right_side


if __name__ == "__main__":
    x = symbols('x')
    equations = [
        "x**2 + 3*x + 3/x",
        "3 / cos(x)",
        "3/x",
        "sin(x) * x ** 2 * cos(x) + 4",
        "x**2 + 4*x - 5",
        "sin(x)+4",
        "sin(cos(x))+cos(sin(x))",
        "cos(x)**2 + 5 ",
        "sin(cos(x))",
        "x**3 - 6*x**2 + 11*x - 6",
        "tan(x) + 3",
        "cos(sin(x)) + 1",
        "exp(2*x) - 5",
        "log(x) - 4",
        "log(x,5) - 5",
        "ln(x)",
        "ln(x) - 4",
        "sin(x) * cos(x) - 1/2",
        "cos(x)**2 - sin(x)**2",
        "x**2 * tan(x) + x - 3",
        "sec(x) - 2",
        "csc(x) + 3"
    ]
    for equation_str in equations: #f(x) = 0
        equation = Eq(eval(equation_str),0)
        left_side,right_side=isolate_x(equation)   # g(x)
        if str(right_side) == "x":
            g = str(left_side)
            print(f"g_x = {g}")
        else:
            print("Did not find the g_x")
