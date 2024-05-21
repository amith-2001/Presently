import streamlit as st
from PIL import Image
import os
import json
import pandas as pd
from backend.save_data import *

def chatbot_interface():
    st.title("Chatbot Interface")
    chat_input = st.text_input("Chatbot Input")
    if st.button("Send"):
        user_input = chat_input
        st.write("User Input:", user_input)

def template2():
    def reset_state():
        st.session_state.title_text = "Click to add title"
        st.session_state.left_content_type = "text"
        st.session_state.left_content_text = "Click to add text on left"
        st.session_state.left_image_data = None
        st.session_state.left_image_path = None
        st.session_state.left_graph_data = None

        st.session_state.right_content_type = "text"
        st.session_state.right_content_text = "Click to add text on right"
        st.session_state.right_image_data = None
        st.session_state.right_image_path = None
        st.session_state.right_graph_data = None

        st.session_state.slide_index = st.session_state.get('slide_index', 0) + 1
        st.session_state.show_left_graph_popup = False
        st.session_state.show_right_graph_popup = False
        st.session_state.previous_screen = None

    def save_image(image, side):
        image_dir = 'uploaded_images'
        os.makedirs(image_dir, exist_ok=True)
        image_path = os.path.join(image_dir, f"{side}_slide_{st.session_state.slide_index}.png")
        image.save(image_path)
        return image_path

    if 'title_text' not in st.session_state:
        st.session_state.slide_index = 1
        reset_state()

    if st.session_state.show_left_graph_popup or st.session_state.show_right_graph_popup:
        if st.session_state.show_left_graph_popup:
            st.title("Upload CSV for Left Graph")
            uploaded_csv = st.file_uploader("Upload CSV File", type=['csv'], key="left_graph_uploader")
            if uploaded_csv:
                df = pd.read_csv(uploaded_csv)
                st.session_state.left_graph_data = df
                st.session_state.show_left_graph_popup = False
                st.success("CSV file uploaded successfully!")
                st.experimental_rerun()
            if st.button("Back"):
                st.session_state.show_left_graph_popup = False
                st.experimental_rerun()

        if st.session_state.show_right_graph_popup:
            st.title("Upload CSV for Right Graph")
            uploaded_csv = st.file_uploader("Upload CSV File", type=['csv'], key="right_graph_uploader")
            if uploaded_csv:
                df = pd.read_csv(uploaded_csv)
                st.session_state.right_graph_data = df
                st.session_state.show_right_graph_popup = False
                st.success("CSV file uploaded successfully!")
                st.experimental_rerun()
            if st.button("Back"):
                st.session_state.show_right_graph_popup = False
                st.experimental_rerun()

    else:
        with st.sidebar:
            st.header("Controls")
            st.session_state.title_text = st.text_input("Enter Title Text", st.session_state.title_text)

            st.subheader("Left Content")
            left_content_key = f"left_content_{st.session_state.slide_index}"
            st.session_state.left_content_type = st.radio("Select Content Type", ["text", "image", "graph"], key=left_content_key, index=0)
            if st.session_state.left_content_type == "text":
                st.session_state.left_content_text = st.text_area("Enter Left Content Text", st.session_state.left_content_text)
                st.session_state.left_image_data = None
                st.session_state.left_image_path = None
                st.session_state.left_graph_data = None
            elif st.session_state.left_content_type == "image":
                uploaded_left_file = st.file_uploader("Upload Left Image", type=['png', 'jpg', 'jpeg'], key=f"left-{st.session_state.slide_index}")
                if uploaded_left_file:
                    image = Image.open(uploaded_left_file)
                    st.session_state.left_image_data = image
                    st.session_state.left_image_path = save_image(image, 'left')
                    st.session_state.left_content_text = None
                    st.session_state.left_graph_data = None
            elif st.session_state.left_content_type == "graph":
                st.session_state.show_left_graph_popup = True
                st.experimental_rerun()

            st.subheader("Right Content")
            right_content_key = f"right_content_{st.session_state.slide_index}"
            st.session_state.right_content_type = st.radio("Select Content Type", ["text", "image", "graph"], key=right_content_key, index=0)
            if st.session_state.right_content_type == "text":
                st.session_state.right_content_text = st.text_area("Enter Right Content Text", st.session_state.right_content_text)
                st.session_state.right_image_data = None
                st.session_state.right_image_path = None
                st.session_state.right_graph_data = None
            elif st.session_state.right_content_type == "image":
                uploaded_right_file = st.file_uploader("Upload Right Image", type=['png', 'jpg', 'jpeg'], key=f"right-{st.session_state.slide_index}")
                if uploaded_right_file:
                    image = Image.open(uploaded_right_file)
                    st.session_state.right_image_data = image
                    st.session_state.right_image_path = save_image(image, 'right')
                    st.session_state.right_content_text = None
                    st.session_state.right_graph_data = None
            elif st.session_state.right_content_type == "graph":
                st.session_state.show_right_graph_popup = True
                st.experimental_rerun()

            if st.button("New Slide"):
                reset_state()

            if st.button("Save"):
                if os.path.exists("presentation_data.json"):
                    try:
                        
                        with open("presentation_data.json", "r") as file:
                            slides_data = json.load(file)
                    except json.JSONDecodeError:
                        slides_data = []
                else:
                    slides_data = []

                new_slide_data = {
                    f"Slide {st.session_state.slide_index}": {
                        "title": st.session_state.title_text,
                        "left_content_type": st.session_state.left_content_type,
                        "left_content": st.session_state.left_content_text,
                        "left_image_path": st.session_state.left_image_path,
                        "left_graph_data": st.session_state.left_graph_data.to_dict() if st.session_state.left_graph_data is not None else None,
                        "right_content_type": st.session_state.right_content_type,
                        "right_content": st.session_state.right_content_text,
                        "right_image_path": st.session_state.right_image_path,
                        "right_graph_data": st.session_state.right_graph_data.to_dict() if st.session_state.right_graph_data is not None else None
                    }
                }
                slides_data.append(new_slide_data)
                add_data(new_slide_data)

                with open("presentation_data.json", "w") as file:
                    json.dump(slides_data, file, indent=4)
                st.success("Slide data saved successfully!")

        st.title(st.session_state.title_text)

        col1, col2 = st.columns(2)
        with col1:
            if st.session_state.left_content_type == "text":
                st.write(st.session_state.left_content_text)
            elif st.session_state.left_content_type == "image":
                if st.session_state.left_image_data:
                    st.image(st.session_state.left_image_data, caption='Uploaded Left Image', use_column_width=True)
            elif st.session_state.left_content_type == "graph" and st.session_state.left_graph_data is not None:
                st.write("Graph Placeholder")
                st.write(st.session_state.left_graph_data)

        with col2:
            if st.session_state.right_content_type == "text":
                st.write(st.session_state.right_content_text)
            elif st.session_state.right_content_type == "image":
                if st.session_state.right_image_data:
                    st.image(st.session_state.right_image_data, caption='Uploaded Right Image', use_column_width=True)
            elif st.session_state.right_content_type == "graph" and st.session_state.right_graph_data is not None:
                st.write("Graph Placeholder")
                st.write(st.session_state.right_graph_data)

if st.button("Open Chatbot Interface"):
    chatbot_interface()
else:
    template2()
