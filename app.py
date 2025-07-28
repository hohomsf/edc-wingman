import streamlit as st
from new_raw import data_catalog  # Your structured catalog goes here
from wingman_api import single_query_search
import time  # Simulating delay (can be removed when using real backend)

# Page config
st.set_page_config(page_title="Wingman", layout="wide")

# Add top padding and minor styling
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
        }
        .chat-box {
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)



st.markdown("""
<div style='padding-top: 40px;'></div>
""", unsafe_allow_html=True)

# Layout: 2 columns
left, right = st.columns([1, 2], gap="large")

# ---------------- Left Panel: Wingman Data Catalog ----------------
with left:
    st.subheader("📂 EDC Explorer")

    for db in data_catalog:
        with st.expander(f"🗄️ {db['database_code']}"):
            st.markdown(f"📘 Description: {db['database_description']}")
            for table in db["tables"]:
                with st.expander(f"📁 {table['table_name']}"):
                    st.markdown(f"📝 {table['table_description']}")
                    st.markdown("**📌 Fields:**")
                    for field in table["fields"]:
                        st.markdown(f"""
                            <div class='chat-box'>
                            <b>🧾 Field:</b> <code>{field['field_name']}</code><br>
                            <b>📛 Name:</b> {field['business_name']}<br>
                            <b>📄 Description:</b> {field['business_description']}<br>
                            <b>🔤 Type:</b> {field['data_type']} ({field.get('length', '-')})<br>
                            <b>🏷️ Tags:</b> {', '.join(field.get('tags', []))}<br>
                            <b>🔍 Sample Values:</b> {', '.join(field.get('sample_values', [])[:3])}
                            </div>
                        """, unsafe_allow_html=True)

# ---------------- Right Panel: Chat Interface ----------------
with right:
   
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="chat_input")

    if user_input:
        with st.spinner("Thinking..."):
            # Simulate delay (replace with real model/backend call)
            message = single_query_search(user_input)
            print('Message Recieved:::::::::::::::::::::::::')
            print(message)
            # Dummy chatbot logic (replace this with your actual logic)
            def get_bot_response(message):
                return f"🤖 Echo: {message}"

            bot_reply = get_bot_response(message)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Wingman", bot_reply))

    # Display chat history
    for sender, msg in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {msg}")

