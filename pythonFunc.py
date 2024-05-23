def longer_string(s1: str, s2: str) -> str:
    """
    Повертає довшу з двох строк.
    """
    return s1 if len(s1) >= len(s2) else s2


def numeric_list(lst: list) -> bool:
    """
    Перевіряє чи всі елементи у списку є числами.
    """
    return all(isinstance(item, (int, float)) for item in lst)


def print_line() -> None:
    """
    Виводить строку з 80 зірочок.
    """
    print('*' * 80)

