import random
from tkinter import *

window = Tk()
window.title("Quiz")
window.geometry("600x450")
window.configure(bg='#6D81FF')

questions = [["What is formed by the intersection of two number lines, the horizontal axis and vertical axis ?",
              "domain", "origin", "zeros", "coordinate plane"],
             ["What is a value substituted for an x-value in a function ?", "output", "quadrants", "range", "input"],
             ["What is a set of ordered pairs ?", "coordinate plane", "range", "function", "relation"],
             ["What is a relation can be shown in a list, a graph, a mapping or a function ?", "input", "Y-axis",
              "X-axis", "Table"],
             ["What form uses the generic equation y-k=m(x-h) ?", "Slope intercept", "Slope", "straight",
              "Point slope"],
             ["What form uses the generic equation Ax+By=C ?", "polynomial", "M", "Ordered pair", "Straight"],
             ["What form uses the generic equation y=mx+b ?", "Slope", "Table", "Quadrants", "Slope intercept"],
             ["What is an equation whose graph creates a straight line ?", "Straight", "Function", "Element",
              "Linear Function"],
             ["Complete this equation, if f(x)=-1/2x+3 and x=5 what is the value of f(x) ?", "-5,5", "-0,5", "5,5",
              "0,5"],
             ["What is the difference between the y-values divided by the difference of the x-values ?", "Straight",
              "Quadrants", "range", "Slope"], [
                 "Complete this sentence : the …. is the set of second numbers (x-values) of the ordered pairs of a "
                 "relation.",
                 "origin", "range", "relation", "table"],
             ["If x=8, what is the value of g(x)=5x(1/2)+20x ?", "80.5", "180", "20", "160"],
             ["What is an equation that has no solution?", "Contradiction", "Impossible", "similar", "Inequality"],
             ["What is an equation that is true for all values of the variables ?", "Inequality", "Contradiction",
              "Straight", "Identity"],
             ["Which of the following words is another name for the range value ?", "The x-intercept", "the input",
              "the y-intercept", "the output"],
             ["The set of numbers x for which a function f(x) is defined is called : ", "the vertex", "the range",
              "the gradient", "the domain"]

             ]


def clear():
    list = window.grid_slaves()
    for n in list:
        n.destroy()


class Quiz:
    def __init__(self, quest):
        clear()
        self.Fragen = []
        for n in quest:
            self.Fragen.append(n)
        self.a1 = ""
        self.a2 = ""
        self.a3 = ""
        self.a4 = ""
        self.Ra = ""
        self.RaBtn = Button(window, text="", font=("Arial", 14))
        self.antw1 = Button(window, text="", font=("Arial", 14))
        self.antw2 = Button(window, text="", font=("Arial", 14))
        self.antw3 = Button(window, text="", font=("Arial", 14))
        self.antw4 = Button(window, text="", font=("Arial", 14))
        self.lock = False
        self.right = 0
        self.naechste = Button(window, text="Next", bg='#3D32FF', fg='white', font=("Arial", 14),
                               command=self.Frage)
        self.nummer = 0
        self.Max = 10
        self.Frage()

    def Frage(self):
        self.naechste.grid(column=0, row=5, pady=5)
        if len(self.Fragen) > 0 and self.nummer < self.Max:
            self.nummer += 1
            self.lock = False
            randNum = random.randint(0, len(self.Fragen) - 1)
            fragenText = self.Fragen[randNum][0]
            self.Ra = self.Fragen[randNum][-1]
            answers = []
            for i in range(1, 5):
                answers.append(self.Fragen[randNum][i])
            random.shuffle(answers)

            self.a1 = answers[0]
            self.a2 = answers[1]
            self.a3 = answers[2]
            self.a4 = answers[3]

            frage = Text(window, bg='#6D81FF', border=0, font=("Calibri", 14), width=40, height=2)
            frage.insert(END, fragenText)
            frage.grid(column=0, row=0, padx=80, pady=(75, 0))

            self.antw1 = Button(window, text=self.a1, border=0, bg='#3D32FF', fg='white', font=("Arial", 14), width=39,
                                command=self.control1)
            self.antw2 = Button(window, text=self.a2, border=0, bg='#3D32FF', fg='white', font=("Arial", 14), width=39,
                                command=self.control2)
            self.antw3 = Button(window, text=self.a3, border=0, bg='#3D32FF', fg='white', font=("Arial", 14), width=39,
                                command=self.control3)
            self.antw4 = Button(window, text=self.a4, border=0, bg='#3D32FF', fg='white', font=("Arial", 14), width=39,
                                command=self.control4)

            self.antw1.grid(column=0, row=1, pady=(8, 5))
            self.antw2.grid(column=0, row=2, pady=5)
            self.antw3.grid(column=0, row=3, pady=5)
            self.antw4.grid(column=0, row=4, pady=5)

            if self.a1 == self.Ra:
                self.RaBtn = self.antw1
            elif self.a2 == self.Ra:
                self.RaBtn = self.antw2
            elif self.a3 == self.Ra:
                self.RaBtn = self.antw3
            elif self.a4 == self.Ra:
                self.RaBtn = self.antw4
            self.Fragen.pop(randNum)
        else:
            clear()
            lb = Label(window,
                       text="You have " + str(self.right) + " of " + str(self.Max) + " right answers",
                       font=("Arial", 14), bg='#6D81FF')
            lb.grid(column=0, row=0, padx=175, pady=(170, 15))
            zumMenu = Button(window, text="Menu", font=("Arial", 35), command=menuCreator, bg='#3D32FF', foreground='white')
            zumMenu.grid(column=0, row=1)

    def control1(self):
        if self.lock == False:
            if self.Ra != self.a1:
                self.antw1.configure(bg="red")
            else:
                self.antw1.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True

    def control2(self):
        if self.lock == False:
            if self.Ra != self.a2:
                self.antw2.configure(bg="red")
            else:
                self.antw2.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True

    def control3(self):
        if self.lock == False:
            if self.Ra != self.a3:
                self.antw3.configure(bg="red")
            else:
                self.antw3.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True

    def control4(self):
        if self.lock == False:
            if self.Ra != self.a4:
                self.antw4.configure(bg="red")
            else:
                self.antw4.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True


class Menu:
    def __init__(self):
        clear()
        width = 100
        height = 100
        image = PhotoImage(file="Quiz_Image.png").zoom(15).subsample(32)
        canvas = Canvas(window, width=width, height=height, bg='#6D81FF', bd=0, highlightthickness=0)
        canvas.create_image(width / 2, height / 2, image=image)
        canvas.grid(column=0, row=0)

        title = Label(window, text="EURO GAME", font=("Calibri", 40), bg='#6D81FF', fg='white').grid(row=1, column=0)

        self.Quiz = Button(window, text="Start Quiz", font=("Calibri", 25), bg='#3D32FF', fg='white',
                           command=quizCreator,
                           width=15, height=3)
        label_subtitle = Label(window, text="Do you want to play ?", font=("Calibri", 25), bg='#6D81FF',
                               fg='white').grid(row=3, column=0)
        self.Quiz.grid(column=0, row=2, padx=175)


def menuCreator():
    m = Menu()


def quizCreator():
    q = Quiz(questions)


menuCreator()
window.mainloop()
