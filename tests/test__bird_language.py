from src.bird_language import translate


def test__translate__signature():
    result = translate("hieeelalaooo")

    assert isinstance(result, str)


def test__translate__examples():
    assert translate("hieeelalaooo") == "hello", "Hi!"

    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"

    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"

    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
