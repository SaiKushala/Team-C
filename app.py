import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Team C Dashboard",
    layout="wide",
)

# Sidebar for navigation and user commands
st.sidebar.title("Team C Assistant")
st.sidebar.markdown("I can help you manage tasks, teams, and generate reports. Use the commands below:")
st.sidebar.button("Create Project Charter")
st.sidebar.button("Upload Documents")
st.sidebar.button("Plan Tasks")
st.sidebar.button("Generate Reports")
st.sidebar.button("Set Reminders")
st.sidebar.button("Help & Support")

# ---- Main Page ---- #
st.title("Team C Project Management Dashboard")
st.markdown("---")


# Search Section with Placeholder and Icons
st.markdown("""
    <style>
        .stTextInput>div>div>input {
            font-size: 16px;
            padding-left: 35px;
        }
        .stTextInput>div>div>button {
            background-color: transparent;
            border: none;
            position: absolute;
            left: 5px;
            top: 5px;
        }
        .search-icon {
            font-size: 24px;
            color: #333;
        }
    </style>
    """, unsafe_allow_html=True)



# Display the upload and send request icons
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <button style="border: none; background-color: transparent;">
            <i class="fas fa-upload search-icon"></i>
        </button>
        <button style="border: none; background-color: transparent;">
            <i class="fas fa-paper-plane search-icon"></i>
        </button>
    </div>
    """, unsafe_allow_html=True)

# Define DataFrames for Task Management
tasks = [
    {"Task": "Implement new chat interface components", "Status": "In Progress", "Due Date": "Dec 20, 2024"},
    {"Task": "Connect with external services", "Status": "Completed", "Due Date": "Dec 10, 2024"},
    {"Task": "Write technical documentation", "Status": "Pending", "Due Date": "Dec 30, 2024"},
]
tasks_df = pd.DataFrame(tasks)


# Container for Active Projects and Quick Actions
with st.container():
    
    col1, col2 = st.columns([2, 1])

    with col1:
        # Display Active Tasks Table
        st.write("### Active Tasks")
        st.dataframe(tasks_df, width=800)

    with col2:
        # Quick Actions Buttons
        st.write("### Quick Actions")
        if st.button("Create Project"):
            st.success("Project Created Successfully!")
        if st.button("Generate Report"):
            st.success("Report Generated Successfully!")
        if st.button("Set Reminder"):
            st.success("Reminder Set Successfully!")

# Progress Overview
st.write("## Project Updates")
project_updates = [
    "**Frontend Deployment**: ✅ Completed",
    "**API Integration**: 🛠️ In Progress",
    "**Bug Fixes**: ⏳ Pending Review",
]
# Display Project Updates in a container
with st.container():
    for update in project_updates:
        st.markdown(f"- {update}")

# Daily Summary
st.write("## Daily Summary")
with st.container():
   st.write("Frontend deployment completed")
# Integrations Section
st.write("## Integrations")
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Connect Google Docs"):
            st.success("Google Docs connected successfully!")
    with col2:
        if st.button("Connect MS Word"):
            st.success("MS Word connected successfully!")
    with col3:
        if st.button("Connect Slack"):
            st.success("Slack connected successfully!")
    with col4:
        if st.button("Export PDF"):
            st.success("PDF generated successfully!")

# Add the search box with a placeholder
search_input = st.text_input(
    label="",
    placeholder="Search Projects, Documents, and Tasks",
    key="search_input"
)

# Search Functionality Implementation
if search_input:
    st.write(f" You searched for: **{search_input}**")
    filtered_tasks = tasks_df[tasks_df["Task"].str.contains(search_input, case=False)]
    if not filtered_tasks.empty:
        st.dataframe(filtered_tasks)
    else:
        st.warning("No tasks or projects match your search query.")

# Footer
st.markdown("---")

