formatter = "{} {} {} {} "#that variable present by text but that not regular because is full by ({})  and that make this function command replace by anything number , text or variable
print(formatter.format(1,2,3,4))# now we 'll see this because we use the (formatter function) the place of ({}) is change by the number with same position of ({})  by using (format )
print(formatter.format("one","two","three","four"))# that the same thing but samall text
print(formatter.format(True,False,False,True))# yes that again but is function
print(formatter.format(formatter,formatter,formatter,formatter))# this is a variable is replace herself four time

print(formatter.format(
   "Try your",
   "Own text here",
   "Maybe a poem",
   "Or a song about fear",
)) # we don't care about the way of your wrinting but the the time your write that because you don't create 4 thing your syntaxe is error because we have 4of this ({})
