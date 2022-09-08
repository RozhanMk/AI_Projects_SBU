import sys
import re

train_data = sys.argv[1]
test_data = sys.argv[2]
output = sys.argv[3]

n_spams = 0
n_hams = 0
all_words = set()

spam_words = 0
alpha = 1
repeat_word_in_spam = {}    # {word: count}

ham_words = 0
repeat_word_in_ham = {}    # {word: count}

spam_word_possibility = {} # {word: possibility}
ham_word_possibility = {} # {word: possibility}

predicts = []
 
#training
with open(train_data, 'r') as f:
    words = f.read().split()
    for w in words:
        word = w.strip()
        if word == 'spam':
            n_spams += 1
        elif word == 'ham':
            n_hams += 1
        else:
            all_words.add(word)
            if word not in repeat_word_in_spam.keys():
                repeat_word_in_spam[word] = 0
            
            if word not in repeat_word_in_ham.keys():
                repeat_word_in_ham[word] = 0
            
            
with open(train_data, 'r') as f:
    lines = f.readlines()
    for line in lines:
        tag = line.split("\t")[0]
        mail = line.split("\t")[1]
        if tag == "spam":
            words = mail.split(" ")
            spam_words += len(words)
            for w in words:
                word = w.strip()
                if word in repeat_word_in_spam.keys():
                    repeat_word_in_spam[word] += 1
                else:
                    repeat_word_in_spam[word] = 1

        if tag == "ham":
            words = mail.split(" ")
            ham_words += len(words)
            for w in words:
                word = w.strip()
                if word in repeat_word_in_ham.keys():
                    repeat_word_in_ham[word] += 1
                else:
                    repeat_word_in_ham[word] = 1

for word in repeat_word_in_spam.keys():
    possibility = float(repeat_word_in_spam[word] + alpha) / float((alpha * len(all_words)) + spam_words)
    spam_word_possibility[word] = possibility

for word in repeat_word_in_ham.keys():
    possibility = float(repeat_word_in_ham[word] + alpha) / float((alpha * len(all_words)) + ham_words)
    ham_word_possibility[word] = possibility

#Working on test data
with open(test_data, 'r') as f:
    lines = f.readlines()
    
    for line in lines:
        formula_spam = float(n_spams/(n_spams+n_hams))  
        formula_ham = float(n_hams/(n_spams+n_hams))
        for w in line.split(" "):
            word = w.strip()
            if word in spam_word_possibility.keys():
                formula_spam *= spam_word_possibility.get(word , 1)
            if word in ham_word_possibility.keys():
                formula_ham *= ham_word_possibility.get(word , 1)
        if formula_spam > formula_ham:
            predicts.append("spam")
        else:
            predicts.append("ham")
    
    with open(output, 'w') as f:
        i=0
        result = ""
        for p in predicts:
            result += p + "\t" + lines[i]
            i+=1
        f.write(result)



