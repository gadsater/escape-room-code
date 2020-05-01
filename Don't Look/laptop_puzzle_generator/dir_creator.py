import os

dir_seq = ['Look Here!', 'Many Directory', 'Less Directory', 'Any Directory', 'All Directory', 'More Directory', 'Nothing Directory', 'Some Directory', 'Few Directory' ]

dir_list = [ 'Many', 'Less', 'Any', 'All', 'More', 'Nothing', 'Some', 'Few' ]

reply_msg = [ 
    'Do you want to go in?',
    'Do you want to go in?',
    'Do you still want to go in?',
    'Ok, sorry. You are in the wrong path.',
]

def dir_create(dir_list, path, depth, corr_path):
    path_seq = '/'.join(dir_seq[:(depth + 1)])
    path_seq = './' + path_seq + '/'

    if path_seq == path:
        corr_path = 0
    else:
        corr_path += 1

    if corr_path < 4:
        f = open(path + 'README', 'w+')
        f.write(reply_msg[corr_path])
        f.close()
    
    for i in range(len(dir_list)):
        elem = dir_list.pop(i)
        os.mkdir(path + elem + ' Directory')
        new_dir_list = dir_list.copy()
        dir_list.insert(i, elem)
        new_path = path + elem + ' Directory/'
        dir_create(new_dir_list, new_path, depth + 1, corr_path)


os.mkdir('./Look Here!/')
dir_create(dir_list, './Look Here!/', 0, 0)