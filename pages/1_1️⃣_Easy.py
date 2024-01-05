import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Palmer Penguins Predictor - Easy Mode",
    page_icon="🐧",
)

st.title("🐧 Palmer Penguins Predictor - Easy Mode")

# User input features
with st.container(border=True):
    island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
    gender = st.selectbox('Gender',('male','female'))
    bill_length_mm = st.slider('Bill length (mm)', 32.1,59.6,43.9)
    bill_depth_mm = st.slider('Bill depth (mm)', 13.1,21.5,17.2)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0,231.0,201.0)
    body_mass_g = st.slider('Body mass (g)', 2700.0,6300.0,4207.0)

data = {'island': island,
        'bill_length_mm': bill_length_mm,
        'bill_depth_mm': bill_depth_mm,
        'flipper_length_mm': flipper_length_mm,
        'body_mass_g': body_mass_g,
        'gender': gender}
input_df = pd.DataFrame(data, index=[0])

# Combines user input features with entire penguins dataset
# This will be useful for the encoding phase
penguins_raw = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species'], axis=1)
df = pd.concat([input_df,penguins],axis=0)

# Encoding ordinal features
encode = ['gender','island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1] # Selects only the first row (the user input data)

st.write(df)

