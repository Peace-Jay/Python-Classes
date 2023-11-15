students_details = {
    "names" : {
        "firstname" : ['Shola', "Mitchell", "Fiona"],
        "lastname" : ["Emmanuel", "Francis", "Miguel"],
        "middlename": ["Joe", "Smith", "Mary"]
    },
    "age" : [12, 17, 20],
    "scores" : {
        "maths" : [90,61,70],
        "english" : [80, 90, 70],
        "python" : [70, 80, 90]
    }
}

grade = None
english_grade = None


first_name = students_details['names']['firstname'][1]
last_name = students_details['names']['lastname'][1]
maths_score = students_details["scores"]['maths'][1]
english_score = students_details["scores"]['english'][1]

if maths_score >= 70 and maths_score <=100:
    grade = 'A'
elif maths_score >=60 and maths_score <=69:
    grade = 'B'

if english_score >= 70 and english_score <=100:
    english_grade = 'A'
elif english_score >=60 and english_score <=69:
    english_grade = 'B'

# print(f"{first_name} {last_name} scored \n {maths_score} in Math and had {grade} \n {english_score} in English and had {english_grade}")

print(f" ************STUDENTS REPORTS***********************")
print("*****************************************************")
print(f"NAME: {first_name} {last_name} \nMATH : {maths_score} GRADE: {grade}\nENGLISH: {english_score} GRADE: {english_grade}")
print("*****************************************************")