from data_loader import load_data
from analytics import calculate_revenue, get_top_products, show_sales_dynamics, export_analytics

def main():
    print("=" * 50)
    print("АНАЛИЗ ПРОДАЖ ИНТЕРНЕТ-МАГАЗИНА")
    print("=" * 50)
    
    # Запрос пути к файлу
    file_path = input("Введите путь к файлу с данными (CSV/JSON): ").strip()
    
    # Загрузка данных
    data = load_data(file_path)
    
    if data is None:
        print("Не удалось загрузить данные. Программа завершена.")
        return
    
    # Показываем первые строки для проверки
    print("\nПервые 5 строк данных:")
    print(data.head())
    
    # Выполняем анализ
    calculate_revenue(data)
    get_top_products(data, 5)
    show_sales_dynamics(data)
    
    # Предлагаем экспорт
    export_choice = input("\nЭкспортировать аналитику в CSV? (y/n): ").strip().lower()
    if export_choice == 'y':
        export_filename = input("Введите имя файла для экспорта (или нажмите Enter для 'product_analytics.csv'): ").strip()
        if not export_filename:
            export_filename = 'product_analytics.csv'
        export_analytics(data, export_filename)
    
    print("\n" + "=" * 50)
    print("Анализ завершен!")
    print("=" * 50)

if __name__ == "__main__":
    main()
