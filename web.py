import streamlit as st 
import google.generativeai as genai

# Configure Google API Key
api_key = "AIzaSyCl2DDXFdXy09KZCfiR2kYO-NT4Rpsbc8w"  # Replace with your actual API key
try:
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Error configuring API: {e}")
    st.stop()

# Apply custom CSS for ruby red background, white boxes, and red dropdown with cornering
st.markdown("""
    <style>
        body {
            background-color: #9B111E; /* Ruby red background */
            color: white; /* White text */
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: #9B111E;
            color: white; /* White text */
        }
        .stTextInput, .stTextArea, .stSelectbox, .stButton > button {
            background-color: white; /* White background for input boxes */
            color: #990000; /* Red text */
            border: 2px solid #990000; /* Red border */
            border-radius: 10px; /* Rounded corners */
            padding: 10px;
        }
        .stButton > button:hover {
            background-color: #990000; /* Red hover */
            color: white; /* White text on hover */
        }
        h1, h2, h3, .stSidebar {
            color: white; /* White headings */
            font-family: 'Times New Roman', Times, serif; /* Title font */
        }
        .stMarkdown p {
            color: white;
            font-size: 14px;
        }
        .stSidebar {
            background-color: #9B111E; /* Ruby red sidebar */
            border-right: 2px solid white; /* White sidebar accent */
        }
        .stSelectbox select {
            background-color: red; /* Red background for dropdown */
            color: white; /* White text in dropdown */
            border-radius: 10px; /* Rounded corners for dropdown */
        }
        .stMarkdown {
            border-top: 5px solid white; /* White thick line above footer */
            padding-top: 10px; /* Space above the line */
            padding-bottom: 10px; /* Space below the line */
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Sanjivani AI Based Content Generator")

# Sidebar for Navigation
feature = st.sidebar.selectbox("Choose a Feature", [
    "Generate Content",
    "Create Social Media Post",
    "Generate Ideas for Content Creation",
    "Generate Video Script",
    "Generate Digital Marketing Ideas"
])

# Content Generation Function
def generate_google_content(prompt, model="gemini-1.5-flash"):
    try:
        model_instance = genai.GenerativeModel(model)
        response = model_instance.generate_content(prompt)
        # Clean output: Remove unwanted characters like *, #
        clean_text = response.text.replace("*", "").replace("#", "").strip()
        return clean_text
    except Exception as e:
        return f"Error: {e}"

# Features
if feature == "Generate Content":
    st.subheader("Content Generator")
    topic = st.text_area("Enter the topic or key details for the content:")
    if st.button("Generate Content"):
        with st.spinner("Generating content..."):  # Loader spinner
            prompt = f"Create an content focused on Sanjivani Group of Institutes and Sanjivani University: {topic}"
            result = generate_google_content(prompt)
            st.text_area("Generated Content", result, height=200)

elif feature == "Create Social Media Post":
    st.subheader("Social Media Post Generator")
    event = st.text_input("Enter the event or topic:")
    if st.button("Generate Social Media Post"):
        with st.spinner("Generating content..."):  # Loader spinner
            prompt = f"Write a social media post about Sanjivani Group of Institutes and Sanjivani University for event: {event}"
            result = generate_google_content(prompt)
            st.text_area("Generated Content for Post", result, height=200)

elif feature == "Generate Ideas for Content Creation":
    st.subheader("Ideas for Content Creation")
    topic = st.text_input("Enter the theme or topic for content creation:")
    if st.button("Generate Content Ideas"):
        with st.spinner("Generating ideas..."):  # Loader spinner
            prompt = f"Generate creative ideas for content creation focused on Sanjivani University for theme: {topic}"
            result = generate_google_content(prompt)
            st.text_area("Generated Ideas", result, height=200)

elif feature == "Generate Video Script":
    st.subheader("Video Script Generator")
    topic = st.text_area("Enter the video topic or main points:")
    if st.button("Generate Video Script"):
        with st.spinner("Generating content..."):  # Loader spinner
            prompt = f"Create a video script for Sanjivani Group of Institutes and Sanjivani University based on: {topic}"
            result = generate_google_content(prompt)
            st.text_area("Generated Video Script", result, height=200)

elif feature == "Generate Digital Marketing Ideas":
    st.subheader("Digital Marketing Ideas Generator")
    topic = st.text_input("Enter the digital marketing theme or platform:")
    if st.button("Generate Digital Marketing Ideas"):
        with st.spinner("Generating ideas..."):  # Loader spinner
            prompt = f"Generate digital marketing ideas for Sanjivani Group of Institutes and Sanjivani University for platform: {topic}"
            result = generate_google_content(prompt)
            st.text_area("Generated Digital Marketing Ideas", result, height=200)

# Footer
st.markdown("---")
st.markdown("Created By **Tushar**")
