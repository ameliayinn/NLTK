from nltk.corpus import stopwords

tokens = ['day', 'to', 'night', 'to', 'morning', 'keep', 'with',
          'me', 'in', 'the', 'moment', 'I\'d', 'let', 'you', 'had',
          'I', 'known', 'it', 'why', 'don\'t', 'you', 'say', 'so']

clean_tokens = tokens[:]
stwords = stopwords.words('english')
# print(stwords) # 打印英文停用词表
for token in tokens:
    if token in stwords:
        clean_tokens.remove(token)

print(clean_tokens)