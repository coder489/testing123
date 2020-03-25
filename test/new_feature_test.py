from app.new_feature import announce

def test_announce():
    result = announce()
    assert result == "Hello World"