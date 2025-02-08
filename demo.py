# import streamlit as st
# import ollama

# st.title("💡 AI Decision Maker")

# query = st.text_input("Enter your decision-making question:")

# if st.button("Get AI Decision"):
#     if query:
#         response = ollama.chat(
#             model="llama3.3",
#             messages=[{"role": "user", "content": query}]
#         )
#         st.write("### 🤖 AI's Decision:")
#         st.write(response["message"]["content"])
#     else:
#         st.warning("Please enter a question!")

import streamlit as st
import ollama
import time

# Page Configuration
st.set_page_config(
    page_title="AI Decision Maker",
    page_icon="💡",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color:#f4f4f4;
        }
        .stButton>button {
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 18px !important;
            padding: 10px 20px !important;
            border-radius: 8px !important;
        }
        .stTextInput>div>div>input {
            font-size: 18px;
        }
        .response-box {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            font-size: 16px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 style='text-align: center; color: #333;'>💡 AI Decision Maker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Get smart AI-powered decisions instantly.</p>", unsafe_allow_html=True)

# User Input Section
query = st.text_input("🔎 Enter your decision-making question:", placeholder="e.g., Should I invest in AI stocks?")

# Button to Get AI Decision
if st.button("🔮 Get AI Decision"):
    if query:
        with st.spinner("🤖 AI is thinking..."):
            time.sleep(2)  # Simulate processing time
            
            # AI Response from DeepSeek-R1:7B
            response = ollama.chat(
                model="deepseek-r1:7b",
                messages=[{"role": "user", "content": query}]
            )

            # Display Response
            st.markdown("### 🤖 AI's Decision:")
            st.markdown(f"<div class='response-box'>{response['message']['content']}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a question!")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:14px;'>🚀 Powered by KalpeshMahajan</p>", unsafe_allow_html=True)
