import streamlit as st
import numpy as np
import plotly.figure_factory as ff


st.header("Twój Eko Kącik")

slider = st.slider("Czas")

col1, col2 = st.columns(2)
with col1:
    st.write("Toe będzie kolumna pierwsza")

    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])
    st.plotly_chart(fig, use_container_width=True)


with col2:
    st.write("To będzie kolumna druga")
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])
    st.plotly_chart(fig, use_container_width=True)


with st.container():
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    metric_col1.metric("Cena", 212)
    metric_col2.metric("Emisja $CO_2$", 1203, delta=21)
    metric_col3.metric("Top %", slider)