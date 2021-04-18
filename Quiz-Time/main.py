from flask import Flask, render_template

app = Flask("")

# information for each page (for flask variables)
math_dict = [
  {'Img': '../static/assets/MQ1.png', 'Q': 'Choose 1:', 'A1': '3/(4t)', 'A2': '3/(2t)', 'A3': '3/2', 'A4': '3/4', 'F1': "toNext('M','1','2',1)", 'F2': "toNext('M','1','2',0)", 'F3': "toNext('M','1','2',0)", 'F4': "toNext('M','1','2',0)", 'num': 'MQ1'},
  {'Img': '../static/assets/MQ2.png', 'Q': "What does the nth term test say about S?", 'A1': 'Converges conditionally', 'A2': 'Converges', 'A3': 'Diverges', 'A4': 'Inconclusive', 'F1': "toNext('M','2','3',0)", 'F2': "toNext('M','2','3',0)", 'F3': "toNext('M','2','3',1)", 'F4': "toNext('M','2','3',0)", 'num': 'MQ2'},
  {'Img': '../static/assets/MQ3.png', 'Q': "Solve", 'A1': '-sin(x)x^2', 'A2': '2xsin(x)+cos(x)x^2', 'A3': 'cos(x)x^2-sin(x)x^2', 'A4': '2xcos(x)-sin(x)x^2', 'F1': "toNext('M','3','4',0)", 'F2': "toNext('M','3','4',0)", 'F3': "toNext('M','3','4',0)", 'F4': "toNext('M','3','4',1)", 'num': 'MQ3'},
  {'Img': '../static/assets/MQ4.png', 'Q': "Can this differential equation be solved using separation of variables?", 'A1': 'Yes', 'A2': 'No', 'A3': 'Yes', 'A4': 'No', 'F1': "toNext('M','4','5',0)", 'F2': "toNext('M','4','5',1)", 'F3': "toNext('M','4','5',0)", 'F4': "toNext('M','4','5',1)", 'num': 'MQ4'},
  {'Img': '../static/assets/MQ5.png', 'Q': "What is the absolute maximum value of g?", 'A1': '36', 'A2': '4', 'A3': '116', 'A4': 'g has no maximum value', 'F1': "toNext('M','5','6',0)", 'F2': "toNext('M','5','6',0)", 'F3': "toNext('M','5','6',0)", 'F4': "toNext('M','5','6',1)", 'num': 'MQ5'},
  {'Img': '../static/assets/MQ6.png', 'Q': "Find lim f(x) x->1", 'A1': '0', 'A2': '1', 'A3': 'e', 'A4': 'DNE', 'F1': "toNext('M','6','7',1)", 'F2': "toNext('M','6','7',0)", 'F3': "toNext('M','6','7',0)", 'F4': "toNext('M','6','7',0)", 'num': 'MQ6'},
  {'Img': '../static/assets/MQ7.png', 'Q': "Area of region between f & g from [1, 5]", 'A1': '25', 'A2': '392/5', 'A3': '184/15', 'A4': '16', 'F1': "toNext('M','7','8',0)", 'F2': "toNext('M','7','8',0)", 'F3': "toNext('M','7','8',0)", 'F4': "toNext('M','7','8',1)", 'num': 'MQ7'},
  {'Img': '../static/assets/MQ8.png', 'Q': "Determine S", 'A1': 'S diverges', 'A2': '6', 'A3': '3', 'A4': '-3', 'F1': "toNext('M','8','9',1)", 'F2': "toNext('M','8','9',0)", 'F3': "toNext('M','8','9',0)", 'F4': "toNext('M','8','9',0)", 'num': 'MQ8'},
  {'Img': '../static/assets/MQ9.png', 'Q': "Integrate", 'A1': 'C+4x-3ln|x|', 'A2': '4ln|x| + C - 3e^x', 'A3': 'C+4x-3e^x', 'A4': 'C+4ln|x|-3ln|x|', 'F1': "toNext('M','9','10',0)", 'F2': "toNext('M','9','10',1)", 'F3': "toNext('M','9','10',0)", 'F4': "toNext('M','9','10',0)", 'num': 'MQ9'},
  {'Img': '../static/assets/MQ10.png', 'Q': "lim g(x) x->-3", 'A1': '1', 'A2': '0', 'A3': 'oo', 'A4': 'undefined', 'F1': "toNext('M','10','11',1)", 'F2': "toNext('M','10','11',0)", 'F3': "toNext('M','10','11',0)", 'F4': "toNext('M','10','11',0)", 'num': 'MQ10'},
  {'Img': '../static/assets/MQ11.png', 'Q': "dy/dx=", 'A1': '10/(lnx(1+5x^2))', 'A2': 'ln(x)/(1+5x^2)', 'A3': '10x/(1+5x^2)', 'A4': '(1+5x^2)^-1', 'F1': "toNext('M','11','12',0)", 'F2': "toNext('M','11','12',0)", 'F3': "toNext('M','11','12',1)", 'F4': "toNext('M','11','12',0)", 'num': 'MQ11'},
  {'Img': '../static/assets/MQ12.png', 'Q': "g'(2)=", 'A1': '22/3', 'A2': '4', 'A3': '1/3', 'A4': '-88/3', 'F1': "toNext('M','12','13',1)", 'F2': "toNext('M','12','13',0)", 'F3': "toNext('M','12','13',0)", 'F4': "toNext('M','12','13',0)", 'num': 'MQ12'},
  {'Img': '../static/assets/MQ13.png', 'Q': "Area of R? (Intersects at theta = +- pi/3)", 'A1': 'pi/2', 'A2': '.685', 'A3': '5.961', 'A4': 'pi', 'F1': "toNext('M','13','14',0)", 'F2': "toNext('M','13','14',0)", 'F3': "toNext('M','13','14',0)", 'F4': "toNext('M','13','14',1)", 'num': 'MQ13'}
]

