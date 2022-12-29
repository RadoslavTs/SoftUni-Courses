import random
questions = ["Кой е черната мамба?", "Кога черната мамба апе?", "Ше ям ли бой?"]
guess_counter = 0
answered_questions = []
for sequence in range(10):
    current_question = random.choice(questions)
    if current_question not in answered_questions:
        answered_questions.append(current_question)
        print(current_question)
    else:
        continue
    if current_question == "Кой е черната мамба?":
        answer = input("Въведете отговор: ")
        if answer == "Тали":
            print("Ти позна въпроса\n")
            guess_counter += 1
        else:
            print("Грешен отговор\n")
    if current_question == "Кога черната мамба апе?":
        answer = input("Въведете отговор: ")
        if answer == "вечер":
            print("Ти позна въпроса\n")
            guess_counter += 1
        else:
            print("Грешен отговор\n")
    if current_question == "Ше ям ли бой?":
        answer = input("Въведете отговор: ")
        if answer == "да":
            print("Ти позна въпроса\n")
            guess_counter += 1
        else:
            print("Грешен отговор\n")
    if guess_counter == 2:
        print("Ти спечели играта")
        break

