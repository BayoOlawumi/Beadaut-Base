import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.markdown("## What do we have here ?")
st.sidebar.markdown("- Movie Recommender Application")
st.sidebar.markdown("- Vote Average by Year")
st.sidebar.markdown("- Search Engine")

df = pd.read_csv("processed_mv.csv")
# Display almost anything
st.title('Horror Movies Analytics Application ')

st.subheader(
    """
        **Analysed it yourself!**

""")

# st.dataframe() method to draw an interactive table.
st.dataframe(df.head())
st.divider()

st.markdown("#### Data Overview")
st.dataframe(df.describe())
st.divider()

# Interesting Widgets
# st.slider(), st.button(), st.selectbox(), st.text_input, st.checkbox()

c = st.container()
c.markdown("## Movie Recommender Application")
c.subheader("Select Favorite Language")

# st.selectbox()
choice = c.selectbox("Pick One", list(df['original_language'].unique()))

c.markdown("**Recommended Movies**")

c.dataframe(df[df["original_language"] == choice].sort_values(by=['popularity'], ascending=False)[["title",'popularity']])


st.markdown("## Check Vote Average by Year")

# st.slider()
year_to_filter = st.slider('year', 2000, 2025, 2000)
filtered_data = df[df['year'] == year_to_filter]
st.markdown(f"{year_to_filter}")
st.dataframe(filtered_data)

# add a line chart to your app with st.line_chart(). 
st.line_chart(data = filtered_data, y = 'vote_average', color='popularity_rank')



st.subheader("Search Movie")
st.text_input("Put Movie Name", key="movie")
# You can access the value at any point with:
if st.session_state.movie:
    obtained = df[df['title'] == st.session_state.movie]
    if obtained.empty:
        st.write(f"We do not have {st.session_state.movie} in our database")
    else:
        st.table(obtained)
        



#  python -m streamlit run main_page.py

# pip install scikit-learn

# pip install seaborn