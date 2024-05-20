import streamlit as st
import streamlit.components.v1 as components
import time

def live_typing_effect(text, speed=100):
    """Simulate live typing effect in Streamlit."""
    typing_script = f"""
    <html>
    <body>
    <div id="typing"></div>
    <script type="text/javascript">
        var i = 0;
        var text = "{text}";
        var speed = {speed}; // Speed in milliseconds

        function typeWriter() {{
            if (i < text.length) {{
                document.getElementById("typing").innerHTML += text.charAt(i);
                i++;
                setTimeout(typeWriter, speed);
            }}
        }}
        typeWriter();
    </script>
    </body>
    </html>
    """
    components.html(typing_script, height=100)

def main():
    st.title("Simulated Live Typing in Streamlit")
    input_text = st.text_area("Enter text to simulate typing:")
    typing_speed = st.slider("Select typing speed in milliseconds:", min_value=50, max_value=200, value=100)
    if st.button("Simulate Typing"):
        live_typing_effect(input_text, typing_speed)

if __name__ == '__main__':
    main()
