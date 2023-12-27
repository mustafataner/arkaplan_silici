
import streamlit as st
from rembg import remove
import numpy as np
from PIL import Image
import io



st.title('Arka Plan Kaldırma Uygulaması')

uploaded_file = st.file_uploader("Bir fotoğraf yükleyin", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Yüklenen fotoğraf.', use_column_width=True)

    if st.button('Arka Planı Kaldır'):
        input_img = np.array(image)
        output = remove(input_img)
        output_image = Image.fromarray(output)

        st.image(output_image, caption='Arka planı kaldırılmış fotoğraf.', use_column_width=True)

        buf = io.BytesIO()
        output_image.save(buf, format='PNG')
        buf.seek(0)
        btn = st.download_button(
            label="Fotoğrafı İndir",
            data=buf,
            file_name='output.png',
            mime='image/png')

