from nltk.tokenize import word_tokenize
mytext = "Del día a la noche a la mañana, mantente conmigo en el momento. " \
         "Te dejaría si lo supiera. ¿Por qué no lo dices?"
print(word_tokenize(mytext, language='spanish'))  # 设定语言为西班牙语
