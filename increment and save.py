# This Pythonista script increments and saves the current file.  
# I wrote it so I could quickly save different versions of scripts.
# It is meant to be added to the editor's action menu. 

import editor
import re

text = editor.get_text()
filepath = editor.get_path()

#sloppy regex
filepath_a = re.split("/",filepath)
filename = filepath_a[len(filepath_a)-1]

#remove extension
filename = filename[:-3]

#finds number at end
num = re.split('[^\d]', filename)[-1]

#get length of number string 
l=len(num)

#check if number string is empty
#if file ends with a number, increment it
if l >=1:
	num2 = int(num) + 1
	#remove number from filename and add
	#the new incremented number
	filename = filename[:-l] + str(num2)

#write new file
editor.make_new_file(filename, text)


