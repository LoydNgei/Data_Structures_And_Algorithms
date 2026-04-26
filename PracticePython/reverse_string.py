def reverse_string(text):
    reversed_text = ""
    index = len(text) - 1

    while index >= 0:
        reversed_text += text[index]
        index -= 1
    return reversed_text


my_word = "hello"
result = reverse_string(my_word)
print(result)