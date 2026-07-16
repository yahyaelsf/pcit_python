import sqlite3 as sql
# # app.db
# db = sql.connect("app.db")
# cr = db.cursor()
# # create table
# cr.execute("create table if not exists users (id integer primary key ,name text , email text)")
# # add data to table
# cr.execute("insert into users (name , email) values ('yahya' , 'yahya@gmail.com')")
# # edit data from table
# cr.execute("update users set name = 'yahyaelsaftawi' where id = '1' and name = 'yahya'")
# # delete from table 
# cr.execute("DELETE FROM users WHERE id = '2'")
# # delete table 
# cr.execute("drop table users")
# db.commit()
# db.close()
db = sql.connect("app.db")
cr = db.cursor()
cr.execute("create table if not exists users (id integer primary key ,name text , email text)")
user_message = """
choise form choises :
1 => create user 
2 => edit user 
3 => delete user
4 => show_users 
5 => exit
"""
uid = '2'
def commit_and_clode():
    db.commit()
    db.close()
def add_user():
    name = input("Enter you name: ")
    email = input("Enter you email: ")
    cr.execute("insert into users (name , email) values ( ? , ?)" , (name , email ))
    commit_and_clode()
def edit_user():
    name = input("Enter you name: ")
    new_name = input("Enter your new name: ")
    cr.execute("update users set name = ? where name = ? and id = ? " , (new_name , name , uid ) )
    commit_and_clode()
def delete_user():
    name = input("Enter you name: ")
    cr.execute("delete from users where name = ? and id = ? " , ( name , uid ) )
    commit_and_clode()

def show_users():
    cr.execute("select * from users")
    data = cr.fetchall()
    for row in data :
        print(f"id is {row[0]} ," ,end=" ")
        print(f"name is {row[1]} ," , end= " ")
        print(f"email is {row[2]}.")
    
user_input = input(user_message)
user_choises = ["1" , "2" ,"3" , "4"]
if user_input in user_choises :
    if user_input == "1" :
        add_user()
    elif user_input == "2" :
        edit_user()
    elif user_input == "3" : 
        delete_user()
    elif user_input == "4" : 
        show_users()
        
    else : 
        print("app is closed")
        commit_and_clode()

    
else : 
    print("Error ")