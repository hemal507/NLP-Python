from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better",pos="a"))  # adjective 
print(lemmatizer.lemmatize("best",pos="a"))     # default pos = n , noun
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("ran","v"))


