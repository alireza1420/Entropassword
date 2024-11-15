import math
import random

def choose_line(file_name):
    """Choose a line at random from the text file"""
    with open(file_name, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
    return random_line

pass_string="";
Input_num=int(input("Enter the number of inputs: "))

for i in range(int(Input_num)):
    pass_string=pass_string+choose_line("wordlist.txt")
if(len(pass_string)<Input_num):
    pass_string=pass_string+choose_line("wordlist.txt")
# 3 symb 52 upper lower, 10 Numbers = 65 Pool
# possible_String= pow(65)
possible_Combinations=pow(65,len(pass_string));
entropy=math.log(pow(65,len(pass_string)))




print("Password:",pass_string)
print("Length of password:",len(pass_string))
print("Possible Combinatiosn:",possible_Combinations)
print("Entropy:",entropy)
