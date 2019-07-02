# RA Shortcut Creator
# Made by lilbud
# Version 1.0

import os, sys

# REPLACE THESE LINES WITH PATHS TO YOUR FOLDERS

RAPATH = "D:\Emulation\Other Files\RetroArch"
CORES_DIR = os.path.join(RAPATH, "Cores")

corelist = os.listdir(CORES_DIR)

x = 0

for item in corelist[0:]:
    x = x + 1
    print("\n", x, '-', item)

coreselect = (int(input("\n Which core would you like to use?: ")))

choice = coreselect - 1

corechoice = (str(corelist[choice:coreselect]))

'''
test = isinstance(corechoice, str)
print(test)
'''

remove = corechoice.replace('[', '').replace(']', '').replace("'", '')

corepath = CORES_DIR + "\\" + remove

core = ('"{}"'.format(corepath))

file = open("result.bat","w+")
file.write(core)
file.close()






