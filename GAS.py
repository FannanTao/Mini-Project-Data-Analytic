import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

#gap size
st.markdown("""
<style>
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 2rem;
    padding-right: 2rem;
}
</style>
""", unsafe_allow_html=True)

#background
st.markdown("""
<style>
.stApp {
    background-color: #F4E7FE;
}
</style>
""", unsafe_allow_html=True)

#sidebar colour
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #E0BBFC;
}
</style>
""", unsafe_allow_html=True)

#font
st.markdown("""
<style>
/* Apply font ONLY to text, NOT icons */
html, body, [class*="css"] {
    font-family: "Trebuchet MS",!important;
}

/* Keep icons untouched (fix broken arrows) */
svg, i, [data-testid="stSidebarNav"] * {
    font-family: inherit !important;
}
</style>
""", unsafe_allow_html=True)



data = pd.read_csv('Gaming_Academic_Performance.csv')

#title
st.markdown("""
<h2 style='margin-bottom:0px;'>
🎮 Gaming and Academic Performance
</h2>
""", unsafe_allow_html=True)
st.set_page_config(layout="wide")

# Create columns (wide layout)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", 8000)

with col2:
    avg1 =  data['Study Hours'].mean()
    st.metric("Average Study Hours", round(avg1, 2))

with col3:
    avg2 = data['Gaming Hours'].mean()
    st.metric('Average Gaming Hours', round(avg2, 3))

st.divider()

# Another wide layout
left, right = st.columns(2)

#sidebar option
st.sidebar.title('📊About Dataset')
st.sidebar.markdown('-Moderate gaming can slightly improve cognitive performance.')
st.sidebar.markdown('-Excessive gaming negatively impacts grades')
st.sidebar.markdown('-Study hours, sleep, and attendance strongly influence outcomes')

#plot  data
with left:
    #option 1
    x_option = st.selectbox(
        "Choose x-axis column:",
        data.columns,
        key='x'
        )

    y_option = st.selectbox(
        "Choose y-axis column:",
        data.columns,
        key='y'
        )

    #scatter
    fig, ax = plt.subplots(figsize = (4,3))
    fig.patch.set_facecolor('#F4E7FE')
    ax.scatter(data[x_option], data[y_option])

    ax.set_xlabel(x_option)
    ax.set_ylabel(y_option)
    ax.set_title(f' {y_option} vs {x_option}')

    st.pyplot(fig)

with right:
    #option 2
    col_option = st.selectbox(
        "Choose a column:",
        data.columns,
        key='c'
        )

    #line chart
    fig, ax = plt.subplots(figsize = (2,1))
    plt.tight_layout()
    fig.patch.set_facecolor('#F4E7FE')
    st.line_chart(data[col_option])

    ax.set_xlabel(x_option)
    ax.set_ylabel(y_option)
    ax.set_title(f' {y_option} vs {x_option}')

    #histogram
    fig, ax = plt.subplots(figsize = (4,2))
    fig.patch.set_facecolor('#F4E7FE')
    ax.hist(data[col_option], bins=10)
    st.pyplot(fig)