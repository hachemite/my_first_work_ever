#this is not a script. per so but a module.
#That is .this document defines several functions
#that we can then use on other object.thon
#The module will be called "ex25"(without the.py extension).
#In addition .we are going to run this from Python.
#and not the command line (exp:powershell) that we haveused so far.
#I've included instructions at the bottom.
def break_words(stuff):
    """This function will break up word for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off. """
    word = words.pop(0)
    print(word)

def print_last_word (words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)    
    print(word)

def sort_sentence(sentence):
    """Takes in full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the first and last words of sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sort the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#Here are the instuction :

#start python
#python

#2.Import this newly defined module.
#>>>import ex25 ; or this easiet way is to : (from ex25 import*) because we don't need to write every time when call the function ex25.function(var)
#Note : don'ttype ".py" or you'll get an error
#when you imporrt this it will create a new file file on your
#computer called 'ex25.pyc' which is python Bytecode
#ocument "which helps the module load faster in the future.
#You can however .delete it if you want to.

#3.create an object to work with
#>>> sentence ="All good things come to those who wait."


#4. Run "break_word" and show results
#>>>words = ex25.break_words(sentence)
#>>>words
#Note : you can also print without the intermediate variable
# >>> print ex25.break_word(sentence)


#5. Run "sort_word" and show results
#>>>sorted_words = ex25.sort_words(words)
#>>>sorted_words

#Run "print_first_word " (display automaticaly)"
#>>>ex25.print_first_word(words)

#Run "print_last_word " (display automaticaly)"
#>>>ex25.print_last_word(words)

#8. Run "sort_sentence " and show results
#sorted_sentence = ex25.sort_sentence(sentence)
#sorted_sentence
#Note : ZEd used the object "sorted_words" for these
#but that may be mistake because he used that earlier
#and all his variables so far use the function name . 
#so I'm calling the object "sorted_words" but used 
#a different process  to get there.


#Run "print_first_and last" (display automaticaly)
#>>>ex25.print_first_and_last(sentence)

#Run "print_first_and last_sorted" (display automaticaly)
#ex25.print_first_and_last_sorted(sentence)

#If you type help(ex25) you'll see the first block of
#text wrote at the top and the text in triple quotes
#for each function below

#If you type help(ex25.break) you'll see just 
#the triple quote text of that function .that 's called
#a "document comment"

#Finally you can avoid typing "ex25."at the beginning 
#of everythong if you import the module like instead:
#>>>from ex25 import *
#then you can run comman d like this:
# print(break_word(sentence))