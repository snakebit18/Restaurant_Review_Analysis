import streamlit as st
import numpy as np
import joblib
# loading the saved model
loaded_model = joblib.load(open('C:/Users/ASUS/OneDrive/Desktop/Major/reviews_classifier.sav', 'rb'))


# creating a function for Prediction

def Review_Analysis(input_data):
    # changing the input_data to numpy array
    #input_data_as_numpy_array = np.asarray(input_data)
    input_data=[input_data]
    prediction = loaded_model.predict(input_data)

    if (prediction[0] == 0):
        st.error('NEGATIVE')
    else:
        st.success('POSITIVE')


def main():
    # giving a title
    st.title('Restaurant Review Analysis Web App')

    # getting the input data from the user

    Review = st.text_input('Enter Your Review')



    # creating a button for Prediction

    if st.button('Review Result'):
        Review_Analysis(Review)
        


if __name__ == '__main__':
    main()
