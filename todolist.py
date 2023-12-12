import time
import streamlit as st

st.title("To Do List")

task = ["haha"]
task_columns = st.columns(1)

for i, c in enumerate(task_columns):
    if i<len(task):
        c.write(task[i])

task_name = st.text_input('Task Name')

clicked = st.button("Add Task", type="primary")
if clicked == True:
    info = st.info(f"your task {task_name} has been added")
    time.sleep(2)
    task.append(task_name)
    info.empty()
