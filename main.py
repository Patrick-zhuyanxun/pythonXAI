import streamlit as st

st.title("這是標題")
st.write("這是一個用st.write()'函數寫入的文字。")
st.markdown(
    """
這是使用`st.markdown()`函數寫入的文字，可以處理markdown的語法。
例如:
- **粗體**文字
- *斜體*文字
- `程式碼`片段
- [連結](https://www.example.com)

"""
)
# to run the app, use the command:
# streamlit run main.py
