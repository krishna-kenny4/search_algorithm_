def search_algorithm(text, word):
    text_letter_counter = 0
    word_letter_counter = 0

    text = " "+text
    stage_list = []
    remember_index = []

    while text_letter_counter < len(text):

        if text[text_letter_counter] == word[word_letter_counter]:
            char_lst = []
            remember_index.append(text_letter_counter)

            for z in range(len(word)):
                char_lst.append(text[text_letter_counter])
                text_letter_counter += 1

            stage_list.append(char_lst)
            text_letter_counter = text_letter_counter - (len(word) - 1)

        else:
            text_letter_counter += 1

    index = 0
    position_list = []
    for string_ in stage_list:
        if string_ == list(word):
            position_list.append(remember_index[index]-1)
        index += 1

    return position_list


text = input("Enter text: ")
word = input("Enter word: ")
print(search_algorithm(text, word))
