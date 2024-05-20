import streamlit as st
import json
from typing_live import live_typing_effect
from streamlit_lottie import st_lottie
import os
def load_lottiefile(filepath: str):
    """ Load a Lottie animation from a JSON file located at filepath """
    with open(filepath, 'r') as file:
        return json.load(file)


def template_selection():
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
            st.experimental_rerun()

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
            st.experimental_rerun()
    print('tempelate pafe')
    pass


if __name__ == '__main__':
    # Initialize the session state for page navigation if not already set
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'

    if st.session_state['page'] == "temp_page":
        template_selection()

    if st.session_state['page'] == 'home':
        st.title(
            "Welcome! Let's generate Interactive Viz from your data! 🚀")
        lottie_animation_path = "Animation - 1716175109588.json"
        lottie_animation = load_lottiefile(lottie_animation_path)
        st_lottie(lottie_animation, height=250, width=600, key="example")
        live_typing_effect("Hello, I'm your AI Flowchart Generator! 🚀 Just send over your code or GitHub repository, and I'll transform it into a sleek, easy-to-understand flow diagram. Let's streamline your work and make your projects visually engaging!", speed=25)
        col1, col2 = st.columns(2)

        # with col1:
        #     if st.button('Generate from GitHub Repo'):
        #         st.session_state['page'] = 'github_repo'
        #         st.experimental_rerun()

        with col2:
            if st.button('Generate from Code'):
                st.session_state['page'] = 'temp_page'
                st.experimental_rerun()

