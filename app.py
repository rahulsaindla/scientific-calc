from flask import Flask, render_template, request
from sympy import symbols,sympify
import math

app = Flask(__name__)

expression = ""
result = ""
integralresult=""

@app.route("/integration")
def integration():
    return render_template("integration.html")
@app.route("/diff")
def diff():
    return render_template("diff.html")

@app.route("/trig")
def trig():
    return render_template("trig.html")

@app.route("/statistics")
def statistics():
    return render_template("statistics.html")
@app.route("/", methods=["GET", "POST"])
def cal():
      selected_formula = request.args.get("formula", "")
      global expression
      global result
      global integralresult
      if request.method =="POST":
        expression = request.form.get("expression", "")

        lowerlimit = request.form.get("lowerlimit")
        upperlimit = request.form.get("upperlimit")
        selected_formula_post = request.form.get("selected_formula", "")
        

        btn = request.form.get("btn")
        print("BTN =", btn)

        action = request.form.get("action")

        print("ACTION =", action)
        print("FORMULA =", selected_formula_post)
    
    
        if action == "evaluate_integral":

         x = symbols('x')

         formula = selected_formula_post

        
         formula = formula.replace("²", "**2")
         formula = formula.replace("³", "**3")
         formula = formula.replace("⁴", "**4")
         print( formula)


         expr = sympify(formula)
         print(expr.free_symbols)

         print( expr)

         uppervalue = expr.subs(x, float(upperlimit))

         print( "upperlimit",uppervalue)
         lowervalue = expr.subs(x,float(lowerlimit))
         print("lowelimit=",lowervalue)
         answer= uppervalue-lowervalue
         integralresult = answer
        
        if btn == "commentout":
           expression=""
           result=""


        elif btn == "c":

            expression = ""

        elif btn == "DEL":

            expression = expression[:-1]

        elif btn == "1/x":

         if expression:
           expression = f"(1/({expression}))"

        elif btn and btn != "=":

         expression += btn

        elif btn == "=" or btn is None:

            try:

                import re

                exp = expression

# Powers
                exp = exp.replace("^", "**")

# Constants
                exp = exp.replace("π", str(math.pi))
                exp = exp.replace("e", str(math.e))

# Functions
                exp = exp.replace("sin(", "math.sin(math.radians(")
                exp = exp.replace("cos(", "math.cos(math.radians(")
                exp = exp.replace("tan(", "math.tan(math.radians(")

                exp = exp.replace("log(", "math.log10(")
                exp = exp.replace("ln(", "math.log(")

# e^x
                exp = exp.replace("exp(", "math.exp(")

# Close extra bracket added by radians(
                if "math.sin(math.radians(" in exp:
                 exp += ")"

                if "math.cos(math.radians(" in exp:
                 exp += ")"

                if "math.tan(math.radians(" in exp:
                 exp += ")"

# Factorial
                while "!" in exp:
                 exp = re.sub(
                  r'(\d+)!',
                  lambda m: str(math.factorial(int(m.group(1)))),
                 exp
                    )

                answer = str(eval(exp))
                expression = answer

            except ZeroDivisionError:
               result = "Cannot divided by zero"
            except SyntaxError:
               result = "invalid expression"
            except Exception as e:
               result= str(e)
               
               
               
               

            

                

      return render_template("scical.html", expression=expression,result=result,selected_formula=selected_formula,integralresult=integralresult)

if __name__ == "__main__":
    app.run(debug=True)