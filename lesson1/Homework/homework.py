def function(word):
    common_word = word
    upside_down_word = common_word[::-1]

    if common_word == upside_down_word:
        print(True)
    else:
        print(False)

function('hello')