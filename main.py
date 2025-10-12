from turtle import Turtle, Screen
import pandas
screen = Screen()
t = Turtle()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
correct = []
score = 0
game_on = True
while game_on:
    answer_state = screen.textinput(f"{score}/50", "Which state next?").title()
    data = pandas.read_csv("50_states.csv")
    list_states = data.state.to_list()
    #print(list_states)

    if answer_state == "Exit":
        missing_states = [state for state in list_states if state not in correct]
        # for state in list_states:
        #     if state not in correct:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_on = False
        break
    if answer_state in correct:
        print("Bu shtatni yozgan eding.")
    elif answer_state in list_states:
        print("you find it")
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        state_data = data[data.state == answer_state]
        turtle.goto(state_data.x.item(), state_data.y.item())
        turtle.write(state_data.state.item())
        correct.append(answer_state)
        score += 1
    else:
        print("Try again")
if score == 50:
    print("You win!")
    game_on = False





