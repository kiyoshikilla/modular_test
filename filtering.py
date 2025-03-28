def filter_lines(input_filename, output_filename, keyword):
    try:
        with open(input_filename, "r", encoding="utf-8") as infile, open(output_filename, "w", encoding="utf-8") as outfile:
            filtered_lines = [line for line in infile if keyword.lower() in line.lower()]  # Фільтрація з урахуванням регістру
            outfile.writelines(filtered_lines)  # Запис відфільтрованих рядків у вихідний файл
        
        return True  # Повертаємо True, якщо фільтрація успішна
    except FileNotFoundError:
        print(f"Помилка: файл '{input_filename}' не знайдено.")
        return False
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return False