from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    for i in range(n):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke = f'{noun} {adverb} {adjective}'
        print(joke)


get_jokes(n=1)