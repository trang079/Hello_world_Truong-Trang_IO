import pandas as pd
try:
    url = "https://githubusercontent.com"
    df = pd.read_csv(url)
    q1_weight = df['weight_kg'].quantile(0.25)
    print(f"Первый квартиль (Q1) по массе составляет: {q1_weight:.1f} кг")
except Exception as e:
    print(f"Произошла ошибка: {e}")


