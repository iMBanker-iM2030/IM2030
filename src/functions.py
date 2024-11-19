excludedCol = ['고객ID', '기준년월']
def df_value_counts(df, excludedCol = None):
    for col in df.columns:
        if excludedCol:
            if col not in excludedCol:
                df[col].value_counts()
        else:
            df[col].value_counts()


def anova(df, col1, col2):
    from scipy.stats import f_oneway
    from pingouin import pairwise_gameshowell

    categories = df[col1].unique()

    # 각 범주에 대해 col2 데이터를 추출하여 리스트로 생성
    grouped_data = [df[df[col1] == category][col2] for category in categories]

    # f_oneway를 사용하여 ANOVA 분석 실행
    f_value, p_value = f_oneway(*grouped_data)

    # 결과 출력
    print(f"F-value: {f_value}")
    print(f"P-value: {p_value}")

    # p-value에 따라 결론 내기
    if p_value < 0.05:
        print("그룹 간 평균에 유의미한 차이가 있습니다.")
    else:
        print("그룹 간 평균에 유의미한 차이가 없습니다.")
    posthoc = pairwise_gameshowell(dv=col2, between=col1, data=df)
    print(posthoc)


def x2(df):
    from scipy.stats import chi2_contingency
    # 카이제곱 검정 수행
    chi2, p, dof, expected = chi2_contingency(df)

    # 결과 출력
    print(f"Chi2 statistic: {chi2}")
    print(f"P-value: {p}")
    print(f"Degrees of freedom: {dof}")
    print(f"Expected frequencies: \n{expected}")

    # p-value에 따라 결론 도출
    if p < 0.05:
        print("두 변수 간에 연관이 있습니다. (귀무가설 기각)")
    else:
        print("두 변수 간에 연관이 없습니다. (귀무가설 채택)")
