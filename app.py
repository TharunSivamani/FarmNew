import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings


res = {
            'rice':{
                'pic':'🌾'
                },
            'maize':{
                'pic':'🌽',
                },
            'chickpea':{
                'pic':'🧆',
                },
            'kidneybeans':{
                'pic':'🫘',
                },
            'pigeonpeas':{
                'pic':'🌱',
                },
            'mothbeans':{
                'pic':'🫘',
                },
            'mungbean':{
                'pic':'🫘',
                },
            'blackgram':{
                'pic':'🫘',
                },
            'lentil':{
                'pic':'🥬',
                },
            'pomegranate':{
                'pic':'🔴',
                },
            'banana':{
                'pic':'🍌',
                },
            'mango':{
                'pic':'🥭',
                },
            'grapes':{
                'pic':'🍇',
                },
            'watermelon':{
                'pic':'🍉',
                },
            'muskmelon':{
                'pic':'🍈',
                },
            'apple':{
                'pic':'🍎',
                },
            'orange':{
                'pic':'🍊',
                },
            'papaya':{
                'pic':'',
                },
            'coconut':{
                'pic':'🥥',
                },
            'cotton':{
                'pic':'🐑',
                },
            'jute':{
                'pic':'🧵'
            },
            'coffee':{
                'pic':'☕',
            }
        }


st.set_page_config(page_title="Crop Recommender", page_icon="🍁", layout='centered', initial_sidebar_state="collapsed")

def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:center;">     Farm New  🌾 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    html_temp1 = """
    <div>
    <h1 style="font-size:35px;text-align:center;">     Helping New Farmer's Around the Globe</h1>
    </div>
    """
    st.markdown(html_temp1, unsafe_allow_html=True)

    col1,col2,col3  = st.columns([5,2,5])
    
    with col3: 
        with st.expander(" ⓘ Information", expanded=True):
            st.write("""
            Why Crop Recommendation ?
            
            Crop Recommendation is a web application that suggest / recommend the farmer to which crop to grown his / her field.

            Crop Recommendation Using Machine Learning ?

            Digital Farming and Precision Agriculture allow precise utilization of inputs like seed, water, pesticides, and fertilizers at the right time to the crop for maximizing productivity, quality and yields. By deploying sensors for data collection and mapping fields, farmers can understand their field in a better way conserve the resources being used and reduce adverse effects on the environment. 
            """)
        '''
        ### How does it work ❓ 
        Fill in the Parameters and Wait while our Model predicts the best for you !
        '''

    with col2:
        pass

    with col1:
        st.subheader("👨‍🌾 Find out the most suitable crop to grow in your farm ")
        N = st.number_input("Nitrogen (Eg : 90)", 1,10000)
        P = st.number_input("Phosporus (Eg : 42)", 1,10000)
        K = st.number_input("Potassium (Eg : 43)", 1,10000)
        temp = st.number_input("Temperature (Eg : 20.87)",0.0,100000.0)
        humidity = st.number_input("Humidity in % (Eg : 82.00)", 0.0,100000.0)
        ph = st.number_input("pH (Eg : 6.5)", 0.10,100000.0)
        rainfall = st.number_input("Rainfall in mm (Eg : 202.90)",0.0,100000.0)

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1,-1)



        
        
        if st.button('Predict'):

            loaded_model = load_model('model.pkl')
            prediction = loaded_model.predict(single_pred)
            col1.write('''
		    ## Results 🔍 
		    ''')

            result = prediction.item().title().lower()
            y = res[result]['pic']
            # col1.success(f"{result.title()} {y} is the Crop Predicted by Our Model")
            html_temp2 = f"""
            <div>
            <h1 style="font-size:40px;text-align:left;">{result.title()} - {y}</h1>
            <p style="text-align:right;font-size:20px;">is the crop predicted by our Model</p>
            </div>
            """
            st.markdown(html_temp2, unsafe_allow_html=True)
            


if __name__ == '__main__':
	main()


