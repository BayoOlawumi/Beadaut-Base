import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, LabelEncoder
from sklearn.cluster import KMeans
import seaborn as sns



st.title('Unsupervised Learning Techniques')
st.subheader(
    """
        **Clustering Method**

""")

selected_technique = st.sidebar.selectbox(
    'Clustering Result',
    ('K-Means', 'Hierarchical', 'DBSCAN')
)

'You selected: ', selected_technique

df = pd.read_csv("processed_mv.csv")
#numeric data

if selected_technique == 'K-Means':
    my_numeric_df = df.select_dtypes(exclude ='object') # obtains the numerical data type

    st.dataframe(my_numeric_df)

    ad_dummies = pd.get_dummies(my_numeric_df.adult)
    my_numeric_df = pd.concat([my_numeric_df, ad_dummies], axis=1)
    my_numeric_df.drop(['id', 'adult'], axis=1, inplace=True)


    # Prepare function that will preprocess additional features
    normalize = MinMaxScaler()
  
    extracted_features = normalize.fit_transform(my_numeric_df.values)

    #Create and train (fit) the model

    model = KMeans(n_clusters=4, random_state=42)
    model = model.fit(extracted_features)

    df['grp'] = model.labels_ + 1

    
    st.scatter_chart(data=df, x='runtime', y='vote_average', color='grp')

else:
    st.write(f"We do not have {selected_technique} in our system yet")