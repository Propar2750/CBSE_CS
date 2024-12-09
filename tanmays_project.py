from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
import os


score_calculator = []
i = 0
solution = ""
name_entry=""

# THE LOGIN SCREEN


home = Tk()

home.title("Login Page")
home.configure(background="darkgreen")

connection = mysql.connector.connect(host="localhost", user="root", password="amity")
cursor = connection.cursor()
cursor.execute("create database if not exists qa")
cursor.execute("use qa")
cursor.execute("create table if not exists datas(Name varchar(60),Answer varchar(60))")
cursor.execute("create table if not exists scores(Score int,Name varchar(30))")
connection.close()

play_room1 = 0
# THE CHECK FUNCTION

def check():
    global name_entry
    # GETTING DATA FROM THE ENTRIES

    username = user_name.get()
    username.lower()
    userpass = user_pass.get()
    userpass.lower()

    # FOR ADMIN

    if username == "admin" and userpass == "pass":

        home.destroy()  # DESTROYING THE LOGIN PAGE
        admin_page = Tk()  # CREATING THE ADMIN PAGE

        admin_page.title("Admin Page")  # SETTING THE TITLE OF THE PAGE
        admin_page.configure(background="darkgreen")  # SETTING THE BACKGROUND COLOUR

        # SETTING THE LABEL OF THE PAGE(TITLE)

        # THE LABEL FOR THE QUESTIONS ENTRY

        Label_1 = Label(admin_page, text="Write Question here", font=('arial', 10), bd=9)
        Label_1.grid(row=0, column=0)

        # THE ENTRY IN WHICH THE QUESTION WILL BE TAKEN

        question = Entry(admin_page, width=15)
        question.grid(row=0, column=1)

        # THE LABEL FOR THE ANSWER ENTRY

        answer = Label(admin_page, text="Enter the Answer:", font=('arial', 10), bd=9)
        answer.grid(row=1, column=0)

        name_search = Label(admin_page, text="Name", font=('arial', 10), bd=9)
        name_search.grid(row=0, column=3)

        name_en = Entry(admin_page, width=15)
        name_en.grid(row=0, column=4)

        # THE ENTRY FOR THE ANSWER

        answer_entry = Entry(admin_page, width=15)
        answer_entry.grid(row=1, column=1)

        # THE FUNCTION FOR CLOSING THE WINDOW

        def exit_func():
            try:
                confirm = messagebox.askyesno("Confirm", "Are you sure you want to exit")
                if confirm > 0:
                    admin_page.destroy()
            except Exception as e:
                messagebox.showerror("Error", "Something Went wrong\nCheck the entries again or try again")

        # THE FUNCTION FOR CLEARING THE DATA IN THE ENTRIES

        def clear_func():
            try:
                question.delete(0, END)
                answer_entry.delete(0, END)
                name_en.delete(0, END)
            except Exception as e:
                messagebox.showerror("Error", "Something Went wrong\nCheck the entries again or try again")

        # THE FUNCTION FOR ADDING TO THE DATABASE

        def add_in_data():
            try:
                # GETTING THE DATA FROM ENTRIES
                qdata = question.get()
                adata = answer_entry.get()

                # ADDING THE IF ELSE FOR IF THE DATA FEILDS ARE EMPTY

                if qdata == "" or adata == "":
                    messagebox.showwarning("Incomplete Feilds",
                                           "Please make sure that you have filled both the entries")
                else:
                    connection = mysql.connector.connect(host="localhost", user="root", password="amity",
                                                         db="qa")
                    cursor = connection.cursor()
                    cursor.execute("insert into datas(name, answer)values(%s, %s)", (qdata, adata))
                    connection.commit()

                    question.delete(0, END)
                    answer_entry.delete(0, END)

                    messagebox._show("Insertion Complete", "Your data has been succesfully added to the database")
                    connection.close()

                    connection.close()
            except Exception as e:
                messagebox.showerror("Error", "Something Went wrong\nCheck the entries again or try again")

        # THE SHOW DATA FUNCTION

        def show_func():
            try:
                connection = mysql.connector.connect(host="localhost", user="root", password="amity", db="qa")
                cursor = connection.cursor()
                cursor.execute("select * from datas")
                data = cursor.fetchall()

                cursor.close()

                if data == []:
                    messagebox.showerror("No Data", "There is no data yet")
                else:
                    messagebox._show("Questions",data)
                    

                connection.close()
            except Exception as e:
                messagebox.showerror("Error", "Something Went wrong\nCheck the entries again or try again")

        # THE DELETE ENTRY FUNCTION

        def del_func():
            qdata = str(question.get())
            connection = mysql.connector.connect(host="localhost", user="root", password="amity", db="qa")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM datas where name=%s", (qdata,))
            da = cursor.fetchall()
            cursor.close()

            if qdata == "":
                messagebox.showwarning("Delete Status", "The question is important for deletion")
            elif da == []:
                messagebox.showerror("Invalid Entry", "No such question is there ")
            else:
                try:

                    connection = mysql.connector.connect(host="localhost", user="root", password="amity",
                                                         db="qa")
                    cursor = connection.cursor()
                    cursor.execute("delete from datas where name='" + qdata + "'")
                    connection.commit()

                    question.delete(0, END)
                    answer_entry.delete(0, END)

                    messagebox._show("Deletion Succesful", "The Question has been succesfully removed")
                    connection.close()
                except Exception as e:
                    messagebox.showerror("Error", "Something Went wrong\nCheck the entries again or try again\n")

        # THE UPDATE QUESTION FUNCTION

        def update_func_quest():
            qdata = question.get()
            adata = answer_entry.get()

            if adata == "":
                messagebox.showwarning("Unfilled Entries", "For updating the questions the answer needs to be filled")
            else:
                try:

                    connection = mysql.connector.connect(host="localhost", user="root", password="amity",
                                                         db="qa")
                    cursor = connection.cursor()
                    cursor.execute("UPDATE datas SET name=%s where answer=%s;", (qdata, adata))
                    connection.commit()

                    question.delete(0, END)
                    answer_entry.delete(0, END)

                    messagebox._show("Update Status", "The question is succesfully updated")
                except Exception as e:
                    messagebox.showerror("Error", "Something Went wrong\nCheck the entries again or try again")

        def update_func_ans():

            qdata = question.get()
            adata = answer_entry.get()
            try:

                if qdata == "":
                    messagebox.showwarning("Unfilled Entries", "For updating the answer the question is neccasary")

                else:
                    connection = mysql.connector.connect(host="localhost", user="root", password="amity",
                                                         db="qa")
                    cursor = connection.cursor()
                    cursor.execute("UPDATE datas SET answer=%s where name=%s;", (adata, qdata))
                    connection.commit()

                    question.delete(0, END)
                    answer_entry.delete(0, END)

                    messagebox._show("Update Status", "The answer is succesfully updated")
            except Exception as e:
                messagebox.showerror("Error", "Something Went wrong\nCheck the entries again or try again" + e)

        def show_attempt():
            connection = mysql.connector.connect(host="localhost", user="root", password="amity", db="qa")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM scores")
            score_data = cursor.fetchall()
            cursor.close()
            if score_data == []:
                messagebox.showerror("No Data", "There is no data yet")
            else:
                messagebox._show("Response data",score_data)
                

            connection.close()

        def search_student():
            name = name_en.get()
            name = str(name)

            if name == "":
                messagebox.showerror("Data unfilled", "Name needs to be fiiled to search")
            else:

                connection = mysql.connector.connect(host="localhost", user="root", password="amity", db="qa")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM scores WHERE name=%s", (name,))
                score_data = cursor.fetchall()

                if score_data == []:
                    messagebox.showwarning("No Data", "There is no such name")
                else:
                    messagebox._show("Student data",score_data)

                connection.close()

        # THE BUTTONS

        # THE EXIT BUTTON
        search_student = Button(admin_page, text="Search by name", font=('arial', 18), width=20, bg="orange",
                                command=search_student)
        search_student.grid(row=1, column=4)

        exit_bt = Button(admin_page, text="Exit", font=('arial', 18), width=10, bg="orange", command=exit_func)
        exit_bt.grid(row=4, column=0)

        # THE CLEAR BUTTON

        clear_bt = Button(admin_page, text="Clear", font=('arial', 18), width=10, bg="orange", command=clear_func)
        clear_bt.grid(row=6, column=0)

        # THE ADD BUTTON

        add_bt = Button(admin_page, text="Insert question", font=('arial', 18), width=20, bg="orange", command=add_in_data)
        add_bt.grid(row=4, column=1)

        # THE SHOW BUTTON

        show_bt = Button(admin_page, text="Show all questions", font=('arial', 18), width=20, height=1, bg="orange", command=show_func)
        show_bt.grid(row=6, column=1)

        # THE DELETE BUTTON

        del_bt = Button(admin_page, text="Delete question", font=('arial', 18), width=20, bg="orange", command=del_func)
        del_bt.grid(row=4, column=2)

        # THE UPDATE QUESTION BUTTON

        upd_q = Button(admin_page, text="Update Ques", font=('arial', 18), width=20, bg="orange",
                       command=update_func_quest)
        upd_q.grid(row=6, column=2)

        # THE UPDATE ANSWER BUTTON

        upd_a = Button(admin_page, text="Update Ans", font=('arial', 18), width=10, bg="orange",
                       command=update_func_ans)
        upd_a.grid(row=4, column=3)

        # THE SCORE ADDERS

        score_button = Button(admin_page, text="Show Marks", font=('arial', 18), width=10, bg="orange",
                              command=show_attempt)
        score_button.grid(row=6, column=3)

        # THE SEARCH STUDENT

        # THE ADMIN PAGE MAINLOOP
        admin_page.mainloop()


    elif username == "user" and userpass == "play":
        home.destroy()
        user_page = Tk()

        user_page.title("Play Page")
        user_page.configure(background="darkgreen")

        def go_in_quiz():
            global i
            global ans1
            global ans
            global play_room1
            global name_entry
            name = name_entry.get()
            name = str(name)
            user_page.destroy()
            user_page.mainloop()
            

            connection = mysql.connector.connect(host="localhost", user="root", password="amity", db="qa")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM datas")
            data = cursor.fetchall()
            cursor.close()
            connection.close()
            number = len(data)
            data_num = number + 1

            play_room = Tk()
            play_room.title("Quiz Page")
            play_room.configure(background="darkgreen")

            questi = data[i][0]
            user_data = str(questi)
            ans = data[i][1]

            qlabel = Label(play_room, text=f"Question: {user_data}", font=('arial', 10), bd=18)
            qlabel.grid(row=0, column=0)
            ans1 = Entry(play_room, width=15)
            ans1.grid(row=0, column=1)

            def submit_answer():
                global score
                global userans
                global ans1
                global ans
                global i
                global play_room1
                try:


                    userans = ans1.get()
                    try:
                        play_room.destroy()

                    except:
                        pass
                    try:
                        play_room1.destroy()
                    except:
                        pass

                    if i != len(data) -1:
                        if userans == str(ans):

                            messagebox._show(title = "CORRECT ANSWER", message=f'CORRECT ANSWER')
                            score_calculator.append("True")

                            play_room1 = Tk()
                            play_room1.title("Quiz Page")
                            play_room1.configure(background="darkgreen")

                            i += 1

                            questi = data[i][0]
                            user_data = str(questi)
                            ans = data[i][1]

                            qlabel = Label(play_room1, text=f"Question: {user_data}", font=('arial', 10), bd=18)
                            qlabel.grid(row=0, column=0)

                            ans1 = Entry(play_room1, width=15)
                            ans1.grid(row=0, column=1)

                            submit = Button(play_room1, text="Submit", font=('arial', 18), width=10, bg="orange",
                                            command=submit_answer)
                            submit.grid(row=3, column=0)

                            play_room1.mainloop()


                        else:
                            messagebox._show(title = "WRONG ANSWER", message=f'{str(ans)} was the correct answer')

                            play_room1 = Tk()
                            play_room1.title("Quiz Page")
                            play_room1.configure(background="darkgreen")

                            i += 1
                            questi = data[i][0]
                            user_data = str(questi)
                            ans = data[i][1]

                            qlabel = Label(play_room1, text=f"Question: {user_data}", font=('arial', 10), bd=18)
                            qlabel.grid(row=0, column=0)

                            ans1 = Entry(play_room1, width=15)
                            ans1.grid(row=0, column=1)

                            submit = Button(play_room1, text="Submit", font=('arial', 18), width=10, bg="orange",
                                            command=submit_answer)
                            submit.grid(row=3, column=0)

                            play_room1.mainloop()

                    else:
                        if userans == str(ans):

                            messagebox._show(title = "CORRECT ANSWER", message=f'CORRECT ANSWER')
                            score_calculator.append("True")
                        else:
                            messagebox._show(title = "WRONG ANSWER", message=f'{str(ans)} was the correct answer')
                    play_room.mainloop()
                except IndexError:
                    pass
                score = str(len(score_calculator))
                messagebox._show("Your Score was", score)

                connection = mysql.connector.connect(host="localhost", user="root", password="amity", db="qa")
                cursor = connection.cursor()
                cursor.execute("insert into scores(score, name)values(%s, %s)", (score, name))
                connection.commit()
                connection.close()

                messagebox._show("Succesful", "Your Data has been sent to the teacher")
                os._exit(0)

            submit = Button(play_room, text="Submit", font=('arial', 18), width=10, bg="orange",
                            command=submit_answer)
            submit.grid(row=3, column=0)

        play = Button(user_page, text="Enter Quiz", font=('arial', 18), width=10, bg="orange", command=go_in_quiz)
        play.grid(row=5, column=5)

        name_label = Label(user_page, text="Enter your name:", font=('arial', 10), bd=18)
        name_label.grid(row=2, column=0)

        name_entry = Entry(user_page, width=10)
        name_entry.grid(row=2, column=1)

    else:
        messagebox.showerror("Access Denied", "Invalid Passoword or Username")


