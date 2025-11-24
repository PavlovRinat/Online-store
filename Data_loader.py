import pandas as pd
import json

def load_data(file_path):
    """Загружает данные из CSV или JSON файла"""
    print(f"Пытаюсь загрузить файл: {file_path}")
    
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
            print("Файл CSV загружен успешно")
        elif file_path.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = pd.DataFrame(json.load(f))
            print("Файл JSON загружен успешно")
        else:
            print("Ошибка: поддерживаются только CSV и JSON файлы")
            return None
        
        print(f"Загружено записей: {len(data)}")
        print("Колонки в данных:", list(data.columns))
        return data
        
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден")
        return None
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return None
