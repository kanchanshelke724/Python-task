def count_word_frequency(paragraph):
    words = paragraph.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(f"{word}: {count}")


user = input("Enter a paragraph: ")
count_word_frequency(user)
