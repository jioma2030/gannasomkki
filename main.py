
import gdown
import pandas as pd
import plotly.express as px
import streamlit as st

# Google Drive에서 데이터 다운로드
def download_data():
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    output = "data.csv"  # 로컬에 저장될 파일명
    gdown.download(url, output, quiet=False)
    return output

# 데이터 로드 및 시각화
def load_and_visualize_data():
    # 데이터 다운로드
    data_file = download_data()
    
    # 데이터 읽기
    data = pd.read_csv(data_file)
    
    # 데이터프레임 확인
    st.write("### 데이터 미리보기")
    st.write(data.head())

    # 데이터 컬럼 이름 확인 (여기서 x_column, y_column 변경 필요)
    st.write("### 데이터 컬럼 이름")
    st.write(data.columns)

    # 시각화 (x, y 컬럼은 실제 데이터에 맞게 변경)
    fig = px.scatter(data_frame=data, x='x_column', y='y_column', title='Scatter Plot Example')

    # Plotly 그래프를 Streamlit에 표시
    st.plotly_chart(fig)

# Streamlit 앱 실행
def main():
    st.title("Plotly와 Streamlit을 활용한 데이터 시각화 웹앱")

    # 데이터 로드 및 시각화 실행
    load_and_visualize_data()

if __name__ == "__main__":
    main()
