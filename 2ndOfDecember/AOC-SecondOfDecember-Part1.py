OPPONENTS_ROCK = "A"
OPPONENTS_PAPER = "B"
OPPONENTS_SCISSOR = "C"

MY_ROCK = "X"
MY_PAPER = "Y"
MY_SCISSOR = "Z"

SCISSOR_CONT = 3
PAPER_CONT = 2
ROCK_CONT = 1

LOSS_CONT = 0
WIN_CONT = 6
DRAW_CONT = 3

my_total_score = 0
opponents_total_score = 0

number_of_lines = 0
with open("/Users/nurdanemin/Desktop/adventofcode-input-day2.txt") as file:
    line = file.readline()
    while line:

        line = line.strip().split(" ")
        opponents_choice = line[0]
        my_choice = line[1]

        if opponents_choice == OPPONENTS_ROCK:
            opponents_total_score += ROCK_CONT
            if my_choice == MY_ROCK:
                my_total_score += (ROCK_CONT + DRAW_CONT)
                opponents_total_score += DRAW_CONT
            elif my_choice == MY_PAPER:
                my_total_score += (PAPER_CONT + WIN_CONT)
                opponents_total_score += LOSS_CONT
            else:
                my_total_score += (SCISSOR_CONT + LOSS_CONT)
                opponents_total_score += WIN_CONT

        elif opponents_choice == OPPONENTS_PAPER:
            opponents_total_score += PAPER_CONT
            if my_choice == MY_ROCK:
                my_total_score += (ROCK_CONT + LOSS_CONT)
                opponents_total_score += WIN_CONT

            elif my_choice == MY_PAPER:
                my_total_score += (PAPER_CONT + DRAW_CONT)
                opponents_total_score += DRAW_CONT

            else:
                my_total_score += (SCISSOR_CONT + WIN_CONT)
                opponents_total_score += LOSS_CONT

        elif opponents_choice == OPPONENTS_SCISSOR:
            opponents_total_score += SCISSOR_CONT
            if my_choice == MY_ROCK:
                my_total_score += (ROCK_CONT + WIN_CONT)
                opponents_total_score += LOSS_CONT
            elif my_choice == MY_PAPER:
                my_total_score += (PAPER_CONT + LOSS_CONT)
                opponents_total_score += WIN_CONT
            elif my_choice == MY_SCISSOR:
                opponents_total_score += DRAW_CONT
                my_total_score += (SCISSOR_CONT + DRAW_CONT)
        line = file.readline()

print("my score is :" + str(my_total_score) + " Opponents score is: " + str(opponents_total_score))
