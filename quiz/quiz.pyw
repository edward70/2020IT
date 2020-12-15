from tkinter import *
from tkinter import messagebox
import json

class Quiz(Tk): # quiz class
    def __init__(self): # constructor
        super().__init__() # init gui
        self.title("Quiz") # set title

        self.score = 0 # global score

        # array containing data for every screen
        with open("questions.json") as f:
            self.screen_contents = json.loads(f.read())

        self.inscreen = InputScreen(self) #input screen
        self.inscreen.grid(row=0) # put in grid
        
    def start(self):
        self.name = self.inscreen.namevar.get() # get name
        if len(self.name) == 0: # check if entry is empty
            messagebox.showerror("Bad input", "Please enter your name") # name error
            return # return from function
        
        try: # handle conversion error
            yearlevel = int(self.inscreen.yearvar.get()) # get year

            if yearlevel != 10: # check in year 10
                messagebox.showinfo("Wrong year level", "This is a quiz for students in year 10.") # not in year 10 message
                return
        except:
            messagebox.showerror("Bad input", "You did not enter an integer for your year level eg. 10.")
            return # incorrect entry
        self.inscreen.grid_forget() # clear screen
        QuizScreen(self, self.screen_contents.copy()).grid(row=0) # initialise with a copy so the original screens data is restored when quiz is restarted

class InputScreen(Frame): # class
    def __init__(self, parent): # constructor
        super().__init__(parent) # init frame
        self.parent = parent # parent save

        Label(self, text='Please enter your name and year level', font=('Arial', 10, 'bold')).grid(row=0) # text label
        Label(self, text='Name:').grid(row=1)
        self.namevar = StringVar()
        Entry(self, textvariable=self.namevar).grid(row=2)
        Label(self, text='Year Level:').grid(row=3)
        self.yearvar = StringVar()
        Entry(self, textvariable=self.yearvar).grid(row=4)
        Button(self, text="Submit", command=self.parent.start).grid(row=5) # submit button
        

class QuizScreen(Frame): # screen class
    def __init__(self, parent, screens): # constructor
        super().__init__(parent) # init frame

        self.screens = screens # screens object property

        self.incorrect = 0 # count number of incorrect tries for screen object instance

        question = screens[0][0] # get question from top index of screens array
        self.qlist = screens[0][1] # get possible answer list from top index of screens array
        self.answer = screens[0][2] # get answer index

        if len(screens[0]) == 4:
            # reference: https://stackoverflow.com/a/50303149
            self.image = PhotoImage(file=screens[0][3]) # prevent image deletion by GC
            Label(self, image=self.image).grid(row=0) # add image

        self.parent = parent # store reference to parent object

        score_text = "Score: {}".format(self.parent.score) # text for score

        Label(self, text=score_text).grid(row=1) # pack score

        Label(self, text=question, font=('Arial', 10, 'bold')).grid(row=2) # pack question

        self.answered = IntVar(self) # answer is the index of the question
        self.answered.set(0) # default answer is the first one

        self.radio_array = [] # array of radio buttons
        for i, x in enumerate(self.qlist): # iterate array
            self.radio_array.append(Radiobutton(self, text=x, variable=self.answered, value=i)) # create radiobutton with answer as its index
            self.radio_array[-1].grid(row=3+i) # add it

        Button(self, text="Submit", command=self.submit).grid(row=7) # pack submit button

    def next_screen(self): # next screen function
        if len(self.screens) > 1: # if there are more screens
            self.screens.pop(0) # remove to index of screens so next screen will be fetched
            self.grid_forget() # destroy current screen
            QuizScreen(self.parent, self.screens).grid(row=0) # pack next screen
        else:
            # ask user if they want to restart
            restart = messagebox.askquestion("Quiz Finish", "Congratulations {}! You finished with score of {}. Do you want to restart?".format(self.parent.name, self.parent.score))
            if restart == "yes": # check if they want to restart
                self.parent.score = 0 # reset score
                # reinitialise quizscreen with fresh screen data
                self.grid_forget() # remove current screen
                QuizScreen(self.parent, self.parent.screen_contents.copy()).grid(row=0)
            else:
                exit(0) # quit

    def submit(self): # submit function
        if self.answered.get() == self.answer: # check answer
            self.parent.score += 1 # increment score
            self.radio_array[self.answered.get()].config(fg="green") # mark question green by fetching radio using response index
            messagebox.showinfo("Correct", "Your current score is {}".format(self.parent.score)) # correct message
            self.next_screen() # go to next screen
        else:
            self.incorrect = self.incorrect + 1 # increment incorrect counter
            self.radio_array[self.answered.get()].config(fg="red") # mark question red by fetching radio using response index
            if self.incorrect == 3: # check if there's 3 incorrect answers
                messagebox.showinfo("Too many incorrect answers", "The correct answer is '{}'.".format(self.qlist[self.answer])) # tell them the answer using answer index to get the answer text
                self.next_screen() # go to the next screen
                return # return
            else:
                messagebox.showinfo("Incorrect", "You entered an incorrect answer.") # incorrect message

if __name__ == "__main__": # check file is called not imported
    Quiz().mainloop() # start mainloop
