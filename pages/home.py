import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(file)))

from data_loader import load_data

def show_home():
    st.title("Анализ продаж интернет-магазина")
    st.write("Загрузите файл с данными о продажах для анализа")
    
    uploaded_file = st.file_uploader("Выберите CSV или JSON файл", 
                                   type=['csv', 'json'])
    
    if uploaded_file is not None:
        # Сохраняем файл временно
        with open('temp_file', 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        # Загружаем данные
        data = load_data('temp_file')
        
        if data is not None:
            st.session_state['data'] = data
            st.success("Данные успешно загружены!")
            st.write("Первые 5 строк данных:")
            st.dataframe(data.head())
            
            # Показываем основную информацию
            st.subheader("Основная информация")
            st.write(f"Всего записей: {len(data)}")
            
            if 'price' in data.columns and 'quantity' in data.columns:
                total_revenue = (data['price'] * data['quantity']).sum()
                st.write(f"Общая выручка: {total_revenue:.2f} руб.")
