import streamlit as st
import pandas as pd
import numpy as np

st.title("My Streamlit App")
st.write("Hello, world!")
st.text("Text Viewer")
# st.line_chart([1, 2, 3, 4, 6])

# @st.cache_data

# st.on_click("Click me!")

st.button("Click me!")

# Write Method
# df = pd.DataFrame({
#     "Column 1": [1, 2, 3, 4, 5],
#     "Column 2": [10, 20, 30, 40, 50],
# })

# df

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# st.dataframe(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }), width=1000)

# st.table(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# dataframe  = np.random.randn(10, 10)
# # st.dataframe(dataframe, width=1000, height=500)
# st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
# st.table(dataframe)