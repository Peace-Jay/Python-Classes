print("*******Starting*******************")
user_choice = input('Do you want to check score? Enter Y/N \n-->')

invalid_choice = True

while invalid_choice:
    if user_choice == 'Y' or user_choice == 'N':
        invalid_choice = False
    else:
        print("Invalid Choice! Enter Y or N")
        user_choice = input('Do you want to check score? Enter Y/N \n-->')

while user_choice == 'Y':
    score = int(input('Enter Score \n-->'))
    if score >= 70 and score <=100:
        print('Grade is A')
    elif score >=60 and score <=69:
        print('Grade is B')
    else:
        print('hmmmmmmmmm')
    
    invalid_choice = True
    user_choice = input('Do you want to check score? Enter Y/N \n-->')

    while invalid_choice:
        if user_choice == 'Y' or user_choice == 'N':
            invalid_choice = False
        else:
            print("Invalid Choice! Enter Y or N")
            user_choice = input('Do you want to check score? Enter Y/N \n-->')

    
    
    
print('*******Exiting***************')