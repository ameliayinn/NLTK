'''import nltk
text=nltk.word_tokenize('why don\'t you say so?')
print(text)
print(nltk.pos_tag(text))'''

import nltk
text1=nltk.word_tokenize('cut with a saw')
text2=nltk.word_tokenize('I saw him yesterday.')
print(nltk.pos_tag(text1))
print(nltk.pos_tag(text2))


