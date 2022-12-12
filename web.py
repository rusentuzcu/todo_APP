import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
cnt = 0
for todo in todos:
    cnt += 1
    st.checkbox(todo, key=f'todo_{cnt}')

st.text_input(label="", placeholder="Add a new todo...")