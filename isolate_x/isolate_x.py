from sympy import symbols,Eq,sin,cos,tan,sec,csc,cot,Mul


#trigonometric, logarithmic and nested functions are not supported
def isolate_x(equation):
    print(f"Given Equation:{equation}")
    left_side = equation.lhs
    right_side = equation.rhs

    highest_degree_term = left_side.as_ordered_terms()[0]
    right_side = highest_degree_term
    left_side = highest_degree_term - left_side 
    

    while not (right_side.is_Atom and right_side.has(x)):

        if right_side.is_Mul:
            args = right_side.args
            for i in range(1,len(args)):
                right_side = right_side / args[i] 
                left_side = left_side / args[i]
        
        elif right_side.is_Pow:
            base,exponent = right_side.as_base_exp()
            right_side = base
            left_side = left_side ** (1 / exponent) 
        
        elif right_side.is_Function:
            if right_side.func is [sin,cos,tan,cot,sec,csc]:
                pass
            # elif right_side.func is [log,ln]:
            #     pass
            else:
                raise NotImplementedError(f"Cannot isolate {right_side}")

            
        
        else:
            raise NotImplementedError(f"Cannot isolate {right_side}")
        
        
    print(f"Left Side:{left_side} Right Side:{right_side}")

    return left_side, right_side


if __name__ == "__main__":
    x = symbols('x')
    equations = [
        "sin(x) * x ** 2 * cos(x) + 4",
        "x**2 + 4*x - 5",
        "sin(cos(x))+cos(sin(x))",
        "cos(x)**2 + 5 ",
        "sin(cos(x))"
    ]
    for equation_str in equations: #f(x) = 0
        equation = Eq(eval(equation_str),0)
        isolate_x(equation)   # g(x)