import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    간단한 전처리 예시:
    - 결측치(NaN) 컬럼별로 제거 또는 평균/최빈값 대체
    - 필요시 컬럼 선택
    """
    df_clean = df.copy()
    # 결측치가 있는 컬럼을 사용자에게 선택하게 할 수도 있음
    for col in df_clean.columns:
        if df_clean[col].dtype in ["float64", "int64"]:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
        else:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0] if not df_clean[col].mode().empty else "")
    return df_clean
