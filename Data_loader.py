import pandas as pd
import json

def load_data(file_path):
    #Загружает данные из CSV или JSON файла
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            with open(file_path, 'r') as f:
                data = pd.DataFrame(json.load(f))
        else:
            print("Ошибка: поддерживаются только CSV и JSON файлы")
            return None
        
        print(f"Успешно загружено {len(data)} записей")
        return data
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return None
