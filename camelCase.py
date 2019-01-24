def camel(string):
    words = string.split("-")
    news = f'{words[0]}'
    i = 0
    for word in words:
        if i > 0:
            word = word[0].replace(word[0], word[0].upper()) + word[1::]
            news += word
        else:
            i += 1
    print(news)
camel("this-is-a-really-cool-challenge-and-i-really-think-camel-casing-is-cool-")
