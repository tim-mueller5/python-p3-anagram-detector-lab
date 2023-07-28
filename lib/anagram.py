# your code goes here!

class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, list):
        self.list = list
        word_letters = [letters for letters in self.word]
        end_list = []
        for item in list:
            letters = [letter for letter in item]
            if(sorted(letters) == sorted(word_letters)):
                end_list.append(item)
        return end_list

            

                


        # if (self.word in list):
        #     print(self.word)
        # else:
        #     return []