import os
import os.path

# os.chdir('main') # change dir to main
dir_list = []
for cur_dir, dirs, files in os.walk('main'):
    if list(filter(lambda x: x.endswith('.py'), files)):
        dir_list.append(cur_dir)

dir_list.sort()
l = '\n'.join(dir_list)
print(l)
        