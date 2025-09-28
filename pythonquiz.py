
# quiz game

questions=("1.What are the mysterious creatures called that players fight in Weathering Waves?",
            "2.Who is the main playable protagonist at the start of Weathering Waves?",
            "3.In the story, what is the world recovering from?",
            "4.Which organization guides Rovers and Resonators in rebuilding the world?",
            "5.What is unique about the protagonist Rover?",)

options= (("A) Phantoms  ","B) Hollows   ","C) Wraiths ","D) Shadows"),
          ("A) Lingyang","B) Rover","C) Jianxin","D) Calcharo"),
          ("A) A war between nations","B) A cataclysmic disaster called the Lament","C) A broken energy core","D) A corruption by the Abyss"),
          ("A) Pioneer Corps","B) Hero Association","C) Phantom Hunters","D) The Dominion"),
          ("A) They cannot fight","B) They can absorb Echoes from enemies","C) They are half-Phantom","D) They are immortal")
            )

answers =("A","B","B","A","B")
guesses =[]
score = 0
quesitons_no= 0


for question in questions:
    print("-----------------------------------------")
    print(question)
    for option in options[quesitons_no]:
     print(option)
    

    guesse=input("Enter options (A,B,C,D):").upper()
    guesses.append(guesse)
    if guesse== answers[quesitons_no]:
       print("Correct!!!")
       score +=1
    else:
       print("Incorrect!!!")
       print(f"Correct anwers is {answers[quesitons_no]}")
    quesitons_no +=1   

print("------------------------------------------")
print("               RESULT                     ")

print("answer:", end="")
for anwer in answers:
   print(anwer,end=" ")
print()

print("guesses:", end="")
for guesse in guesses:
   print(guesse,end=" " )
print()

score=int (score/ len(questions)*100 )
print(f"your score is {score}%")





