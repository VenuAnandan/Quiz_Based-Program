ques = ("Where chennai as located at India? :","what is the largest beach in India? :","which city is called 'Pink City'? :","Biggest river in india? :","How many bones are in the human body? :")
opt = (("A.TamilNadu","B.Kerala","Andhra"),("A.goa","B.pondy","C.Merina"),("A.Chennai","B.Rajastan","C.Karnadagaa"),("A.Kangai","B.Yamunai","C.Kothavari"),("A.207","B.206","C.210"))
ans = ("A","C","B","A","B")

gues = []
score = 0
ques_num = 0


for question in ques:
    print(question)
    for option in opt[ques_num]:
        print(option)

    guesses = input("Enter (A,B,C) :").upper()
    gues.append(guesses)
    if guesses == ans[ques_num]:
        score += 1
        print("Its Correct!")
    else :
        print("INCORRECT Answer")
        print(f"{ans[ques_num]} is the correct answer")
    ques_num += 1

print("--------------RESULT-------------")

print("ans:",end="")
for answer in ans:
    print(answer,end="")
print()

print("gues:",end="")
for guesses in gues:
    print(guesses,end="")
print()


score = int( score / len(ques) * 100)
print(f"Your Score in :{score} %")