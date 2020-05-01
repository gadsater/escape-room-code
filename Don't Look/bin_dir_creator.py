import os

dir_names = [ 'one', 'two' ]
max_depth = 3

def bin_depth_creator(dir_name, path, depth, max_depth):
    if depth == max_depth:
        return

    for elem in dir_name:
        os.mkdir(path + elem)
        bin_depth_creator(dir_name, path + elem + '/', depth + 1, max_depth)

bin_depth_creator(dir_names, './', 0, max_depth)
