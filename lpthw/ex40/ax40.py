class Song(object):
    def __init__(self,lyrics):
        self.lyrics= lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
z = ['منبت الأحرار','مشرق الأنوار','منتدى السؤدد وحماه','دمت منتداه','وحماه','عشت في الأوطان','للعلى عنوان','ملء كل جنان','ذكرى كل لسان','بالروح','بالجسد','هب فتاك','لبي نداك','في فمي وفي دمي','هواك ثار نور ونار','اخوتي هيا','للعلى سعيا','نشهد الدنيا','أنا هنا نحيا','بشعار','الله','الوطن الملك']       
happy_bday = Song(z)

bulls_on_parade = Song(["They rally around the family",
                       "With pockets full of shells"])
                       

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


