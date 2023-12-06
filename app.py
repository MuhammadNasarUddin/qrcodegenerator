import streamlit as st
import pyqrcode


def generate_qr_code(link, filename, file_type, scale):
    qr = pyqrcode.create(link)
    if file_type == 'SVG':
        qr.svg(filename, scale=scale)
    elif file_type == 'PNG':
        qr.png(filename, scale=scale)
    return filename


def main():
    st.title('QR Code Generator')

    link = st.text_input('Enter URL:', 'https://example.com')
    file_type = st.radio('Select File Type:', ('SVG', 'PNG'))
    scale = st.slider('Select Scale:', min_value=1, max_value=10, value=6)

    if st.button('Generate QR Code'):
        if link:
            filename = "qrcode." + file_type.lower()
            generated_filename = generate_qr_code(link, filename, file_type, scale)
            st.image(generated_filename)
            st.success(f"QR Code generated as {generated_filename}")


if __name__ == "__main__":
    main()
