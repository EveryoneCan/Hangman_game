import SelectHints.hints
import MysqlDb.database
import random

print("----WELCOME TO HANGMAN GAME----")
print('')
#Make a list
list1=["elephant","car","train","aeroplane","four","school","sister","chair","telephone",
       "television","radio","glass","paper","pencil","library","peacock","trees","eraser",
       "slippers","butterfly","sofa"]


#Get a random word
x=0
x=random.randrange(21)
get_word=list1[x]

#Input the name of the player
name1=input("Enter the player name:-  ")
print('')

word=get_word

SelectHints.hints.word_hint(get_word,list1)

#Get the length of the word
length1=len(get_word)
len_word=len(get_word)

length2=range(0,length1)

#Get an empty list
list2=[]

#Get _ in the seperate word
for underscore in length2:
    underscore="_"
    ccc=list2.append(underscore)

#Remove commas and brackets in the list 
separator=' '
sep=separator.join(list2)

#Print undescores and print remaining turns
print("Word : ",sep)
print(length1," turns remain")


#Looping of while and for
len1=length1
turn_use=0
while(len_word!=0):
    user_input=input("letter : ")
   
       
    for x in range(length1):
        aa=(get_word[x])
            
            
        if aa==user_input: 
            list2[x]=user_input
            
            list2.append
           
        else:
            len1=len1-1

            
     #Counting turns       
    if user_input not in get_word or user_input=='':
        len_word=len_word-1
        print(len_word," turns remain")

    else:
        len_word=len_word
        print(len_word," turns remain")

    #Remove commas and brackets in the list
    separator1=''
    sep1=separator1.join(list2)

    separator=' '
    sep=separator.join(list2)
    print(sep)

    #If inputted letters=get word(while loop end)
    if sep1==get_word:
        len_word=0

    #To count the remaining turns        
    turn_use=turn_use+1
       

#Display won or lose
if sep1==get_word:
     state='You won!'
else:
    state='You lost!'
    
print(state)



#Display the word tha ran through out the program           
print('word is :',get_word,"")


#Connect to the database
MysqlDb.database.connect_database(name1,word,length1,turn_use,state)

            
       
    
    

    
