import pandas as pd
from datetime import datetime

def calculate_revenue(data):
    #Считает общую выручку
    print("\n=== РАСЧЕТ ВЫРУЧКИ ===")
    
    # Проверяем нужные колонки
    if 'price' not in data.columns or 'quantity' not in data.columns:
        print("Ошибка: в данных нет колонок 'price' или 'quantity'")
        return 0
    
    # Считаем выручку
    data['revenue'] = data['price'] * data['quantity']
    total_revenue = data['revenue'].sum()
    
    print(f"Общая выручка: {total_revenue:.2f} руб.")
    print(f"Всего продаж: {data['quantity'].sum()} шт.")
    print(f"Средний чек: {total_revenue / len(data):.2f} руб.")
    
    return total_revenue

def get_top_products(data, top_n=5):
    """Возвращает топ-N продуктов по продажам"""
    print(f"\n=== ТОП-{top_n} ПРОДУКТОВ ===")
    
    if 'product' not in data.columns:
        print("Ошибка: в данных нет колонки 'product'")
        return []
    
    # Группируем по продуктам
    product_stats = {}
    for _, row in data.iterrows():
        product = row['product']
        revenue = row['price'] * row['quantity']
        
        if product not in product_stats:
            product_stats[product] = {'revenue': 0, 'quantity': 0}
        
        product_stats[product]['revenue'] += revenue
        product_stats[product]['quantity'] += row['quantity']
    
    # Сортируем по выручке
    sorted_products = sorted(product_stats.items(), 
                           key=lambda x: x[1]['revenue'], 
                           reverse=True)
    
    # Выводим топ
    for i, (product, stats) in enumerate(sorted_products[:top_n], 1):
        print(f"{i}. {product}:")
        print(f"   Выручка: {stats['revenue']:.2f} руб.")
        print(f"   Продано: {stats['quantity']} шт.")
    
    return sorted_products[:top_n]

def show_sales_dynamics(data):
    """Показывает динамику продаж по дням"""
    print("\n=== ДИНАМИКА ПРОДАЖ ===")
    
    if 'date' not in data.columns:
        print("Ошибка: в данных нет колонки 'date'")
        return
    
    # Группируем по дате
    data['date'] = pd.to_datetime(data['date'])
    daily_sales = data.groupby(data['date'].dt.date).agg({
        'revenue': 'sum',
        'quantity': 'sum'
    }).reset_index()
    
    print("Продажи по дням:")
    for _, row in daily_sales.iterrows():
        print(f"   {row['date']}: {row['revenue']:.2f} руб. ({row['quantity']} шт.)")

def export_analytics(data, filename='product_analytics.csv'):
    """Экспортирует аналитику по продуктам в CSV"""
    print(f"\n=== ЭКСПОРТ ДАННЫХ ===")
    
    try:
        # Собираем статистику по продуктам
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
                'total_quantity': stats['quantity'],
                'average_price': stats['revenue'] / stats['quantity'] if stats['quantity'] > 0 else 0
            })
        
        df_export = pd.DataFrame(export_data)
        df_export.to_csv(filename, index=False, encoding='utf-8')
        print(f"Данные экспортированы в файл: {filename}")
        print(f"Экспортировано записей: {len(df_export)}")
        
        return True
        
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")
        return False
