from shutil import copyfile

dir_dict = {
    0: 'Oh! So you have come here... Where do you look, there are MANY directories around...',
    1: 'So, you have eliminated a directory, huh! That makes it one less directory than before. I am just reminding where you are.',
    2: 'All directories possibly lead to the answer that you are looking for, but only any one can be choosen at a time.',
    3: 'Now, there is a chance that all directories might contain the answer.',
    4: 'You may believe that you have found the answer but there are more directories to look at. Do not get distracted!',
    5: 'A wise teacher once said "Something is better than nothing but you can be content with nothing".',
    6: 'Well, there are only a few directories left. Even random exploration will lead you to the answer.',
    7: 'There is only one left, what are you waiting for?! Go ahead!',
    8: 'Haha! You thought I had an answer! Well, yes and no. I can guide you to the answer. Trust me! Well, you have already seen it. All you need to do is go back to where it all started.\nSolve the sudoku. May the dice guide you.',
}

dir_seq = ['Look Here!', 'Many Directory', 'Less Directory', 'Any Directory', 'All Directory', 'More Directory', 'Nothing Directory', 'Some Directory', 'Few Directory' ]

file_pos = { 4: 'pig_pen.jpg', 5: 'morse_code.jpg', 7: 'braille.jpg' }

path = './'
for i in range(len(dir_seq)):
    dir = dir_seq[i]

    path += dir + '/'
    f = open(path + 'README', 'w+')
    f.write(dir_dict[i])
    f.close()

    if i in file_pos.keys():
        copyfile(file_pos[i], path + file_pos[i])
