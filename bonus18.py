    # Creamos una pequeña aplicación web para sacar una foto con la webcam y que la convierta a blanco y negro.
    # Creamos en el mismo programa la opción de poder subir la foto desde el ordenador y después la convertimos a blanco y negro.

import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")  # Para poner el título al programa web, en la web.

    # Creamos un componente del programa para subir una imagen desde el ordenador:
uploaded_image = st.file_uploader("Upload Image")

with st.expander('Start Camera.'):  # con este comando añadimos el botón para que abra la cámara cuando nosotros estemos preparados.
        # Abrimos la cámara con el comando que streamlit tiene por defecto:
    camera_image = st.camera_input('Camera')

if camera_image:  # con este condicional nos aseguramos primero que haya una foto tomada y luego se ejecute el código de abajo.
        # Creamos una instancia de la imagen con pillow:
    img = Image.open(camera_image)

        # Convertimos esas imagen de pillow a blanco y negro
    gray_img = img.convert('L')

        # Mostramos esa imagen en la aplicación en modo blanco y negro.
    st.image(gray_img)


    # Con este código convertimos la imagen subido desde el ordenador a blanco y negro:
if uploaded_image:  # nos aseguramos que primero hayamos subido la foto desde el ordenador y luego se ejecuta el código de abajo:

    # Creamos una instancia de la imagen con pillow:
    img = Image.open(uploaded_image)

    # Convertimos esas imagen de pillow a blanco y negro
    gray_uploaded_img = img.convert('L')

    # Mostramos esa imagen en la aplicación en modo blanco y negro.
    st.image(gray_uploaded_img)