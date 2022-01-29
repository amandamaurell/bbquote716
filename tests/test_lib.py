from bbquote716.lib import get_quote

def test_getquote():
    assert len(get_quote()) != 0
    