programming_dict = [
  {'Img': '../static/assets/PQ1.png', 'Q': "How many times does the code in the while loop execute?", 'A1': '7', 'A2': '8', 'A3': '9', 'A4': '10', 'F1': "toNext('P','1','2',1)", 'F2': "toNext('P','1','2',0)", 'F3': "toNext('P','1','2',0)", 'F4': "toNext('P','1','2',0)", 'num': 'PQ1'},
  {'Img': '../static/assets/PQ2.png', 'Q': "How do you output in Python?", 'A1': 'Console.log', 'A2': 'System.out.println', 'A3': 'Print', 'A4': '=>', 'F1': "toNext('P','2','3',0)", 'F2': "toNext('P','2','3',0)", 'F3': "toNext('P','2','3',1)", 'F4': "toNext('P','2','3',0)", 'num': 'PQ2'},
  {'Img': '../static/assets/PQ3.png', 'Q': "How to declare function in JS", 'A1': 'def', 'A2': 'function', 'A3': 'void', 'A4': 'decFun', 'F1': "toNext('P','3','4',0)", 'F2': "toNext('P','3','4',1)", 'F3': "toNext('P','3','4',0)", 'F4': "toNext('P','3','4',0)", 'num': 'PQ3'},
  {'Img': '../static/assets/PQ4.png', 'Q': "How to get month from date in postgresql", 'A1': 'date_part', 'A2': 'date_trunc', 'A3': 'ntile', 'A4': 'get_month', 'F1': "toNext('P','4','5',1)", 'F2': "toNext('P','4','5',0)", 'F3': "toNext('P','4','5',0)", 'F4': "toNext('P','4','5',0)", 'num': 'PQ4'},
  {'Img': '../static/assets/PQ5.png', 'Q': "multiply(8) equals:", 'A1': '8*7*6*5*4*3*2', 'A2': '7*5*3', 'A3': '1', 'A4': '8*6*4*2', 'F1': "toNext('P','5','6',0)", 'F2': "toNext('P','5','6',0)", 'F3': "toNext('P','5','6',0)", 'F4': "toNext('P','5','6',1)", 'num': 'PQ5'},
  {'Img': '../static/assets/PQ6.png', 'Q': "mystery(6) equals:", 'A1': '12', 'A2': '16', 'A3': '26', 'A4': '32', 'F1': "toNext('P','6','7',0)", 'F2': "toNext('P','6','7',1)", 'F3': "toNext('P','6','7',0)", 'F4': "toNext('P','6','7',0)", 'num': 'PQ6'},
  {'Img': '../static/assets/PQ7.png', 'Q': "Output after execution:", 'A1': '4 12', 'A2': '-3 12', 'A3': '7 12', 'A4': '-3 6', 'F1': "toNext('P','7','8',1)", 'F2': "toNext('P','7','8',0)", 'F3': "toNext('P','7','8',0)", 'F4': "toNext('P','7','8',0)", 'num': 'PQ7'},
  {'Img': '../static/assets/PQ8.png', 'Q': "Which of the following could replace the body of compute", 'A1': 'return 4 * n;', 'A2': 'return 8 * n;', 'A3': ' return (int) Math.pow(n,8);', 'A4': ' return (int) Math.pow(n,4);', 'F1': "toNext('P','8','9',0)", 'F2': "toNext('P','8','9',0)", 'F3': "toNext('P','8','9',1)", 'F4': "toNext('P','8','9',0)", 'num': 'PQ8'},
  {'Img': '../static/assets/PQ9.png', 'Q': "Output:", 'A1': 'omp', 'A2': 'mp', 'A3': 'Om', 'A4': 'mpu', 'F1': "toNext('P','9','10',0)", 'F2': "toNext('P','9','10',1)", 'F3': "toNext('P','9','10',0)", 'F4': "toNext('P','9','10',0)", 'num': 'PQ9'},
  {'Img': '../static/assets/PQ10.png', 'Q': " For the method call t(5), how many calls to t will be made, including the original call?", 'A1': '9', 'A2': '14', 'A3': '8', 'A4': '5', 'F1': "toNext('P','10','11',1)", 'F2': "toNext('P','10','11',0)", 'F3': "toNext('P','10','11',0)", 'F4': "toNext('P','10','11',0)", 'num': 'PQ10'},
  {'Img': '../static/assets/PQ11.png', 'Q': "Is equal to:", 'A1': '(x < 7) || (x < 2)', 'A2': '(x >= 7) && (x < 2)', 'A3': ' (x >= 7) || (x <= 2)', 'A4': '(x >= 7) && (x > 2)', 'F1': "toNext('P','11','12',0)", 'F2': "toNext('P','11','12',0)", 'F3': "toNext('P','11','12',1)", 'F4': "toNext('P','11','12',0)", 'num': 'PQ11'},
  {'Img': '../static/assets/PQ12.png', 'Q': "What is returned from numList(5)?", 'A1': '5!', 'A2': '0! 1! 2! 3! 4! 5!', 'A3': '0!', 'A4': '5! 4! 3! 2! 1! 0!', 'F1': "toNext('P','12','13',0)", 'F2': "toNext('P','12','13',0)", 'F3': "toNext('P','12','13',1)", 'F4': "toNext('P','12','13',0)", 'num': 'PQ12'},
  {'Img': '../static/assets/PQ13.png', 'Q': "numbers was an ArrayList containing [7, 2, 4, 6, 3] what is it now?", 'A1': ' [7, 2, 8, 1, 3, 5]', 'A2': '[7, 8, 1, 6, 5, 3]', 'A3': '[7, 2, 1, 3, 2, 5, 9]', 'A4': '[7, 2, 8, 1, 6, 5, 9]', 'F1': "toNext('P','13','14',1)", 'F2': "toNext('P','13','14',0)", 'F3': "toNext('P','13','14',0)", 'F4': "toNext('P','13','14',0)", 'num': 'PQ13'},
]

