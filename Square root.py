def square_root(num, err):
    guess = 1
    for x in range(num):
       next_guess=guess-((guess*guess)-num)/(2*guess)
 