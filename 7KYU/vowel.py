def get_count(sentence):
    nvow = 0
    for vow in ["a", "e", "i", "o", "u"]:
        nvow += sentence.count(vow)
    return nvow