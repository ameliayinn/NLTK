import nltk

tokens = ['day', 'to', 'night', 'to', 'morning', 'keep', 'with',
          'me', 'in', 'the', 'moment', 'I\'d', 'let', 'you', 'had',
          'I', 'known', 'it', 'why', 'don\'t', 'you', 'say', 'so']
# 统计词频
freq = nltk.FreqDist(tokens)

# 输出词和相应的频率
for key, val in freq.items():
    print(str(key) + ':' + str(val))

# 可以把最常用的5个单词拿出来
standard_freq = freq.most_common(5)
print(standard_freq)

'''# 绘图函数为这些词频绘制一个图形
freq.plot(20, cumulative=False)'''