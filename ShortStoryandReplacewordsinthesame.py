#Short story 
#Accept user to enter a short story or essay about about 1000 letters
usr_story = input("Hi folks, go ahead and start writing a 500 words story\n")

#Convert the entered story to lower case
usr_story = usr_story.lower()

#Counting the total number of words in the entered story 
#split() method is used to split the whitespaces between each words
len_story = len(usr_story.split())

#If the lenght exceed 1000 words display error message
if(len_story > 500): 
    print("Your story is lenghty!")
    print("Thank you! Bye!")
    unsuccessful = 1
    
#Else display success message
elif(len_story <= 500):
    print("Great! you have compeleted your story!")
    successful = 1

if successful == 1:
    chg_story = input("Do you like to replace something on your story?(Yes/No)")
    chg_story = chg_story.upper()
    
    if(chg_story) == 'YES':
        old_word = input("Enter the old word you would like to replace: ")
        new_word = input("Enter the new word you would like to replace the old word with: ")
#converting the entered words to lower case        
        old_word = old_word.lower()
        new_word = new_word.lower()
#to check if the entered word is present in the story to replace with new word
        if old_word in usr_story:
#if found replace the old one with the new word using replace method
            usr_story = usr_story.replace(old_word,new_word)
            print("Your changes has been made")
            print("Thank you! Bye!")
        else:
            print("Entered word for replacing is not in the above story")
    elif(chg_story) == 'NO':
        print("Your story is stored! Thank you!")

    else:
        print("Thank you! Bye!")
else:
    print("Thank you! Bye!")
