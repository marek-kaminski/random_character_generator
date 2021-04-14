
import random
from random import choice


# this code gives us the number of lines in the .txt file
file = open("male_names.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()
# this code opens the txt file and gives us a random name from it
f = open("male_names.txt", 'r')
lines = f.readlines()
random_name = (lines[random.randint(1, line_count-1)])


for i in range(0, 1):

    print(random_name)
    str = 20 + 2 * random.randint(1, 10)
    dex = 20 + 2 * random.randint(1, 10)
    int = 20 + 2 * random.randint(1, 10)
    sw = 20 + 2 * random.randint(1, 10)
    ogd = 20 + 2 * random.randint(1, 10)
    print("siła = ", str,'\nzręczność = ', dex,'\ninteligencja = ', int,'\nsiła woli = ', sw,'\nogłada = ', ogd)
    print("****************************************")
# do zribienia:
# - tak żeby lista imion była zczytywana z pliku txt.
# - dokończyć wszystkie staty i zobaczyć czy działają na telefonie
# - zainstalować kivy żeby był jakiś frontend
# -



