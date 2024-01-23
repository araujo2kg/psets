from twttr import shorten

def main():
    test_shorten_default()

def test_shorten_default():
        assert shorten("Twitter") == "Twttr"
        assert shorten("What's your name?") == "Wht's yr nm?"
        assert shorten("CS50") == "CS50"

def test_shorten_upper():
     assert shorten("UPPERCASE") == "PPRCS"

def test_shorten_lower():
     assert shorten("lowercase") == "lwrcs"

def test_shorten_novowels():
     assert shorten("trn dwn th lghts") == "trn dwn th lghts"

if __name__ == "__main__":
    main()
