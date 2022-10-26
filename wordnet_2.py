'''from nltk.corpus import wordnet
syn = wordnet.synsets("fast", pos='a')  #获取"fast"的同义词集
print(syn[0].definition())  # 定义
print(syn[0].examples())  # 例句'''

'''from nltk.corpus import wordnet
synonyms = []
for syn in wordnet.synsets('fancy', pos='v'):  # 同义词
    for lemma in syn.lemmas():  # 词元
        synonyms.append(lemma.name())
print(synonyms)'''


'''from nltk.corpus import wordnet
antonyms = []
for syn in wordnet.synsets("slow"):  # 同义词
    for lemma in syn.lemmas():
        if lemma.antonyms() and lemma.antonyms()[0].name() not in antonyms:   # 如果其同义词有反义词且不在antonyms里面
            antonyms.append(lemma.antonyms()[0].name())  # 将这个同义词的反义词放入antonyms
print(antonyms)'''

'''from nltk.corpus import wordnet
antonyms = []
for syn in wordnet.synsets("fast"):  # 同义词
    lemma = syn.lemmas()[0]
    for _ in range(len(lemma.antonyms())):
        if lemma.antonyms() and lemma.antonyms()[_].name() not in antonyms:  # 如果有反义词且不在antonyms里面
            antonyms.append(lemma.antonyms()[_].name())  # 将反义词放入antonyms
print(antonyms)'''

from nltk.corpus import wordnet
antonyms = []
for syn in wordnet.synsets("slow"):  # 同义词
    for lemma in syn.lemmas():
        # print(lemma.name())
        for _ in range(len(lemma.antonyms())):
            # if lemma.antonyms(): print('1')
            if lemma.antonyms() and lemma.antonyms()[_].name() not in antonyms:  # 如果有反义词且不在antonyms里面
                antonyms.append(lemma.antonyms()[_].name())  # 将反义词放入antonyms
print(antonyms)
