import streamlit as st
from PIL import Image
import json
import os
import pandas as pd

def template2():
    st.set_page_config(page_title="Interactive Presentation Tool", layout="wide")

    def reset_state():
        st.session_state.title_text = "Click to add title"
        st.session_state.left_content_text = "Click to add text on left"
        st.session_state.right_content_text = "Click to add text on right"
        st.session_state.left_image_data = None
        st.session_state.right_image_data = None
        st.session_state.csv_data = None
        st.session_state.slide_index = st.session_state.get('slide_index', 0) + 1

    if 'title_text' not in st.session_state:
        st.session_state.slide_index = 1
        reset_state()

    with st.sidebar:
        st.header("Controls")
        st.session_state.title_text = st.text_input("Enter Title Text", st.session_state.title_text)
        st.session_state.left_content_text = st.text_area("Enter Left Content Text", st.session_state.left_content_text)

        media_type = st.radio("Choose the media type for right panel:", ("Image", "Graph"))

        if media_type == "Image":
            uploaded_right_file = st.file_uploader("Upload Right Image", type=['png', 'jpg', 'jpeg'], key=f"right-{st.session_state.slide_index}")
            if uploaded_right_file:
                st.session_state.right_image_data = Image.open(uploaded_right_file)

        elif media_type == "Graph":
            uploaded_csv_file = st.file_uploader("Upload CSV for Graph", type=['csv'], key=f"csv-{st.session_state.slide_index}")
            if uploaded_csv_file:
                df = pd.read_csv(uploaded_csv_file)
                st.session_state.csv_data = df  # Store dataframe in session

        if st.button("New Slide"):
            reset_state()

        if st.button("Save"):
            slides_data = []
            if os.path.exists("presentation_data.json"):
                with open("presentation_data.json", "r") as file:
                    slides_data = json.load(file)
            new_slide_data = {
                f"Slide {st.session_state.slide_index}": {
                    "title": st.session_state.title_text,
                    "left_content": st.session_state.left_content_text,
                    "right_content": st.session_state.right_content_text
                }
            }
            slides_data.append(new_slide_data)
            with open("presentation_data.json", "w") as file:
                json.dump(slides_data, file, indent=4)
            st.success("Slide data saved successfully!")

    st.title(st.session_state.title_text)
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.left_content_text)
        if st.session_state.left_image_data:
            st.image(st.session_state.left_image_data, caption='Uploaded Left Image', use_column_width=True)
    
    with col2:
        if media_type == "Graph" and st.session_state.csv_data is not None:
            st.write("Select the columns to plot:")
            x_axis = st.selectbox('Choose X-axis:', st.session_state.csv_data.columns, index=0)
            y_axis = st.selectbox('Choose Y-axis:', st.session_state.csv_data.columns, index=1 if len(st.session_state.csv_data.columns) > 1 else 0)
            plot_type = st.selectbox('Choose plot type:', ['Line', 'Bar', 'Area'])
            if st.button("Generate Graph"):
                if plot_type == 'Line':
                    st.line_chart(st.session_state.csv_data[[x_axis, y_axis]])
                elif plot_type == 'Bar':
                    st.bar_chart(st.session_state.csv_data[[x_axis, y_axis]])
                elif plot_type == 'Area':
                    st.area_chart(st.session_state.csv_data[[x_axis, y_axis]])
        elif st.session_state.right_image_data:
            st.image(st.session_state.right_image_data, caption='Uploaded Right Image', use_column_width=True)
        else:
            st.write(st.session_state.right_content_text)

if __name__ == "__main__":
    template2()
