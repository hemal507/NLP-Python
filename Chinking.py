import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')

# Here we are training the PunktSentenceTokenizer with sample text instead of
# using the default one. So we are passing train_text to PunktSentenceTokenizer
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            chunkGram = r""" Chunk: {<.*>+}
                              }<VB.?|IN|DT>+{  """
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

##            chunked.draw()
            print(chunked)
            
##            print(tagged)
              


    except Exception as e:
        print(str(e))


process_content()

