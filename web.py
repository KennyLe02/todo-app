import streamlit as st
import functions

todos = functions.getTodos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.getTodos()

st.title("My Todo App")
st.subheader("Easily add and complete tasks")
st.write("The purpose of this app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "",placeholder="Enter a new todo...",
              on_change=add_todo,key="new_todo")

# st.session_state