import codecs
from curses.ascii import isupper
import random

first_words = set()
ordered_words = []
words_pairs = {}

with codecs.open("speech.txt", mode="r", encoding='utf-8') as f:
    words = f.read().split(" ")
    for w in words:
        ordered_words.append(w)

    i=0
    for sample in ordered_words:
        if len(sample.strip()) > 0 and len(ordered_words[i-1].strip()) > 0:
            #finding first words
            if i > 0 :
                if sample.strip()[0].isupper() and ordered_words[i-1].strip()[-1] in (".",",","!","?",";",":"):
                    first_words.add(sample.strip())
            else:
                first_words.add(sample.strip())
            #putting words and their pairs in a dictionary
            if sample.strip() not in words_pairs.keys():
                words_pairs[sample.strip()] = {}
            if i>0:
                previous_word = ordered_words[i-1].strip()
                if previous_word in words_pairs.keys():
                    if sample.strip() not in words_pairs[previous_word].keys():
                        words_pairs[previous_word][sample.strip()] = 1
                    else:
                        words_pairs[previous_word][sample.strip()] +=1
            i+=1

def get_sentence():
    result = []
    first_word = random.choice(list(first_words)) #get a random first word
    result.append(first_word)
    
    while "." not in result[-1]:
        last_word = result[-1]
        chances = []
        for key in words_pairs[last_word].keys():
            chances.append(words_pairs[last_word][key])
        next_word = random.choices( list(words_pairs[last_word]) , weights = chances, k=1) #get a random next word according to the chances
        result.append(next_word[0])
    return " ".join(result)
        

#generate 50 sentences
with open("output.txt", "w") as f:
    result = ""
    for i in range(50):
        result += get_sentence() + "\n"
    f.write(result)