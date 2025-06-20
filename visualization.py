import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_visualizations(df, selected_viz=None):
    """
    선택된 시각화 종류에 따라 시각화 출력
    """
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if not selected_viz:
        selected_viz = ["히스토그램", "상관관계 히트맵"]
    if "히스토그램" in selected_viz and len(numeric_cols) > 0:
        st.write("### 수치형 컬럼 히스토그램")
        col = st.selectbox("히스토그램을 볼 컬럼을 선택하세요", numeric_cols, key="hist_col")
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)
    if "상관관계 히트맵" in selected_viz and len(numeric_cols) > 1:
        st.write("### 상관관계 히트맵")
        fig2, ax2 = plt.subplots()
        corr = df[numeric_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax2)
        st.pyplot(fig2)
    if len(numeric_cols) == 0:
        st.info("수치형 컬럼이 없습니다.")
