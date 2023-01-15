import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px


st.header("Twój Eko Kącik")

with st.sidebar:
    slider = st.slider("Dzień", min_value=1, max_value=500, value=100, step=1)

## Dataset
d = pd.read_pickle("Notebooks/dataset.pickle")
cols = ['DE_KN_residential3_circulation_pump', 'DE_KN_residential3_dishwasher',
       'DE_KN_residential3_freezer',
       'DE_KN_residential3_refrigerator', 'DE_KN_residential3_washing_machine']
cols_pred = [
    'DE_KN_residential3_circulation_pump_pred',
       'DE_KN_residential3_dishwasher_pred', 'DE_KN_residential3_freezer_pred',
       'DE_KN_residential3_refrigerator_pred',
       'DE_KN_residential3_washing_machine_pred'
        ]
d_prep = d.drop(columns=['energy_consumption', 'start', 'end', 'step', 'cstep']).resample("D").sum()

color_discrete_map={'Pompa cyrkulacyjna':'red',
                                 'Zmywarka':'cyan',
                                 'Zamrażarka':'yellow',
                                 'Lodówka':'darkblue',
                                   'Pralka':'green'}

def piechart(i, pred):
    if pred:
        data = d_prep[cols_pred].iloc[i]
        fig = px.pie(pd.DataFrame({"names": ['Pompa cyrkulacyjna', 'Zmywarka', 'Zamrażarka', 'Lodówka', 'Pralka'], "values": data.values}), values='values', names='names', color_discrete_map=color_discrete_map)
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        return fig
    else:
        data = d_prep[cols].iloc[i]
        fig = px.pie(pd.DataFrame({"names": ['Pompa cyrkulacyjna', 'Zmywarka', 'Zamrażarka', 'Lodówka', 'Pralka'], "values": data.values}), values='values', names='names',color_discrete_map=color_discrete_map)
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        return fig

def barplot(i, pred):
    if pred:
        data = d_prep[cols_pred].iloc[i]
        fig = px.bar(pd.DataFrame({"names": ['Pompa cyrkulacyjna', 'Zmywarka', 'Zamrażarka', 'Lodówka', 'Pralka'], "values": data.values}), x='values', y='names', title="Zużycie energi w [kWh]", labels={'values':'Energia w kWh', 'names': "Urządzenie"})
        return fig
    else:
        data = d_prep[cols].iloc[i]
        fig = px.bar(pd.DataFrame({"names": ['Pompa cyrkulacyjna', 'Zmywarka', 'Zamrażarka', 'Lodówka', 'Pralka'], "values": data.values}), x='values', y='names', title="Zużycie energi w [kWh]", labels={'values':'Energia w kWh', 'names': "Urządzenie"})
        return fig

col1, col2 = st.columns(2)
with col1:
    st.write("Dane rzeczywiste")

    piechart_true = piechart(slider, False) 
    barplot_true = barplot(slider, False)
    st.plotly_chart(piechart_true, use_container_width=True, theme=None)
    st.plotly_chart(barplot_true, use_container_width=True)


with col2:
    st.write("Dane przewidywane przez AI")

    piechart_pred = piechart(slider, True) 
    barplot_pred = barplot(slider, True)
    st.plotly_chart(piechart_pred, use_container_width=True, theme=None)
    st.plotly_chart(barplot_pred, use_container_width=True)


with st.container():
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    metric_col1.metric("Cena", d_prep[cols_pred].iloc[slider].sum() * 1)
    metric_col2.metric("Emisja $CO_2$ [g]", d_prep[cols_pred].iloc[slider].sum() * 801, 
                       delta=(d_prep[cols_pred].iloc[slider-1].sum() -d_prep[cols_pred].iloc[slider].sum())*801)
    metric_col3.metric("Top %", 30)