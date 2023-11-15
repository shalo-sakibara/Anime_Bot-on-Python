import json


def add_key_value_to_json(key, value):
    # Открытие файла в режиме чтения
    with open('base_data.json', 'r') as file:
        # Загрузка данных из файла
        data = json.load(file)

        # Добавление ключа и значения в данные
        data[key] = value

    # Открытие файла в режиме записи
    with open('base_data.json', 'w') as file:
        # Запись обновленных данных в файл
        json.dump(data, file)
    return "Вы подписали рассылку"


def admin_read_json():
    # Открытие файла в режиме чтения
    with open('base_data.json', 'r') as file:
        data = json.load(file)
        return data
