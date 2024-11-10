import json

with open('files\questions.json','r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index,alternative in enumerate(question["Alternatives"]):
        print(index + 1 ,"-" ,alternative)
    user_choice=int(input("Enter your answer: "))
    question["user_choice"]=user_choice

score=0
for index,question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score+=1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{result} {index + 1} - Your Answer : {question['user_choice']}," \
              f"Correct answer is {question['correct_answer']}"
    print(message)
print(data)
print(score ,"/",len(data))


