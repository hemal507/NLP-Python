from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def stem1(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment','er','ic']:
        if word.endswith(suffix):
            print suffix
            return word[:-len(suffix)]
    return word



##ps = PorterStemmer()

example_words = ['Python','pythoner','puthoning','pythoned','pythonly','pythonic']
##example_word2 = ['Work','worker','working','worked','workly']

##for w in example_words:
##    print (ps.stem(w))

for w in example_words:
    print (stem1(w))
    

##for w in example_word2:
##    print (ps.stem(w))

new_text = 'It is very important to be pythonly while you are working with python. All pythoners have pythoned poorly atleast once.'

words = word_tokenize(new_text)
for w in words:
##    print (ps.stem(w))
      print (stem1(w))


    
