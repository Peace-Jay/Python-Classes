print("*******Starting*******************")
user_choice = input('Do you want to check score? Enter Y/N \n-->')


while user_choice != 'N':
    score = int(input('Enter Score \n-->'))
    if score >= 70 and score <=100:
        print('Grade is A')
    elif score >=60 and score <=69:
        print('Grade is B')
    else:
        print('hmmmmmmmmm')
    user_choice = input('Do you want to check score? Enter Y/N \n-->')

print('*******Exiting***************')