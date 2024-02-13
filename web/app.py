import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Task Manager")

st.header("Create Task")
task_title = st.text_input("Task Title")  
task_desc = st.text_area("Task Description")
if st.button("Create Task"):
    task = {'title': task_title, 'description': task_desc}
    res = requests.post(f"{API_URL}/tasks/", json=task)
    if res.status_code == 200:
        st.success("Task Created")
    st.json(res.json())
        
st.header("Get Tasks")
res = requests.get(f"{API_URL}/tasks/")
st.json(res.json())

st.header("Update Task")
task_id = st.text_input("Enter Task ID")
updated_title = st.text_input("Updated Title")
updated_desc = st.text_area("Updated Description")  
if st.button("Update Task"):
    updated_task = {'title': updated_title, 'description': updated_desc} 
    res = requests.put(f"{API_URL}/tasks/{task_id}", json=updated_task)
    if res.status_code == 200:
        st.success("Task Updated")
    st.json(res.json())
    
st.header("Delete Task")
task_id = st.text_input("Enter Task ID")
if st.button("Delete Task"):
    res = requests.delete(f"{API_URL}/tasks/{task_id}")
    if res.status_code == 200:
        st.success("Task Deleted")
    st.json(res.json())