OPPONENTS_ROCK = "A"
OPPONENTS_PAPER = "B"
OPPONENTS_SCISSOR = "C"

MY_LOSS = "X"
MY_DRAW = "Y"
MY_WIN = "Z"

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
        my_status = line[1]

        if opponents_choice == OPPONENTS_ROCK:
            opponents_total_score += ROCK_CONT
            if my_status == MY_LOSS:
                my_total_score += SCISSOR_CONT + LOSS_CONT
                opponents_total_score += WIN_CONT
            elif my_status == MY_DRAW:
                my_total_score += DRAW_CONT + ROCK_CONT
                opponents_total_score += DRAW_CONT
            else:
                my_total_score += PAPER_CONT + WIN_CONT
                opponents_total_score += LOSS_CONT

        elif opponents_choice == OPPONENTS_PAPER:
            opponents_total_score += PAPER_CONT
            if my_status == MY_LOSS:
                my_total_score += (ROCK_CONT + LOSS_CONT)
                opponents_total_score += WIN_CONT

            elif my_status == MY_DRAW:
                my_total_score += (PAPER_CONT + DRAW_CONT)
                opponents_total_score += DRAW_CONT

            else:
                my_total_score += (SCISSOR_CONT + WIN_CONT)
                opponents_total_score += LOSS_CONT

        elif opponents_choice == OPPONENTS_SCISSOR:
            opponents_total_score += SCISSOR_CONT
            if my_status == MY_LOSS:
                my_total_score += (PAPER_CONT + LOSS_CONT)
                opponents_total_score += WIN_CONT
            elif my_status == MY_DRAW:
                my_total_score += (SCISSOR_CONT + DRAW_CONT)
                opponents_total_score += WIN_CONT
            else:
                opponents_total_score += LOSS_CONT
                my_total_score += (ROCK_CONT + WIN_CONT)
        line = file.readline()

print("my score is :" + str(my_total_score) + " Opponents score is: " + str(opponents_total_score))
