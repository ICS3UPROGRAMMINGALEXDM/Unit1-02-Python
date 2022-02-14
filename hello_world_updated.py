"""
Your module description
"""

#saying Hello
print("Hello Ms Raffin!")



while True:
    #asking for user input
    ans = input("How are you?\n").strip().lower()
    
    #if statement that determines how to respond
    if ans == 'good':
        print ("That's good to hear!")
        break
    elif ans == 'bad':
        print('Oh, I\'m sorry to hear that.')
        break
    else:
        print("I\'m sorry, I\'m not the smartest program at the moment. I could not understand what you meant. Try using \"Good\" or \"Bad\" for now.")