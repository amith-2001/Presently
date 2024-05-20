import streamlit as st
import json
from typing_live import live_typing_effect
from streamlit_lottie import st_lottie
def load_lottiefile(filepath: str):
    """ Load a Lottie animation from a JSON file located at filepath """
    with open(filepath, 'r') as file:
        return json.load(file)


if __name__ == '__main__':
    # Initialize the session state for page navigation if not already set
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'

    if st.session_state['page'] == 'home':
        st.title(
            "Welcome! Let's generate Interactive Viz from your data! 🚀")
        lottie_animation_path = "Animation - 1716175109588.json"
        lottie_animation = load_lottiefile(lottie_animation_path)
        st_lottie(lottie_animation, height=250, width=600, key="example")
        live_typing_effect("Hello, I'm your AI Flowchart Generator! 🚀 Just send over your code or GitHub repository, and I'll transform it into a sleek, easy-to-understand flow diagram. Let's streamline your work and make your projects visually engaging!", speed=25)
        col1, col2 = st.columns(2)

        with col1:
            if st.button('Generate from GitHub Repo'):
                st.session_state['page'] = 'github_repo'
                st.experimental_rerun()

        with col2:
            if st.button('Generate from Code'):
                st.session_state['page'] = 'code'
                st.experimental_rerun()
