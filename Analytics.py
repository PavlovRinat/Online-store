import pandas as pd
from datetime import datetime

def calculate_revenue(data):
    #Считает общую выручку
    if 'price' not in data.columns or 'quantity' not in data.columns:
        print("Ошибка: нет колонок price или quantity")
        return 0
    
    data['revenue'] = data['price'] * data['quantity']
    total_revenue = data['revenue'].sum()
    print(f"Общая выручка: {total_revenue:.2f} руб.")
    return total_revenue

def get_top_products(data, n=5):
    #Возвращает топ-N продуктов по продажам
    try:
        product_stats = {}
        for _, row in data.iterrows():
            product = row['product']
            revenue = row['price'] * row['quantity']
            
            if product not in product_stats:
                product_stats[product] = 0
            product_stats[product] += revenue
        
        # Сортируем по убыванию выручки
        sorted_products = sorted(product_stats.items(), key=lambda x: x[1], reverse=True)
        return sorted_products[:n]
    except Exception as e:
        print(f"Ошибка при анализе продуктов: {e}")
        return []

def export_product_analytics(data, filename='product_analytics.csv'):
    #Экспортирует аналитику по продуктам в CSV
    try:
        product_stats = {}
        for _, row in data.iterrows():
            product = row['product']
            revenue = row['price'] * row['quantity']
            quantity = row['quantity']
            
            if product not in product_stats:
                product_stats[product] = {'revenue': 0, 'quantity': 0}
            
            product_stats[product]['revenue'] += revenue
            product_stats[product]['quantity'] += quantity
        
        # Создаем DataFrame для экспорта
        export_data = []
        for product, stats in product_stats.items():
            export_data.append({
                'product': product,
                'total_revenue': stats['revenue'],
                'total_quantity': stats['quantity']
            })
        
        df_export = pd.DataFrame(export_data)
        df_export.to_csv(filename, index=False)
        print(f"Аналитика экспортирована в {filename}")
        return True
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")
        return False
