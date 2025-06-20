import streamlit as st
import pandas as pd
from preprocessing import preprocess_data
from visualization import show_visualizations

st.set_page_config(page_title="데이터 분석 대시보드", layout="wide")
st.title("데이터 분석 대시보드")

# 1. 데이터셋 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("데이터 미리보기")
    st.dataframe(df.head())
    st.write(f"행 개수: {df.shape[0]}, 열 개수: {df.shape[1]}")

    # 2. 전처리
    st.subheader("데이터 전처리")
    with st.expander("전처리 옵션 및 결과 보기", expanded=True):
        df_processed = preprocess_data(df)
        st.write("전처리 결과 미리보기:")
        st.dataframe(df_processed.head())
        st.write(f"전처리 후 행 개수: {df_processed.shape[0]}, 열 개수: {df_processed.shape[1]}")
        st.write("전처리 과정: 결측치는 수치형은 평균, 범주형은 최빈값으로 대체됩니다.")

    # 3. 시각화
    st.subheader("데이터 시각화")
    viz_options = ["히스토그램", "상관관계 히트맵"]
    selected_viz = st.multiselect("원하는 시각화 종류를 선택하세요", viz_options, default=viz_options)
    show_visualizations(df_processed, selected_viz)

    # 4. 결과 다운로드
    csv = df_processed.to_csv(index=False).encode('utf-8-sig')
    st.download_button("전처리된 데이터 다운로드", data=csv, file_name="processed_data.csv", mime="text/csv")
else:
    st.info("왼쪽에서 CSV 파일을 업로드하세요.")
