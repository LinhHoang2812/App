import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.header("Explore your data here")
st.text("Upload your CSV file here")
uploaded_file = st.file_uploader("Choose a file",type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)


    st.subheader("A quick look at your data")

    plot_type = st.radio("Choose a type of graph",("boxplot","count","scatter",))

    if plot_type == "boxplot":
        x = st.text_input("What categorical variable you want to explore?",placeholder="Any categorical from your data")
        y= st.text_input("What numeric variable you want to explore?",placeholder="any numeric variable from your data")
        if y and x is not None:
            fig= plt.figure()
            sns.boxplot(data=df,x=x,y=y)
            st.pyplot(fig)
    elif plot_type == "count":
        x= st.text_input("What variable you want to count per category?",placeholder="Any categorical from your data")
        if x is not None:
            fig= plt.figure()
            sns.countplot(data=df,x=x)
            st.pyplot(fig)

    else:
        x = st.text_input("What feature x you want to explore?")
        y = st.text_input("What feature y you want to explore?")
        if y and x is not None:
            fig= plt.figure(figsize=(20,10))
            sns.scatterplot(data=df,x=x,y=y)
            st.pyplot(fig)
        