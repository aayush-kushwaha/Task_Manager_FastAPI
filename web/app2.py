import streamlit as st
import requests

API_URL = "http://localhost:8000"

def create_task():
    st.header("Create Task")
    task_title = st.text_input("Task Title")  
    task_desc = st.text_area("Task Description")
    if st.button("Create Task"):
        task = {'title': task_title, 'description': task_desc}
        try:
            res = requests.post(f"{API_URL}/tasks/", json=task)
            res_json = res.json()
            if res.status_code == 200:
                st.success("Task Created")
            st.json(res_json)
        except requests.RequestException as e:
            st.error(f"Error creating task: {e}")

def get_tasks():
    st.header("Get Tasks")
    try:
        res = requests.get(f"{API_URL}/tasks/")
        res_json = res.json()
        st.json(res_json)
    except requests.RequestException as e:
        st.error(f"Error getting tasks: {e}")

def update_task():
    st.header("Update Task")
    task_id = st.text_input("Enter Task ID")
    updated_title = st.text_input("Updated Title")
    updated_desc = st.text_area("Updated Description")  
    if st.button("Update Task"):
        updated_task = {'title': updated_title, 'description': updated_desc} 
        try:
            res = requests.put(f"{API_URL}/tasks/{task_id}", json=updated_task)
            res_json = res.json()
            if res.status_code == 200:
                st.success("Task Updated")
            st.json(res_json)
        except requests.RequestException as e:
            st.error(f"Error updating task: {e}")

def delete_task():
    st.header("Delete Task")
    task_id = st.text_input("Enter Task ID")
    if st.button("Delete Task"):
        try:
            res = requests.delete(f"{API_URL}/tasks/{task_id}")
            res_json = res.json()
            if res.status_code == 200:
                st.success("Task Deleted")
            st.json(res_json)
        except requests.RequestException as e:
            st.error(f"Error deleting task: {e}")

# Main Streamlit App
st.title("Task Manager")

# Menu Selection
menu_option = st.sidebar.radio("Select Option", ["Create Task", "Get Tasks", "Update Task", "Delete Task"])

# Perform the selected action
if menu_option == "Create Task":
    create_task()
elif menu_option == "Get Tasks":
    get_tasks()
elif menu_option == "Update Task":
    update_task()
elif menu_option == "Delete Task":
    delete_task()
