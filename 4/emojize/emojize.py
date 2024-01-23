import emoji


def emoji_conversion():
    inp = emoji.emojize(input("Input: "), language="alias")
    print("Output:", inp)


emoji_conversion()
