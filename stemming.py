'''from nltk.stem import PorterStemmer
porter_stemmer = PorterStemmer()
print(porter_stemmer.stem('gets'))  #结果应该为：get'''

'''from nltk.stem import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
print(lancaster_stemmer.stem('gets'))  #结果应该为：get'''

'''from nltk.stem import SnowballStemmer
print(SnowballStemmer.languages)'''

from nltk.stem import SnowballStemmer
french_stemmer = SnowballStemmer('french')
print(french_stemmer.stem("Jour après jour, nuit après matin, reste avec moi dans l'instant. "
                          "Je te laisserais faire si je le savais. Pourquoi ne pas le dire ?"))
