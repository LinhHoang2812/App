import streamlit as st

st.text("Ciao questo è front end funzione ahashhddkjlfkfkg")

st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown("I am :blue[blue]")
st.header("This is a title")
st.subheader("This is subtitle")

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
#pip install PIL
#from PIL import image

st.button("Click me")

lang = st.radio("What's your favorite language? ",('C++','Python'))

import matplotlib.pyplot as plt
from numpy.random import rand

fig = plt.figure()
plt.scatter([1,2,3,4,5],[1,2,3,4,5])
st.pyplot(fig)

