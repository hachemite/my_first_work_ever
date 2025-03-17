from sys import argv # in this we see the module or features of (sys) with (argv) who make me print variable when I open fil.py

script, filename = argv # in this place we write (script) for pc get rid in order not confused with name of file (ex15.py) and take care of the next file name we should to be (.txt) 

txt = open(filename) # in the stage we get the variable  identifaction is an order to open file (txt) without anything

print(f"Here's your file {filename}:") # in this he just write a text with name of file(txt) we get it before for just me to be sure it is the right file
print(txt.read())#1<< in the first the pc print the open file is just get you some weird and secret word and code composer , I think the file without decode
                 #2<< with (read) function the pc finnally decoding the file and give you the real composer and get you the text wwho write
print("Type the filename again :")# it just a text to export 
file_again =input(">")# in the input give the user the chance for write the name of file(txt) we should keep attentionbecause the file should finish by .txt

txt_again = open(file_again) # in the stage we get the variable  identifaction is an order to open file (txt) without anything

print(txt_again.read()) # in this case the the variable his open and he decode for read like the real file