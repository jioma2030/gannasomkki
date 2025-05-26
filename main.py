import streamlit as st
import pandas as pd
import plotly.express as px

# Google Drive 파일 다운로드 링크
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

# 데이터 로딩 (Streamlit Cloud 캐싱 사용)
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"데이터를 불러오는 중 오류 발생: {e}")
        return pd.DataFrame()

# 데이터 로드
df = load_data()

st.title("📊 CSV 데이터 시각화 앱")
st.write("Google Drive에서 CSV 데이터를 불러와 Plotly로 시각화합니다.")

# 데이터 미리 보기
if not df.empty:
    st.subheader("데이터 미리보기")
    st.dataframe(df)

    # 숫자형 컬럼 선택
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if len(numeric_cols) >= 2:
        x = st.selectbox("X축 선택", numeric_cols)
        y = st.selectbox("Y축 선택", numeric_cols, index=1)

        fig = px.scatter(df, x=x, y=y, title=f"{x} vs {y}")
        st.plotly_chart(fig)
    else:
        st.warning("시각화 가능한 수치형 컬럼이 충분하지 않습니다.")
else:
    st.warning("데이터를 불러올 수 없습니다. 링크나 파일 형식을 확인하세요.")
