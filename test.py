import streamlit as st
from PIL import Image
import os
import json
import base64
from io import BytesIO
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('mongodb+srv://maxwelljohn123123:nRJWqRQxvjH4bnYu@stremlit-snowflake-hack.ul6jfec.mongodb.net/?retryWrites=true&w=majority&appName=Stremlit-Snowflake-hackathon')
db = client['ga']
collection = db['ma']

def chatbot_interface():
    st.title("Chatbot Interface")
    chat_input = st.text_input("Chatbot Input")
    if st.button("Send"):
        # Store the text entered by the user in a variable
        user_input = chat_input  # You can use this variable for further processing
        st.write("User Input:", user_input)

def template2():
    
    # Initialize or reset session state to store the data
    def reset_state():
        st.session_state.title_text = "Click to add title"
        st.session_state.left_content_type = "text"
        st.session_state.left_content_text = "Click to add text on left"
        st.session_state.left_image_data = None
        st.session_state.left_graph_data = None
        
        st.session_state.right_content_type = "text"
        st.session_state.right_content_text = "Click to add text on right"
        st.session_state.right_image_data = None
        st.session_state.right_graph_data = None
        
        # Increment the slide index
        st.session_state.slide_index = st.session_state.get('slide_index', 0) + 1

    # Check if it's the initial load of the template
    if 'title_text' not in st.session_state:
        st.session_state.slide_index = 1  # Start from slide 1
        reset_state()

    # Sidebar for inputs
    with st.sidebar:
        st.header("Controls")
        st.session_state.title_text = st.text_input("Enter Title Text", st.session_state.title_text)
        
        st.subheader("Left Content")
        left_content_key = f"left_content_{st.session_state.slide_index}"
        st.session_state.left_content_type = st.radio("Select Content Type", ["text", "image", "graph"], key=left_content_key, index=0)
        if st.session_state.left_content_type == "text":
            st.session_state.left_content_text = st.text_area("Enter Left Content Text", st.session_state.left_content_text)
            st.session_state.left_image_data = None
            st.session_state.left_graph_data = None
        elif st.session_state.left_content_type == "image":
            uploaded_left_file = st.file_uploader("Upload Left Image", type=['png', 'jpg', 'jpeg'], key=f"left-{st.session_state.slide_index}")
            if uploaded_left_file:
                st.session_state.left_image_data = Image.open(uploaded_left_file)
                st.session_state.left_content_text = None
                st.session_state.left_graph_data = None
        elif st.session_state.left_content_type == "graph":
            if st.button("Upload CSV for Left Graph"):
                uploaded_csv = st.file_uploader("Upload CSV File", type=['csv'])
                if uploaded_csv:
                    # Process the uploaded CSV file
                    st.success("CSV file uploaded successfully!")

                    # Here you can process the CSV file and generate the graph

        st.subheader("Right Content")
        right_content_key = f"right_content_{st.session_state.slide_index}"
        st.session_state.right_content_type = st.radio("Select Content Type", ["text", "image", "graph"], key=right_content_key, index=0)
        if st.session_state.right_content_type == "text":
            st.session_state.right_content_text = st.text_area("Enter Right Content Text", st.session_state.right_content_text)
            st.session_state.right_image_data = None
            st.session_state.right_graph_data = None
        elif st.session_state.right_content_type == "image":
            uploaded_right_file = st.file_uploader("Upload Right Image", type=['png', 'jpg', 'jpeg'], key=f"right-{st.session_state.slide_index}")
            if uploaded_right_file:
                st.session_state.right_image_data = Image.open(uploaded_right_file)
                st.session_state.right_content_text = None
                st.session_state.right_graph_data = None
        elif st.session_state.right_content_type == "graph":
            if st.button("Upload CSV for Right Graph"):
                uploaded_csv = st.file_uploader("Upload CSV File", type=['csv'])
                if uploaded_csv:
                    # Process the uploaded CSV file
                    st.success("CSV file uploaded successfully!")

                    # Here you can process the CSV file and generate the graph

        if st.button("New Slide"):
            reset_state()

        if st.button("Save"):
            # Read existing data or initialize empty list
            if os.path.exists("presentation_data.json"):
                try:
                    with open("presentation_data.json", "r") as file:
                        slides_data = json.load(file)
                except json.JSONDecodeError:
                    slides_data = []
            else:
                slides_data = []
            
            # Prepare left image data for JSON (convert to base64)
            left_image_base64 = None
            if st.session_state.left_image_data:
                buffered = BytesIO()
                st.session_state.left_image_data.save(buffered, format="PNG")
                left_image_base64 = base64.b64encode(buffered.getvalue()).decode()

            # Prepare right image data for JSON (convert to base64)
            right_image_base64 = None
            if st.session_state.right_image_data:
                buffered = BytesIO()
                st.session_state.right_image_data.save(buffered, format="PNG")
                right_image_base64 = base64.b64encode(buffered.getvalue()).decode()

            # Append new slide data
            new_slide_data = {
                f"Slide {st.session_state.slide_index}": {
                    "title": st.session_state.title_text,
                    "left_content_type": st.session_state.left_content_type,
                    "left_content": st.session_state.left_content_text,
                    "left_image_base64": left_image_base64,
                    "right_content_type": st.session_state.right_content_type,
                    "right_content": st.session_state.right_content_text,
                    "right_image_base64": right_image_base64
                }
            }
            slides_data.append(new_slide_data)

            # Write updated data back to the file
            with open("presentation_data.json", "w") as file:
                json.dump(slides_data, file, indent=4)
            st.success("Slide data saved successfully!")

            # Save data to MongoDB
            result = collection.insert_one(new_slide_data)
            st.success(f"Slide data also saved to MongoDB with id {result.inserted_id}")

    # Main presentation area
    st.title(st.session_state.title_text)

    # Two columns for content
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.left_content_type == "text":
            st.write(st.session_state.left_content_text)
        elif st.session_state.left_content_type == "image":
            if st.session_state.left_image_data:
                st.image(st.session_state.left_image_data, caption='Uploaded Left Image', use_column_width=True)
        elif st.session_state.left_content_type == "graph":
            # Placeholder for displaying graph
            st.write("Graph Placeholder")
    
    with col2:
        if st.session_state.right_content_type == "text":
            st.write(st.session_state.right_content_text)
        elif st.session_state.right_content_type == "image":
            if st.session_state.right_image_data:
                st.image(st.session_state.right_image_data, caption='Uploaded Right Image', use_column_width=True)
        elif st.session_state.right_content_type == "graph":
            # Placeholder for displaying graph
            st.write("Graph Placeholder")

# Open the chatbot interface in a new session
if st.button("Open Chatbot Interface"):
    chatbot_interface()
else:
    template2()
