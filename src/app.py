import streamlit as st
from PIL import Image

from utils import run_ocr, correct_text

st.set_page_config(layout="wide")
st.title("OCR and Vietnamese Error Correction")

# Logic trạng thái hiển thị
if "ocr_text" not in st.session_state:
    st.session_state.ocr_text = ""

if "corrected_text" not in st.session_state:
    st.session_state.corrected_text = ""

"""
Chia giao diện thành 2 bên:
1. Bên trái: Phần upload ảnh văn bản
2. Bên phải: Hiển thị kết quả
"""
col1, col2 = st.columns(2)

# Đây là phần cho phép upload ảnh văn bản (Cột bên trái)
with col1:
    uploaded_file = st.file_uploader(
        "Upload image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Input Image", use_container_width=True)

    run_btn = st.button("Chuyển thành văn bản")

# Xử lý logic chạy
if uploaded_file and run_btn:
    with st.spinner("Đang trích xuất và xử lý văn bản..."):
        st.session_state.ocr_text = run_ocr(image)
        st.session_state.corrected_text = correct_text(
            st.session_state.ocr_text
        )

# Phần hiển thị kết quả
with col2:
    st.subheader("Văn bản được trích xuất")
    st.text_area(
        label="",
        value=st.session_state.ocr_text,
        height=200,
        placeholder="Kết quả chuyển từ ảnh được hiển thị tại đây..."
    )

    st.subheader("Văn bản sau khi xử lý")
    st.text_area(
        label="",
        value=st.session_state.corrected_text,
        height=200,
        placeholder="Văn bản sau khi xử lý được hiển thị tại đây..."
    )