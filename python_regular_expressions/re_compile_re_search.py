import re
print('\d — это всего лишь ОДНО число, поэтому он находит только «2» в «2014»')
text = "Hello! My name is Sinan. It is 2014 and it's amazing."
pattern1 = re.compile("\d")
re.search(pattern1, text)  # \d — это всего лишь ОДНО число, поэтому он находит только «2» в «2014»
print('Ответ: ', re.search(pattern1, text).group(0))


# добавление + означает «по крайней мере один», но потенциально больше
print('добавление + означает «по крайней мере один», но потенциально больше')
pattern2 = re.compile("\d+")
print('Ответ: ',re.search(pattern2, text).group(0)) # == '2014'

# используйте квадратные скобки [] для соответствия одному из присутствующих элементов
print('используйте квадратные скобки [] для соответствия одному из присутствующих элементов')
text2 = 'abcdefg'
pattern3 = re.compile('[cfg]')
print('Ответ: ',re.search(pattern3, text2).group(0))

print('Выводит номера с тире между ними')
mystery_pattern = re.compile("\d+-\d+-\d+")
# потратьте несколько минут и обсудите, какое применение может иметь этот таинственный_шаблон
print('Ответ: ',re.search(mystery_pattern, "my phone number is 609-462-6706 dude").group(0))


# . соответствует ВСЕМ
print('Точка -  соответствует ВСЕМ буквам и символам')
all_of_the_text = "dmzhvbek.-uhvbc   \  dfljghwco87rc6geinsr6t4gi7rgwefiuvbekuhvbdfljghwco87rc6geinsr6t4gi7rgwefiu ywgsfybcstzvgbrtybte"
anything_pattern = re.compile(".+")
print('Ответ: ',re.search(anything_pattern, all_of_the_text).group(0))

# \w соответствует любому буквенно-цифровому символу слова
# если вы хотите сопоставить фактический период, выполните \.
print('соответствует любому буквенно-цифровому символу слова')
email_pattern = re.compile("[\w\.]+@\w+\.com")
print('Ответ: ',re.search(email_pattern, "my email address is sinan.u.ozdemir@gmail.com").group(0))
