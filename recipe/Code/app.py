"""Importing the required libraries"""
import streamlit as st
from map import find_recipe #pylint: disable=import-error

def generate(): #pylint: disable=inconsistent-return-statements
    """Function that creates the layout of the generated recipe"""

    st.markdown("""
    <style>.big-font1 {font-size:50px !important;}
    </style>""",
    unsafe_allow_html=True)

    st.markdown("""<p class="big-font1";
    style="font-family:verdana"><b>Recipe Generator</b></p>""",
    unsafe_allow_html=True)

    ingredients = st.text_input(label = "Enter the Ingredients")
    generate_button = st.button('Generate Recipe')
    if generate_button:
        generate_button = False
        recipe = find_recipe(str(ingredients))

        title = recipe["title"]
        image = recipe["image"]
        ingredients = recipe["ingredients"]
        instructions = recipe["instructions_list"]

        html_str = f"""
        <style>
        p.a {{
        font: bold {30}px Verdana;
        text-align: center
        }}
        </style>
        <p class="a">{title}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1,2,1])

        with col1:
            st.write("")

        with col2:
            st.image(image, width = 350)

        with col3:
            st.write("")

        st.markdown("""
        <style>
        .headers {
        font-size:30px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown("""<p class="headers"; style="font-family:verdana"><b>Ingredients</b></p>""",
                    unsafe_allow_html=True)
        for i in ingredients:
            st.write(i + '\n\n')

        st.markdown("""
        <style>
        .headers {
        font-size:30px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown("""<p class="headers"; style="font-family:verdana"><b>Instructions</b></p>""",
                    unsafe_allow_html=True)
        for i in instructions:
            st.write(i + '\n\n')

        if st.button('Regenerate Recipe'):
            return generate()

def main():
    """Function that calls the generate function"""
    generate()

if __name__ == '__main__':
    main()
