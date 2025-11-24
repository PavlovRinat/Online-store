import streamlit as st
from analytics import get_top_products

def show_products():
    st.title("Топ продукты")
    
    if 'data' not in st.session_state:
        st.warning("Сначала загрузите данные на главной странице")
        return
    
    data = st.session_state['data']
    
    # Топ продукты
    top_n = st.slider("Количество продуктов в топе", 3, 10, 5)
    top_products = get_top_products(data, top_n)
    
    st.subheader(f"Топ-{top_n} продуктов по выручке")
    
    for i, (product, revenue) in enumerate(top_products, 1):
        st.write(f"{i}. {product}: {revenue:.2f} руб.")
