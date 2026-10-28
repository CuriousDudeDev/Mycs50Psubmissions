def main():
    word = input('Enter the word: ')
    print(shorten(word))


def shorten(word):
    new = ''
    for i in word:
        new += '' if i in ['a' , 'e' , 'i' , 'o' , 'u'] else i
    return (new)


if __name__ == "__main__":
    main()
