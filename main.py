import streamlit as st
import pandas as pd
import plotly.express as px

# Google Drive 파일 다운로드 링크
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    return pd.read_csv(url)

df = load_data()

st.title("📊 CSV 데이터 시각화 앱")
st.write("Google Drive에서 데이터를 불러와 Plotly로 시각화합니다.")

st.subheader("데이터 미리보기")
st.dataframe(df)

numeric_cols = df.select_dtypes(include='number').columns.tolist()
if len(numeric_cols) >= 2:
    x_axis = st.selectbox("X축 선택", numeric_cols)
    y_axis = st.selectbox("Y축 선택", numeric_cols, index=1)

    fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    st.plotly_chart(fig)
else:
    st.warning("시각화 가능한 숫자형 컬럼이 부족합니다.")
