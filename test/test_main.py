import pytest
from main.main import generate_password


def test_generate_password_length():
    # Тестирование генерации пароля с различными длинами
    for length in range(1, 11):
        password = generate_password(length)
        assert len(password) == length


def test_generate_password_characters():
    # Тестирование генерации пароля с различными типами символов
    for _ in range(10):
        password = generate_password(length=8, use_digits=True, use_letters=True, use_symbols=True)
        assert any(char.isdigit() for char in password)
        assert any(char.isalpha() for char in password)
        assert any(not char.isalnum() for char in password)


def test_generate_password_exceptions():
    # Тестирование вызова исключения при отсутствии выбранных типов символов
    with pytest.raises(ValueError):
        generate_password(length=8, use_digits=False, use_letters=False, use_symbols=False)
