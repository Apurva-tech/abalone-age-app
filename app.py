import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('final_model.pkl','rb'))



st.set_page_config(
    page_title="Prediction App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

from PIL import Image
image = Image.open('banner.jpeg')

st.image(image,
      use_column_width=True)


def predict_age(Length,Diameter,Height,Whole_weight,Shucked_weight,Viscera_weight,Shell_weight):
    input=np.array([[Length,Diameter,Height,Whole_weight,Shucked_weight,Viscera_weight,Shell_weight]]).astype(np.float64)
    prediction = model.predict(input)
    #pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return int(prediction)


def main():
    #st.title("Abalone Age Prediction")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Abalone Age Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    Length = st.text_input("Length")
    Diameter = st.text_input("Diameter")
    Height = st.text_input("Height")
    Whole_weight = st.text_input("Whole weight")
    Shucked_weight = st.text_input("Shucked weight")
    Viscera_weight = st.text_input("Viscera weight")
    Shell_weight = st.text_input("Shell weight")

    safe_html ="""  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> The Abalone is young</h2>
      </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> The Abalone is middle aged</h2>
      </div>
    """
    danger_html="""  
      <div style="background-color:#F08080; padding:10px >
       <h2 style="color:black ;text-align:center;"> The Abalone is old</h2>
       </div>
    """

    if st.button("Predict the age"):
        output = predict_age(Length,Diameter,Height,Whole_weight,Shucked_weight,Viscera_weight,Shell_weight)
        st.success('The age is {}'.format(output))

        if output == 1:
            st.markdown(safe_html,unsafe_allow_html=True)
        elif output == 2:
            st.markdown(warn_html,unsafe_allow_html=True)
        elif output == 3:
            st.markdown(danger_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
