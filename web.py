import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)





st.title("My Todo App")
cnt = 0
for todo in todos:
    cnt += 1
    st.checkbox(todo, key=f'todo_{cnt}')

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

print("hello")
st.session_state