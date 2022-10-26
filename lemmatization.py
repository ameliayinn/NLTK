'''from nltk.stem import PorterStemmer
porter_stemmer = PorterStemmer()
print(porter_stemmer.stem('increases'))  #返回结果为incres
'''

'''from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('increases'))  # 结果为：increase
'''

'''from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('getting', pos="v"))'''


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('alleged', pos="v"))  # 返回动词
print(lemmatizer.lemmatize('friends', pos="n"))  # 返回名词
print(lemmatizer.lemmatize('previous', pos="a"))  # 返回形容词
print(lemmatizer.lemmatize('carelessly', pos="r"))  # 返回副词


