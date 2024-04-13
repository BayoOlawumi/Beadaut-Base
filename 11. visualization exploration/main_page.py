import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.markdown("# Analytics ❄️")

df = pd.read_csv("processed_mv.csv")
# Display almost anything
st.title('Horror Movies Analytics Application ❄️')

st.subheader(
    """
        **Analysed it yourself!**

""")

st.dataframe(df.head())
st.divider()

st.markdown("#### Data Overview")
st.dataframe(df.describe())
st.divider()

c = st.container()
c.markdown("## Movie Recommender Application")
c.subheader("Select Favorite Language")
choice = c.selectbox("Pick One", list(df['original_language'].unique()))

c.markdown("**Recommended Movies**")
c.dataframe(df[df["original_language"] == choice].sort_values(by=['popularity'], ascending=False)[["title",'popularity']])


st.markdown("## Check Vote Average by Year")
year_to_filter = st.slider('year', 2000, 2025, 2000)
filtered_data = df[df['year'] == year_to_filter]
st.markdown(f"{year_to_filter}")
st.dataframe(filtered_data)
st.line_chart(data = filtered_data, y = 'vote_average', color='popularity_rank')

st.subheader("Search Movie")
st.text_input("Put Movie Name", key="movie")
# You can access the value at any point with:
if st.session_state.movie:
    st.table(df[df['title'] == st.session_state.movie])


#  python -m streamlit run main_page.py