random_dict = [
  {'Img': '../static/assets/RQ1.png', 'Q': "Michoacan's capital is:", 'A1': 'Zamora', 'A2': 'Morelia', 'A3': 'La Piedad', 'A4': 'Sahuayo', 'F1': "toNext('R','1','2',0)", 'F2': "toNext('R','1','2',1)", 'F3': "toNext('R','1','2',0)", 'F4': "toNext('R','1','2',0)", 'num': 'RQ1'},
  {'Img': '../static/assets/RQ2.png', 'Q': "The main character in Attack On Titan is:", 'A1': 'Levi', 'A2': 'Mikasa', 'A3': 'Zeke', 'A4': 'Eren', 'F1': "toNext('R','2','3',0)", 'F2': "toNext('R','2','3',0)", 'F3': "toNext('R','2','3',0)", 'F4': "toNext('R','2','3',1)", 'num': 'RQ2'},
  {'Img': '../static/assets/RQ3.png', 'Q': "Who's a co-founder of Google", 'A1': 'Diego Solorio', 'A2': 'Sergey Brin', 'A3': 'Peter Szulczewski', 'A4': 'Marc Benioff', 'F1': "toNext('R','3','4',0)", 'F2': "toNext('R','3','4',1)", 'F3': "toNext('R','3','4',0)", 'F4': "toNext('R','3','4',0)", 'num': 'RQ3'},
  {'Img': '../static/assets/RQ4.png', 'Q': "How many planets are there in our solar system:", 'A1': '9', 'A2': '7', 'A3': '10', 'A4': '8', 'F1': "toNext('R','4','5',0)", 'F2': "toNext('R','4','5',0)", 'F3': "toNext('R','4','5',0)", 'F4': "toNext('R','4','5',1)", 'num': 'RQ4'},
  {'Img': '../static/assets/RQ5.png', 'Q': "What colour does (127, 127, 127) make in RGB: ", 'A1': 'Grey', 'A2': 'Black', 'A3': 'White', 'A4': 'Gold', 'F1': "toNext('R','5','6',1)", 'F2': "toNext('R','5','6',0)", 'F3': "toNext('R','5','6',0)", 'F4': "toNext('R','5','6',0)", 'num': 'RQ5'},
  {'Img': '../static/assets/RQ6.png', 'Q': "What colour is a purple house?", 'A1': 'Yellow', 'A2': 'White', 'A3': 'Purple', 'A4': 'None of the above', 'F1': "toNext('R','6','7',0)", 'F2': "toNext('R','6','7',0)", 'F3': "toNext('R','6','7',1)", 'F4': "toNext('R','6','7',0)", 'num': 'RQ6'},
  {'Img': '../static/assets/RQ7.png', 'Q': "24th president of USA:", 'A1': 'Grover Cleveland', 'A2': 'Zackary Taylor', 'A3': 'Michael Jackson', 'A4': 'Dwight D. Eisenhower', 'F1': "toNext('R','7','8',1)", 'F2': "toNext('R','7','8',0)", 'F3': "toNext('R','7','8',0)", 'F4': "toNext('R','7','8',0)", 'num': 'RQ7'},
  {'Img': '../static/assets/RQ8.png', 'Q': "As of 2021 how many Jurassic Park movies?", 'A1': '5', 'A2': '6', 'A3': '7', 'A4': '8', 'F1': "toNext('R','8','9',0)", 'F2': "toNext('R','8','9',1)", 'F3': "toNext('R','8','9',0)", 'F4': "toNext('R','8','9',0)", 'num': 'RQ8'},
  {'Img': '../static/assets/RQ9.png', 'Q': "Top Cause of Death 2004 USA:", 'A1': 'Accidents', 'A2': 'Strokes', 'A3': 'Cancer', 'A4': 'Heart disease', 'F1': "toNext('R','9','10',0)", 'F2': "toNext('R','9','10',0)", 'F3': "toNext('R','9','10',0)", 'F4': "toNext('R','9','10',1)", 'num': 'RQ9'},
  {'Img': '../static/assets/RQ10.png', 'Q': "How many UCs are there in California?", 'A1': '9', 'A2': '7', 'A3': '10', 'A4': '8', 'F1': "toNext('R','10','11',1)", 'F2': "toNext('R','10','11',0)", 'F3': "toNext('R','10','11',0)", 'F4': "toNext('R','10','11',0)", 'num': 'RQ10'},
  {'Img': '../static/assets/RQ11.png', 'Q': "First video game created:", 'A1': 'Space Invaders', 'A2': 'Pong', 'A3': 'Pac-Man', 'A4': 'Tetris', 'F1': "toNext('R','11','12',0)", 'F2': "toNext('R','11','12',1)", 'F3': "toNext('R','11','12',0)", 'F4': "toNext('R','11','12',0)", 'num': 'RQ11'},
  {'Img': '../static/assets/RQ12.png', 'Q': "Year of Declaration of Independence:", 'A1': '1778', 'A2': '1775', 'A3': '1777', 'A4': '1776', 'F1': "toNext('R','12','13',0)", 'F2': "toNext('R','12','13',0)", 'F3': "toNext('R','12','13',0)", 'F4': "toNext('R','12','13',1)", 'num': 'RQ12'},
  {'Img': '../static/assets/RQ13.png', 'Q': "How many continents exist?", 'A1': '5', 'A2': '6', 'A3': '7', 'A4': '8', 'F1': "toNext('R','13','14',0)", 'F2': "toNext('R','13','14',0)", 'F3': "toNext('R','13','14',1)", 'F4': "toNext('R','13','14',0)", 'num': 'RQ13'}
]

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/math")
def math():
    return render_template("math.html", math_dict=math_dict)

@app.route("/programming")
def programming():
    return render_template("programming.html", programming_dict=programming_dict)

@app.route("/random")
def random():
    return render_template("random.html", random_dict=random_dict)
app.run(host='0.0.0.0',port=8080)