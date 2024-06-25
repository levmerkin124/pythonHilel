from removeSpaces import remove_spaces

def test_remove_space_only_space():
    assert remove_spaces(" ") == ""

def test_remove_space_with_space():
    assert remove_spaces("Hello World") == "HelloWorld"

def test_remove_space_without_space():
    assert remove_spaces("HelloWorld") == "HelloWorld"

