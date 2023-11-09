import streamlit as st
import numpy as np
from download_model import file_exists, download_file
from tensorflow.keras.models import load_model
from PIL import Image

def Animal_app():
    st.header("Animal Wildlife - Prediction")
    st.write('https://www.kaggle.com/datasets/biancaferreira/african-wildlife')
    st.markdown('---')
    st.write('#### Why is it important to predict the image of an African wild animal?')
    st.write('Predicting the image of an African wild animal is important for wildlife conservation, ecological research, and education. It helps in monitoring and protecting endangered species, understanding ecosystems, and raising awareness about African wildlife.')


    file_path = 'afric_model_tf.h5'
    file_url = 'https://lermaserver.com/evelyn/file.php'
    if not file_exists(file_path):
        st.warning('File does not exist. Downloading...')
        download_file(file_url, file_path)
        st.success('File downloaded.')

    data_afric = load_model(file_path)

    # Agregar la opción para que el usuario cargue una imagen
    uploaded_image = st.file_uploader("Submit Image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Mostrar la imagen cargada
        image = Image.open(uploaded_image)
        st.image(image, caption='Image loaded', use_column_width=True)

        # Redimensionar la imagen a 128x128 píxeles
        resized_image = image.resize((128, 128))
        #st.image(resized_image, caption='Imagen redimensionada', use_column_width=True)

        image_array = np.array(resized_image)
        image_array = image_array / 255.0  # Normaliza los valores de píxeles (si es necesario)
        image_array = np.expand_dims(image_array, axis=0)  # Agrega una dimensión para la muestra

        if st.button("Predict"):  # Botón de predicción
            prediction_afric = data_afric.predict(image_array)
            probability_class = [(i, value) for i, value in enumerate(prediction_afric[0])] # Obtén el valor de la predicción como un escalar
            predicted_class = max(probability_class, key=lambda x: x[1])

            # Descripciones de los animales
            animal_descriptions = {
                0: 'Buffalo - The African buffalo, also known as the Cape buffalo, is a large, powerful herbivore with distinctive curved horns.',
                1: 'Elephant - African elephants are the world\'s largest land animals, known for their large ears and long tusks.',
                2: 'Rhino - African rhinoceroses are known for their thick skin and two species, the white rhino and the black rhino.',
                3: 'Zebra - Zebras are characterized by their black and white stripes and are a common sight in African savannas.'
            }
            
            #if isinstance(predicted_class, np.ndarray) and predicted_class.size == 1:
                #predicted_class = predicted_class.item()  # Convierte a un valor escalar
        
            st.write('Descripción:', animal_descriptions.get(predicted_class[0], 'Unknown Animal'), ' with a probability of ', round(predicted_class[1] * 100, 2) , '%')




           

