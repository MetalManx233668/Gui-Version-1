from tkinter import*
import random
names = []
global questions_answers
asked = []

questions_answers = {
    1: ["What is the biggest continent in the world?", 'South America', 'Asia','Europe', 'Antartica' ,'Asia',1],
    2: ["Which state is Niagra falls in?",'Calafornia','New York','Los Angeles', 'Florida','New York',2],
    3: ["Where would you find the leaning tower of pisa?", 'Italy','Spain', 'Greece','Sweden','Italy',4],
}

def randomiser():
    global qnum
    qnum = random.randint(1,3)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomiser()
   

class QuizStarter:
  def __init__(self, parent):
    background_color="lightgrey"
   
    self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    self.heading_label=Label(self.quiz_frame, text = "The Geography Quiz", font =( "Tw Cen MT","18","bold"))
    self.heading_label.grid(row= 0, padx=20)

    self.var1=IntVar()

    self.user_label=Label(self.quiz_frame, text="Please Enter your Username Below: ", font=( "Tw Cen MT","18","bold"),bg=background_color)
    self.user_label.grid(row=1, padx=20, pady=20)

    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=2,padx=20, pady=20)

    self.continue_button = Button(self.quiz_frame, text="Continue", font=( "Helvetica","13","bold"), bg="darkgrey",command=self.name_collection)
    self.continue_button.grid(row=3,padx=20, pady=20)

  def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()
        Quiz(root)

class Quiz:

   def __init__(self, parent):
    background_color="lightgrey"
   
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()

    randomiser()

    self.question_label=Label(self.quiz_frame, text = questions_answers[qnum][0], font =( "Tw Cen MT","18","bold"))
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.var1=IntVar()

    self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb1.grid(row=1, sticky=W)

    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb2.grid(row=2, sticky=W)

    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb3.grid(row=3, sticky=W)

    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb4.grid(row=4, sticky=W)

    self.confirm_button = Button(self.quiz_frame, text="Confrim",bg="white",command=self.test_progress)
    self.confirm_button.grid(row=6)
     
     
   def questions_setup(self):
     randomiser()
     self.varl.set(0)
     self.question_label.config(text=questions_answers[qnum][0])
     self.rb1.config(text=questions_answers[qnum][1])
     self.rb2.config(text=questions_answers[qnum][2])
     self.rb3.config(text=questions_answers[qnum][3])
     self.rb4.config(text=questions_answers[qnum][4])

 
   def test_progress(self):
      global score
      scr_label=self.score_label
      choice=self.var1.get()
      if len(asked)>9:
        if choice == questions_answers[qnum][6]:
          score +=1
          sc_label.configure(text=score)
          self.confirm_button.config(text-"Confirm")
        else:
          score+=0
          sc_label.configure(text-"The correct answer was: "+ questionsanswers[qnum][5] )
          self.confirm_button.config(text-"confirm")
     
      else:
            if choice==0:
              self.confirm_button.config(text-"Try Again, you didn't select an option then submit again" )
              choice=self.var1.get()
            else:
              if choice == questions_answers[qnum][6]:
                score+=1
                sc_label.configure(text=score)
                self.confrim_button.config(text-"confirm")
                self.questions_setup()
 
              else:
                  score+=0
                  scr_label.configure(text-"The correct answer was: "
                                      + questions_answers [qnum][5])
                  self.confrim_button.config(text-"Confirmn")
                  self.questions_setup()
       
if __name__ == "__main__":
  root = Tk()
  root.title("NZ Road Rules Quiz")
  quiz_instance = QuizStarter(root)
  root.mainloop()

from tkinter import *

from PIL import Image, ImageTk



class Start:
    def __init__(self, parent):
        self.quiz_frame =Frame(parent)
        self.quiz_frame.pack()

if __name__== "__main__":
    window = Tk()
    window.title("12CSC Quiz")
    window.geometry("600x600")
    bg_image = Image.open("img2.jpg")
    bg_image = bg_image.resize((1000,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Start(window)

    window.mainloop()