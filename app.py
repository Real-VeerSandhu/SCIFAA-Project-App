import streamlit as st 
import plotly.express as px
import pandas as pd
import base64
from joblib import load


st.set_page_config(page_title="CAN-USA COVID-19 Analysis", page_icon="📈", layout='wide', initial_sidebar_state="collapsed")

st.markdown("""
# Canada v.s. USA COVID-19 Analysis
A data science project bringing forth insight on the fight against the pandemic\n
""")
st.write('----')

final1 = pd.read_csv('Data/linear-graph.csv')
model = load('Models/lin_model1.joblib')
combined = pd.read_csv('Data/out-data.csv')

figW = px.line(combined, x='Date', y='Cases', color='Country', title = "Confirmed Cases in the USA vs Canada")
figW2 = px.line(combined, x='Date', y='Deaths', color='Country', title = "Confirmed Deaths in the USA vs Canada")
fig1 = px.line(combined, x='Date', y='Cases/Population', color='Country', title = "Cases per 100 People in the USA vs Canada", labels={'Cases/Population': 'Cases per 100 People'})
fig2 = px.line(combined, x='Date', y='Diff Cases/Population', color='Country', title = "Increase/Decrease in Cases per 100 People in the USA vs Canada", labels={'Diff Cases/Population': 'Change in Cases per 100 People'})
fig3 = px.line(combined, x='Date', y='Deaths/Cases', color='Country', title = "Deaths per 100 Cases in the USA vs Canada", labels={'Deaths/Cases': 'Deaths per 100 Cases'})
fig4 = px.line(combined, x='Date', y='Tests/Cases', color='Country', title = "Tests per Case in the USA vs Canada", labels={'Tests/Cases': 'Tests per Case'})
rel = px.line(final1, x='Cases', y='Deaths', color='Type', title = 'Cases vs Deaths in Canada (Linear Model vs True Data)')

def main():
    nav = st.selectbox('Navigation', ['Home', 'Analysis Charts', 'Data Modelling'])
    if nav == 'Home':
        st.write('### This interactive app contains all developments as part of the Canada v.s. USA COVID-19 Analysis.')
        st.write('Completed by Veer Sandhu as a Data Science Intern at SCI FAA')
        st.write('*The COVID-19 pandemic has impacted every nation on earth and has been dealt with through countless methods and strategies. Investigating where countries succeeded and where they failed can provide valuable information on resource management, prioritization, planning, and organization. Canada and the U.S may seem similar at first glance, however, they are different economically, socially, and politically. This project compares the two countries regarding how they dealt with the pandemic and which one took the better approach.*')
        with open('Data/final_report.pdf', "rb") as f:
                b64 = base64.b64encode(f.read()).decode('utf-8')        
        a = f'<a href="data:file/csv;base64,{b64}" download="Canada vs USA COVID-19 Analysis Report - Veer Sandhu.pdf">Download the Project Report</a>'
        st.markdown(a, unsafe_allow_html=True)
        st.write("""
        [View the Code Repository](https://github.com/Real-VeerSandhu/SCIFAA-COVID-19-Project)
        """)
    elif nav == 'Analysis Charts':
        col1, col2 = st.beta_columns([1,1])
        with col1:
            st.plotly_chart(figW)
        with col2:
            st.plotly_chart(figW2)

        col3, col4 = st.beta_columns([1,1])
        with col3:
            st.plotly_chart(fig1)
            st.plotly_chart(fig3)
        with col4:
            st.plotly_chart(fig2)
            st.plotly_chart(fig4)
    elif nav == 'Data Modelling':
        st.write('### Models built off Machine Learning and AI')
        col5, col6 = st.beta_columns([2,1])       
        with col5:
            st.plotly_chart(rel)
            
        with col6:
            st.write('Interactive Model (Predicts the Death Count)')
            user_in = st.number_input('Enter the Total Cases', 0, 2000000000)
            user_in = 452638
            if st.button('Run Model'):
                pred = model.predict([[user_in]])
                st.write('Model Prediction (Deaths): ', pred[0][0])
if __name__ ==  '__main__':
    main() 