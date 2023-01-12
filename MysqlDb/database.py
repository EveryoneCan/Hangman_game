#This is from the main,py program
def connect_database(name1,word,length1,turn_use,state):
    import mysql.connector
    import random
    
    #Open database connection with a dictionary
    conDict={'host':'localhost',
             'database':'hangman_game',
             'user':'root',
             'password':''}

    db=mysql.connector.connect(**conDict)

    #Prepare a cursor  object using cursor () method
    cursor=db.cursor()

    #Execute SQL query using eexecute () method
    recno=random.randrange(1000,9999)
    mysqltxt="INSERT INTO player_detail (rec_no,name,word_guessed,turns_provided,turns_used,win_lost) VALUES(%s,%s,%s,%s,%s,%s)"
    myval=(recno,name1,word,length1,turn_use,state)
    cursor.execute(mysqltxt,myval)

    #Commit the change, end the program and returnning
    db.commit()
    print(cursor.rowcount,"Record added to the database")
    db.close()
    return
