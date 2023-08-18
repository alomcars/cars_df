import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(car_df):
    st.header('Visualise data')

    st.set_option('deprecation.showPyplotGlobalUse', False)


    st.subheader("Scatter plot")

    features_list = st.multiselect("Select the x-axis values:",

    for feature in features_list:
        st.subheader(f"Scatter plot between {feature} and price")
        plt.figure(figsize = (12, 6))
        sns.scatterplot(x = feature, y = 'price', data = car_df)
        st.pyplot()


    st.subheader("Visualisation Selector")


    plot_types = st.multiselect("Select charts or plots:", ('Histogram', 'Box Plot', 'Correlation Heatmap'))


    if 'Histogram' in plot_types:
        st.subheader("Histogram")
        columns = st.selectbox("Select the column to create its histogram",
                                      ('carwidth', 'enginesize', 'horsepower'))
        plt.figure(figsize = (12, 6))
        plt.title(f"Histogram for {columns}")
        plt.hist(car_df[columns], bins = 'sturges', edgecolor = 'black')
        st.pyplot()


    if 'Box Plot' in plot_types:
        st.subheader("Box Plot")
        columns = st.selectbox("Select the column to create its box plot",
                                      ('carwidth', 'enginesize', 'horsepower'))
        plt.figure(figsize = (12, 2))
        plt.title(f"Box plot for {columns}")
        sns.boxplot(car_df[columns])
        st.pyplot()

    if 'Correlation Heatmap' in plot_types:
        st.subheader("Correlation Heatmap")
        plt.figure(figsize = (8, 5))
        ax = sns.heatmap(car_df.corr(), annot = True) 
        bottom, top = ax.get_ylim() 
        ax.set_ylim(bottom + 0.5, top - 0.5) 
        st.pyplot()