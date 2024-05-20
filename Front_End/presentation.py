import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import TextArea, AnnotationBbox


# Function to draw a circle
def draw_circle(ax, center, radius=0.1):
    circle = plt.Circle(center, radius, color='blue', fill=True)
    ax.add_patch(circle)


# Function to draw a triangle
def draw_triangle(ax, center, size=0.1):
    triangle = plt.Polygon([(center[0], center[1] - size / np.sqrt(3)),
                            (center[0] - size / 2, center[1] + size / (2 * np.sqrt(3))),
                            (center[0] + size / 2, center[1] + size / (2 * np.sqrt(3)))], color='green')
    ax.add_patch(triangle)


# Function to draw a square
def draw_square(ax, center, size=0.1):
    square = plt.Rectangle((center[0] - size / 2, center[1] - size / 2), size, size, color='red')
    ax.add_patch(square)


# Function to add text
def add_text(ax, text, position):
    text_area = TextArea(text, textprops=dict(color="black", size=12))
    ab = AnnotationBbox(text_area, position, xybox=(0, 0), xycoords='axes fraction',
                        boxcoords="offset points", box_alignment=(0.5, 0.5))
    ax.add_artist(ab)


# Main app function
def main():
    st.title('Streamlit Presentation Creator')

    # Session state to track pages and their content
    if 'pages' not in st.session_state:
        st.session_state.pages = [[]]
        st.session_state.current_page = 0

    # Sidebar for adding shapes, text, and images
    with st.sidebar:
        st.write("Add Content")
        content_type = st.radio("Select content type:", ('Shape', 'Text', 'Image', 'Echart'))

        if content_type == 'Shape':
            shape = st.selectbox('Choose a shape:', ['Circle', 'Triangle', 'Square'])
            if st.button('Add Shape'):
                st.session_state.pages[st.session_state.current_page].append(('shape', shape))

        elif content_type == 'Text':
            text = st.text_input("Enter text:")
            if st.button('Add Text'):
                st.session_state.pages[st.session_state.current_page].append(('text', text))

        elif content_type == 'Image':
            image_file = st.file_uploader("Upload an image", type=['jpg', 'png'])
            if st.button('Add Image'):
                st.session_state.pages[st.session_state.current_page].append(('image', image_file))

        elif content_type == 'Echart':
            # Placeholder for Echarts integration
            st.write("Echarts integration coming soon!")

    # Navigation controls
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Previous'):
            if st.session_state.current_page > 0:
                st.session_state.current_page -= 1
    with col2:
        if st.button('Next'):
            if st.session_state.current_page < len(st.session_state.pages) - 1:
                st.session_state.current_page += 1
    with col3:
        if st.button('Add New Page'):
            st.session_state.pages.append([])
            st.session_state.current_page = len(st.session_state.pages) - 1

    # Display current page and its contents
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')  # Turn off the axis

    for content in st.session_state.pages[st.session_state.current_page]:
        content_type, value = content
        if content_type == 'shape':
            if value == 'Circle':
                draw_circle(ax, (0.5, 0.5))
            elif value == 'Triangle':
                draw_triangle(ax, (0.5, 0.5))
            elif value == 'Square':
                draw_square(ax, (0.5, 0.5))
        elif content_type == 'text':
            add_text(ax, value, (0.5, 0.5))
        elif content_type == 'image' and value is not None:
            image = plt.imread(value)
            ax.imshow(image, extent=[0, 1, 0, 1])

    st.pyplot(fig)
    st.write(f"Page {st.session_state.current_page + 1} of {len(st.session_state.pages)}")


if __name__ == '__main__':
    main()
