import streamlit as st
import pickle

st.set_page_config(page_title="Text Classification" , page_icon=':flag-pa:',layout='wide')
st.write('')
st.title('☆ Voice Classification ☆')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

###################################################################################################

vect = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def prediction(text):                # takes a string of text as input and returns the prediction
    text_v = vect.transform([text])  #transforms it into a format that the model can understand using the vectorizer
    result = model.predict(text_v)   #makes a prediction with the model, and returns the result

    if result == 1:
        return 'Passive'
    else:
        return 'Active'




st.write('')
st.write('')
st.write('')
st.markdown('#### 💎Text Classification for Active vs. Passive Voice Detection ')


st.write('')
st.write('')
txt = st.text_area('Write Your Sentence')

st.write('')
st.write('')
btn = st.button('Predict') # button to make the prediction

st.write('')

if btn:                        #When this button is clicked, this script calls up the "prediction function" on the text that the user inputted, & displays the result.
    p_result = prediction(txt)
    st.markdown(f'# {p_result}')



st.write('')
st.write('')
st.markdown('<span>All code can be found here <a href="https://github.com/Shriket/Text-Classification-Model-Voice">Text Classification Model</a></span>',unsafe_allow_html=True)
st.markdown('Created By Shriket')
