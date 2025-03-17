#study drill 2 co,fusing me for this reason I will use all the way possible
print('1*__________________________________________________')
class Song(object):
    def __init__(self,lyrics):
        self.lyrics= lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
music = ["Happy bithay to you",
        "I don't want to get sued",
        "So I'll stop right there"
                  ]        
happy_bday = Song(music)


happy_bday.sing_me_a_song()


print('\n\n\n2*__________________________________________________')
class Song(object):
    def __init__(self):
        self.lyrics= ["Happy bithay to you",
                      "I don't want to get sued",
                      "So I'll stop right there"] 
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
  
happy_bday = Song()

happy_bday.sing_me_a_song()

print('\n\n\n3*__________________________________________________')

class Song(object):
    def __init__(self,lyrics):
        self.lyrics= lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        
happy_bday = Song(["Happy bithay to you",
                  "I don't want to get sued",
                  "So I'll stop right there"
                  ])

sad_bday = Song(happy_bday.lyrics)
sad_bday.sing_me_a_song()

        