# THE MAINFRAME OF THE LOGIN PAGE
MainFrame = Frame(home, width=600, height=100, bd=1, relief=SOLID)
MainFrame.pack(side=TOP, pady=20)

# THE TITLE LABLE AND THE MIDDLE FRAME

w_to = Label(MainFrame).pack(side="left")
lbl = Label(MainFrame, text="Login Screen", font=('arial', 38), width=600)
lbl.pack()
MidFrame = Frame(MainFrame, width=600)
MidFrame.pack(side=TOP, pady=50)

# THE USERNAME AND PASSWORD VARIABLES

USER_NAME = StringVar()
USER_PASS = StringVar()

# THE FRAME ON WHICH LABEL AND TEXT

lbl_Name = Label(MidFrame, text="Name:", font=('arial', 25), bd=18)
lbl_Name.grid(row=0)
lbl_Pass = Label(MidFrame, text="Password:", font=('arial', 25), bd=18)
lbl_Pass.grid(row=1)

# THE ENTRIES OF NAME AND PASSWORD

user_name = Entry(MidFrame, textvariable=USER_NAME, font=('arial', 25), width=15)
user_name.grid(row=0, column=1)
user_pass = Entry(MidFrame, textvariable=USER_PASS, font=('arial', 25), width=15, show="*")
user_pass.grid(row=1, column=1)

# THE BOTTOM FRAME

BottomFrame = Frame(MainFrame, width=600)
BottomFrame.pack(side=TOP, pady=20)

# THE BUTTON WHICH WILL CHECK THE USERNAME AND PASSWORD

checker = Button(BottomFrame, text="Enter", font=("arial", 18), command=check, bg="orange")
checker.grid(row=2, column=3, pady=20)

#IMAGE
image=Image.open("riddler.jpeg")
resize_image=image.resize((300,300))
img=ImageTk.PhotoImage(resize_image)
image_label=Label(image=img)
image_label.image=img
image_label.pack()

# THE LOGIN PAGE MAINLOOP

home.mainloop()
