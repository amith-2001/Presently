import streamlit as st
from PIL import Image
import json
import os

# Set page configuration
st.set_page_config(page_title="Presentation Tool", page_icon=":sparkles:")

# Initialize navigation state if not already set
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'welcome'

# Function to display the welcome page
def welcome_page():
    st.title("Welcome to the Presentation Tool!")
    st.write("This tool helps you create stunning presentations by choosing predefined templates.")
    if st.button("Go to Template Selection"):
        st.session_state.current_page = 'choose_template'

# Function to display the template selection page
def choose_template_page():
    st.title("Choose Your PowerPoint Template")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Template 1")
        template1_path = "template1.png"
        if os.path.exists(template1_path):
            st.image(template1_path, caption="Template 1 Example")
        else:
            st.error("Error: Template 1 image not found!")
        if st.button("Choose Template 1", key="btn1"):
            st.session_state.current_page = 'selected_template1'
            st.success("You have selected Template 1!")

    with col2:
        st.header("Template 2")
        template2_path = "template2.png"
        if os.path.exists(template2_path):
            st.image(template2_path, caption="Template 2 Example")
        else:
            st.error("Error: Template 2 image not found!")
        if st.button("Choose Template 2", key="btn2"):
            st.session_state.current_page = 'selected_template2'
            st.success("You have selected Template 2!")




def template2():
    

    # Initialize or reset session state to store the data
    def reset_state():
        st.session_state.title_text = "Click to add title"
        st.session_state.left_content_text = "Click to add text on left"
        st.session_state.right_content_text = "Click to add text on right"
        st.session_state.left_image_data = None
        st.session_state.right_image_data = None
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
        st.session_state.left_content_text = st.text_area("Enter Left Content Text", st.session_state.left_content_text)
        st.session_state.right_content_text = st.text_area("Enter Right Content Text", st.session_state.right_content_text)
        
        uploaded_left_file = st.file_uploader("Upload Left Image", type=['png', 'jpg', 'jpeg'], key=f"left-{st.session_state.slide_index}")
        uploaded_right_file = st.file_uploader("Upload Right Image", type=['png', 'jpg', 'jpeg'], key=f"right-{st.session_state.slide_index}")
        
        if uploaded_left_file:
            st.session_state.left_image_data = Image.open(uploaded_left_file)

        if uploaded_right_file:
            st.session_state.right_image_data = Image.open(uploaded_right_file)

        if st.button("New Slide"):
            reset_state()

        if st.button("Save"):
            # Read existing data or initialize empty list
            if os.path.exists("presentation_data.json"):
                try:
                    # add_data()
                    with open("presentation_data.json", "r") as file:
                        slides_data = json.load(file)
                except json.JSONDecodeError:
                    slides_data = []
            else:
                slides_data = []
            
            # Append new slide data
            new_slide_data = {
                f"Slide {st.session_state.slide_index}": {
                    "title": st.session_state.title_text,
                    "left_content": st.session_state.left_content_text,
                    "right_content": st.session_state.right_content_text
                }
            }
            slides_data.append(new_slide_data)

            # Write updated data back to the file
            with open("presentation_data.json", "w") as file:
                json.dump(slides_data, file, indent=4)
            st.success("Slide data saved successfully!")

    # Main presentation area
    st.title(st.session_state.title_text)

    # Two columns for content
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.left_content_text)
        if st.session_state.left_image_data:
            st.image(st.session_state.left_image_data, caption='Uploaded Left Image', use_column_width=True)
    
    with col2:
        st.write(st.session_state.right_content_text)
        if st.session_state.right_image_data:
            st.image(st.session_state.right_image_data, caption='Uploaded Right Image', use_column_width=True)










            

# Function to display the selected template confirmation
def selected_template(template_number):
    st.title(f"You have selected Template {template_number}")
    st.write("Here you can start customizing your template or download it to start working locally.")
    if st.button("Back to templates"):
        st.session_state.current_page = 'choose_template'

# Navigation logic
if st.session_state.current_page == 'welcome':
    welcome_page()
elif st.session_state.current_page == 'choose_template':
    choose_template_page()
elif st.session_state.current_page == 'selected_template1':
    selected_template(1)
elif st.session_state.current_page == 'selected_template2':
    template2()
