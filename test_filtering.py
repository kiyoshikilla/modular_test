import pytest
import os
from filtering import filter_lines

@pytest.fixture
def sample_text():
    """
    Фікстура для створення тестового вхідного файлу з текстом.
    Після завершення тесту файл автоматично видаляється.
    """
    content = """The river flows gently through the valley.
Birds chirp melodiously in the early morning.
He enjoys walking in the park every evening.
A warm cup of tea soothes the mind.
The dog enjoys walking by the lake.
She painted a beautiful landscape on the canvas.
The city lights sparkle like stars at night.
A peaceful walking trail winds through the forest.
"""
    input_filename = "test_input.txt"
    with open(input_filename, "w", encoding="utf-8") as f:
        f.write(content)
    yield input_filename  # Передаємо ім'я файлу для тестів
    os.remove(input_filename)  # Видаляємо після тестів

@pytest.mark.parametrize("keyword, expected_lines", [
    ("walking", [
        "He enjoys walking in the park every evening.\n",
        "The dog enjoys walking by the lake.\n",
        "A peaceful walking trail winds through the forest.\n"
    ]),
    ("tea", [
        "A warm cup of tea soothes the mind.\n"
    ]),
    ("city", [
        "The city lights sparkle like stars at night.\n"
    ]),
    ("river", [
        "The river flows gently through the valley.\n"
    ]),
    ("notfound", [])  # Перевірка, коли збігів немає
])
def test_filter_lines(sample_text, keyword, expected_lines):
    """
    Тестуємо функцію filter_lines з різними ключовими словами
    """
    output_filename = "test_output.txt"
    
    # Виконуємо фільтрацію
    assert filter_lines(sample_text, output_filename, keyword) is True

    # Перевіряємо вміст вихідного файлу
    with open(output_filename, "r", encoding="utf-8") as f:
        result_lines = f.readlines()
    
    assert result_lines == expected_lines  # Перевіряємо, що отримані рядки відповідають очікуваним

    os.remove(output_filename)  # Видаляємо вихідний файл після тесту
