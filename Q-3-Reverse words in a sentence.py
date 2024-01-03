def reverse_words(sentence):
    result = ""
    word = ""

    for i in sentence:
        if i == " ":
            if result == "":
                result = word
            else:
                result = result + word
            word = ""
        else:
            word += i

    if result == "":
        result = word
    else:
        result = word + " " + result

    return result

input_string = "hi aswin"
output = reverse_words(input_string)
print(output)

