import streamlit as st
from pages import home, sales_stats, products

# Настройка страницы
st.set_page_config(
    page_title="Анализ продаж",
    page_icon="📊",
    layout="wide"
)

# Сайдбар с навигацией
st.sidebar.title("Навигация")
page = st.sidebar.radio("Выберите страницу:", [
    "Главная",
    "Статистика продаж", 
    "Топ продукты"
])

# Показываем выбранную страницу
if page == "Главная":
    home.show_home()
elif page == "Статистика продаж":
    sales_stats.show_sales_stats()
elif page == "Топ продукты":
    products.show_products()
