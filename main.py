import streamlit as st
from agents.manager import ManagerAgent

st.set_page_config(page_title="🧠 Multi-Agent System", layout="wide")

# Custom CSS for sidebar & main content
custom_css = """
<style>
/* Sidebar styling */
[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #4B6CB7 0%, #182848 100%);
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
[data-testid="stSidebar"] .css-1d391kg {
    padding: 1rem 1rem 1rem 1rem;
}
[data-testid="stSidebar"] h2 {
    color: #FFD700;
    font-weight: bold;
    margin-bottom: 1rem;
}
[data-testid="stSidebar"] a {
    color: #FFFFFF;
    text-decoration: none;
    font-size: 1.1rem;
    display: block;
    margin: 0.5rem 0;
    padding: 0.3rem;
    border-radius: 5px;
}
[data-testid="stSidebar"] a:hover {
    background-color: #FFD700;
    color: #182848;
    font-weight: bold;
}

/* Task history container in sidebar */
.sidebar-task-history {
    max-height: 300px;
    overflow-y: auto;
    margin-top: 1rem;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 10px;
    font-size: 0.9rem;
}

/* Main content styling */
.css-1d391kg {
    padding: 2rem 3rem 3rem 3rem;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Main page title style */
.main-title {
    color: #4B6CB7;
    font-weight: 900;
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

/* About page card */
.about-card {
    background-color: #f0f4f8;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    margin-top: 1rem;
    max-width: 700px;
}
<h3 style="
    color: #FFD700; 
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
    font-size: 30px; 
    font-weight: bold;
    text-shadow: 1px 1px 2px #555;
    margin-bottom: 10px;
">
    Aamna Ashraf Rajput
</h3>
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.markdown("## 🧠 Multi-Agent System")
    st.markdown("### Created by:")
    st.markdown("<h3 style='color:#FFD700'>Aamna Ashraf Rajput</h3>", unsafe_allow_html=True)
    
    page = st.radio("Navigate", ["Home", "About"])
    
    # Task History in Sidebar
    st.markdown("### 🕓 Task History")
    if "task_history" not in st.session_state or not st.session_state.task_history:
        st.info("No tasks yet.")
    else:
        with st.container():
            st.markdown('<div class="sidebar-task-history">', unsafe_allow_html=True)
            for entry in reversed(st.session_state.task_history):
                st.markdown(f"""
                    <div style="border-bottom:1px solid #ddd; padding-bottom:8px; margin-bottom:8px;">
                        <strong>🧾 Task:</strong><br> {entry['task']}<br>
                        <strong>🤖 Response:</strong><br> {entry['response'][:100]}...
                    </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# Initialize ManagerAgent
manager = ManagerAgent()

# Session state for task history
if "task_history" not in st.session_state:
    st.session_state.task_history = []

# Home page content
if page == "Home":
    st.markdown('<h1 class="main-title">🤖 Multi-Agent Assistant</h1>', unsafe_allow_html=True)
    st.markdown("Ask the **Manager Agent**, and it will delegate your task to the correct agent!")

    with st.form("task_form"):
        user_input = st.text_area("📝 Enter your task or question:", height=150)
        submitted = st.form_submit_button("🚀 Submit Task")

        if submitted and user_input.strip():
            with st.spinner("🤔 Manager is thinking..."):
                result = manager.handle_task(user_input)

            st.session_state.task_history.append({
                "task": user_input.strip(),
                "response": result
            })

            st.success("✅ Task completed by appropriate agent.")
            st.markdown(f"**🧠 Response:** {result}")

   # New task button after results
if st.session_state.task_history:
    if st.button("➕ Generate New Task"):
        st.session_state.task_history.clear()
        # No need for st.experimental_rerun()

# About page content
elif page == "About":
    st.markdown("""
    <style>
    .about-card {
        background: #d1d5db;  /* Slightly darker light gray */
        color: #333333;       
        border-radius: 15px;
        padding: 30px 40px;
        max-width: 700px;
        margin: 30px auto;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        animation: fadeInZoom 1s ease forwards;
    }

    .about-card h3 {
        font-size: 2.8rem;
        margin-bottom: 20px;
        text-align: center;
        font-weight: 900;
        letter-spacing: 1.2px;
        color: #1e40af;
        text-shadow: none;
    }

    .about-card p {
        font-size: 1.3rem;
        line-height: 1.7;
        margin-bottom: 18px;
        text-align: justify;
        color: #4b5563;
    }

    .about-card ul {
        margin-left: 20px;
        margin-bottom: 20px;
        font-size: 1.2rem;
        list-style-type: disc;
        color: #374151;
    }

    .about-card ul li {
        margin-bottom: 12px;
    }

    @keyframes fadeInZoom {
        0% {
            opacity: 0;
            transform: scale(0.95);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }
    </style>

    <div class="about-card">
        <h3>Multi-Agent System by Aamna Ashraf Rajput</h3>
        <p>This application demonstrates a multi-agent AI system built with Streamlit and Google Gemini models.</p>
        <p>The system delegates tasks intelligently among specialized agents such as Developer, Blogger, Manager, etc.</p>
        <p><strong>Features include:</strong></p>
        <ul>
            <li>Clean and responsive UI with sidebar navigation</li>
            <li>Session-based task history</li>
            <li>Clear, well-documented code generation and technical explanations by Developer Agent</li>
        </ul>
        <p>Created with passion and care for educational and productivity purposes.</p>
    </div>
    """, unsafe_allow_html=True)
