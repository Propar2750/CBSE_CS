import mysql.connector as sqltor
mycon = sqltor.connect(host="localhost",user="root",passwd="#12tabparv")
cursor = mycon.cursor()

# Database contains tables with format Database --> users table , table_user_1(_2)(_3) etc.
def data_base_setup():
    if mycon.is_connected():
        print("Successfully connected")
    cursor.execute("Create Database if not exists planner")
    cursor.execute("Use planner")
    cursor.execute("CREATE TABLE users (userid int, username varchar, breakfasttime time, lunchtime time, dinnertime time, starttime time, endtime time);")
    cursor.execute("select * from users")
    # On a new pc


def setup():
    cursor.execute("Use planner")
    input_1 : input("Do you have a user id (y/n)")
    if input_1.lower().startswith('y'):
        global user_id
        user_id = input("Please enter your user_id")
    elif input_1.lower().startswith('n'):
        breakfast_time = input("Please enter your breakfast time in 24hour format 16:09 \n")
        lunch_time = input("Please enter your lunch time in 24hour format 16:09 \n")

        dinner_time = input("Please enter your dinner time in 24hour format 16:09 \n")




def new():
    x = input("Arguments")

data_base_setup()
