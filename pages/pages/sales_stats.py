import streamlit as st
import pandas as pd
from analytics import calculate_revenue, export_product_analytics

def show_sales_stats():
    st.title("Статистика продаж")
    
    if 'data' not in st.session_state:
        st.warning("Сначала загрузите данные на главной странице")
        return
    
    data = st.session_state['data']
    
    # Выручка
    st.subheader("Выручка")
    total_revenue = calculate_revenue(data)
    st.metric("Общая выручка", f"{total_revenue:.2f} руб.")
    
    # Экспорт аналитики
    st.subheader("Экспорт данных")
    if st.button("Экспортировать аналитику по продуктам"):
        if export_product_analytics(data):
            st.success("Файл product_analytics.csv создан!")
    
    # Фильтры
    st.subheader("Фильтры")
    col1, col2 = st.columns(2)
    
    with col1:
        if 'category' in data.columns:
            categories = ['Все'] + list(data['category'].unique())
            selected_category = st.selectbox("Выберите категорию", categories)
            
            if selected_category != 'Все':
                filtered_data = data[data['category'] == selected_category]
                category_revenue = (filtered_data['price'] * filtered_data['quantity']).sum()
                st.write(f"Выручка в категории {selected_category}: {category_revenue:.2f} руб.")
