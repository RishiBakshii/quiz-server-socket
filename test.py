import random

question={"what is the color of apple":"red",
          "what is color of plants ":'green'
          }
random_index=random.randint(0,len(question)-1)
question_list=list(question.keys())

print(question_list[random_index])
player_answer=input("\nanswer : .. ")

if player_answer==question[question_list[random_index]]:
    print("correct")
else:
    print("wrong")


