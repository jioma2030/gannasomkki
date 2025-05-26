import streamlit as st
import pandas as pd
import plotly.express as px

# Google Drive에서 CSV 다운로드 링크
CSV_URL = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

# 데이터 로딩 함수
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(CSV_URL)
        return df
    except Exception as e:
        st.error(f"데이터 로딩 실패: {e}")
        return pd.DataFrame()

# 앱 제목
st.title("📊 Google Drive CSV 시각화 앱")

# 데이터 불러오기
df = load_data()

# 데이터가 존재할 경우
if not df.empty:
    st.subheader("데이터 미리보기")
    st.dataframe(df)

    # 숫자형 컬럼 선택
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if len(numeric_cols) >= 2:
        x_axis = st.selectbox("X축 선택", numeric_cols)
        y_axis = st.selectbox("Y축 선택", numeric_cols, index=1)

        # Plotly 시각화
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
        st.plotly_chart(fig)
    else:
        st.warning("시각화할 숫자형 컬럼이 충분하지 않습니다.")
else:
    st.error("데이터를 불러올 수 없습니다. 링크를 확인하세요.")
