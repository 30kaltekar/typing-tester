from getch import getch
import time
import random
import os
from colorama import Fore, Style, Back

points = 0

level3 = ["Though the person did not move, indeed he was real"]

def split(x):
    return [char for char in x]


def get_list(x, count, status):
    try:

        value = ''

        for i in x:
            if status == "W":
                i = Style.BRIGHT + Fore.RED + i + Style.RESET_ALL
            else:
                i = Style.BRIGHT + Fore.WHITE + i + Style.RESET_ALL  # this sets the color of the text you need to type

        v = x[count]
        x[count] = Style.BRIGHT + Fore.BLACK + Back.GREEN + v + Style.RESET_ALL  # this sets the color of the current letter that is needed

        for i in x:
            value += i
        return value

    except:
        return ("Your done! 👍")


playing = True

while playing == True:
    print(Fore.GREEN + "Get Ready to type!" + Style.RESET_ALL)

    time.sleep(1)
    start = time.time()

    sentence = random.choice(level3)

    win = False
    out = ''

    os.system('clear')
    count = 0

    while win != True:
        ls = split(sentence)
        length = len(ls)

        os.system('clear')
        copy = ls
        status = "C"

        out_s = get_list(split(sentence), count, status)
        print(Fore.CYAN + Style.BRIGHT + 'Type this sentence: ' + Fore.WHITE +
              Back.BLACK + out_s)

        print(Style.RESET_ALL + Fore.CYAN + "                >>> " +
              Style.RESET_ALL + Fore.GREEN + out)
        key = False

        while key != True:
            try:
                key_needed = ls[count]
                print(key_needed)

                try:
                    get_key = getch()

                    if get_key == key_needed:
                        status = "C"
                        out += get_key

                        count += 1
                        key = True
                    else:
                        print(Fore.RED + 'Wrong key! You pressed ' + get_key)
                        status = "W"
                except:
                    print("Error! Try again")
            except:
                if length == count:
                    win = True
                    playing = False
                    key = True

                    # here is how the score is calculated
                    end = time.time()
                    time_taken = end - start
                else:
                    print("Error!")
                    
wpm = len(out)*60/(5*time_taken)
points += wpm * 2
print("Time: " + str(int(time_taken)))
print(round(wpm), end="")
print(" WPM")
