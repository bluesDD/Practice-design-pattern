def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

if __name__ == "__main__":
    address = "four score and sevne ye ago..."
    result = index_words(address)
    print(result[:10])

    it = list(index_words_iter(address))
    print(it[:10])


