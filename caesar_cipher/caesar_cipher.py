# import nltk
# from nltk.corpus import words
# from nltk.corpus import brown
# brown.words()
# from itertools import cycle, islice
import re

# nltk.download()

# original_words_list =words.words()
# words_list = [word.lower() for word in original_words_list]

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(sentence,shift_key):
  convert=[]
  c=[]    
  for char in sentence:
    w= re.sub("\d|\s|\W","_",sentence)
    if char in w :
        converted = shift_key + alphabet.index(char)
        new_converted = converted % 26
        c.append(str(alphabet[new_converted]))
        convert.append((str(alphabet[new_converted])))
        listToStr = ''.join([str(char) for char in w]) 
    elif not char in w:
        if char!=alphabet:
            char= " "
            c.append(char)
            e= re.sub("_"," ",listToStr)  
  prRed(e) 
  prYellow("".join(c))
  print ("".join(c))
  return ("".join(c))
  

def decrypt(sentence,shift_key):
  convert=[]
  c=[]    
  for char in sentence:
    w= re.sub("\d|\s|\W","_",sentence)
    if char in w :
        converted = shift_key + alphabet.index(char)
        new_converted = converted % 26
        c.append(str(alphabet[new_converted]))
        convert.append((str(alphabet[new_converted])))
        listToStr = ''.join([str(char) for char in w]) 
    elif not char in w:
        if char!=alphabet:
            char= " "
            c.append(char)
            e= re.sub("_"," ",listToStr)  
  prRed(e) 
  prYellow("".join(c))
  print ("".join(c))
  return ("".join(c))


# import nltk
# nltk.download('words')

# original_words_list = nltk.corpus.words.words()
# # print(words_list[30000:30100])
# words_list = [word.lower() for word in original_words_list]

# # For any given sentence, how many english words are there?
# def count_words(sentence):
#     sentence_words = sentence.split()
#     en_word_count = 0

#     for word in sentence_words:
#         if word.lower() in words_list:
#             en_word_count += 1

#     return en_word_count

# def most_likely(sentences):
#     _max = 0
#     _max_sentence = ''

#     for sentence in sentences:
#         if count_words(sentence) > _max:
#             _max_sentence = sentence
#             _max = count_words(sentence)
#     return _max_sentence


if __name__ == "__main__":
    
    encrypt("cat is animal ! hsdfo # rr5",500)
    prGreen("*"*50)
    encrypt("cat is animal ! hsdfo # rr5",3)
    prGreen("*"*50)
    decrypt("dbu jt bojnbm ! itegp # ss5",-1)
    prGreen("*"*50)
    decrypt("fdw lv dqlpdo   kvgir   uu",-3)
    prGreen("*"*50)
    decrypt("jha pz hupths   ozkmv   yy",-7)
    prGreen("*"*50)
    decrypt("dbu jt bojnbm   itegp   ss",-27)

    # sentence = 'John Is Hungry'
    # print(count_words(sentence))
    # sentences = [
    #     'asd ka hyhrtw',
    #     'kds iu okyhgf',
    #     'iwn is okhsti',
    #     'dog is hungry',
    #     'ahmad is fghjk',
    #     'ths ik okstgr',
    #     'jug sd plwrdw',
    #     'cat jh hujgru'
    # ]
    # print(most_likely(sentences))