import random as rn
import os


t_abilities = ('Strength', 'Intelligence', 'Wisdom', \
    'Dexterity', 'Constitution', 'Charisma')
d = 'y'
while d !='n':
    os.system('clear')
    for trait in t_abilities:
        i_ra3 = 0
        for i in range(1,4):
            i_ra = rn.randrange(1,7)
            i_ra3 += i_ra
            print('Roll #{} is {}.\tTotal: {}'.format(i,i_ra,i_ra3))
        print('\t\t\t{}: {}\n'.format(trait,i_ra3))
    d = str(input('Roll again? (y/n): '))