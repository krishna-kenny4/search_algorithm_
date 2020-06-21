def search_algorithm(text, word):
    text_letter_counter = 0
    word_letter_counter = 0

    text = " "+text
    stage_list = []

    while text_letter_counter < len(text):

        if text[text_letter_counter] == word[0]:
            char_lst = []

            for z in range(len(word)):
                char_lst.append(text[text_letter_counter])
                text_letter_counter += 1
                
            stage_list.append(char_lst)
            text_letter_counter = text_letter_counter - (len(word) - 1)

        else:
            text_letter_counter += 1

    return stage_list


print(search_algorithm("i am awesome", "awesome"))
