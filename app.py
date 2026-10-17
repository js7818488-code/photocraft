import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import io

st.set_page_config(
    page_title="PhotoCraft",
    page_icon="📸",
    layout="wide"
)

st.title("📸 PhotoCraft")
st.subheader("Professional Online Photo Editor")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    brightness = st.slider(
        "Brightness",
        0.5,
        3.0,
        1.0
    )

    contrast = st.slider(
        "Contrast",
        0.5,
        3.0,
        1.0
    )

    blur = st.slider(
        "Blur",
        0,
        10,
        0
    )

    grayscale = st.checkbox(
        "Convert to Grayscale"
    )

    edited = image.copy()

    edited = ImageEnhance.Brightness(
        edited
    ).enhance(brightness)

    edited = ImageEnhance.Contrast(
        edited
    ).enhance(contrast)

    if blur > 0:
        edited = edited.filter(
            ImageFilter.GaussianBlur(radius=blur)
        )

    if grayscale:
        edited = edited.convert("L")

    with col1:
        st.image(
            image,
            caption="Original Image"
        )

    with col2:
        st.image(
            edited,
            caption="Edited Image"
        )

    buffer = io.BytesIO()
    edited.save(buffer, format="PNG")

    st.download_button(
        "⬇ Download Edited Image",
        data=buffer.getvalue(),
        file_name="edited_image.png",
        mime="image/png"
    )