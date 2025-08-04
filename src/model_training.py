import pandas as pd

def analyze_turnover_and_revenue(reservations_df, cafes_df):
    # 1. 유효 예약만 필터링 (예: status='completed')
    completed = reservations_df[reservations_df['status'] == 'completed'].copy()

    # 2. 이용 시간(분) 계산
    completed['usage_minutes'] = (completed['end_time'] - completed['start_time']).dt.total_seconds() / 60

    # 3. 카페별 총 이용 시간, 총 매출, 좌석 수 집계
    merged = completed.merge(cafes_df[['cafe_id', 'max_seats']], on='cafe_id')

    summary = merged.groupby('cafe_id').agg(
        total_usage_minutes=pd.NamedAgg(column='usage_minutes', aggfunc='sum'),
        total_revenue=pd.NamedAgg(column='order_amount', aggfunc='sum'),
        max_seats=pd.NamedAgg(column='max_seats', aggfunc='first')
    ).reset_index()

    # 4. 회전율 = 총 이용 시간 / (좌석 수 * 기간(분))
    min_date = completed['start_time'].min()
    max_date = completed['end_time'].max()
    total_period_minutes = (max_date - min_date).total_seconds() / 60

    summary['turnover_rate'] = summary['total_usage_minutes'] / (summary['max_seats'] * total_period_minutes)

    # 5. 시간당 매출 = 총 매출 / 총 이용 기간(시간)
    summary['revenue_per_hour_per_seat'] = summary['total_revenue'] / (summary['total_usage_minutes'] / 60)

    return summary

if __name__ == "__main__":
        
    # 데이터 불러오기
    reservations_df = pd.read_csv("data/reservations.csv", parse_dates=["start_time", "end_time"])
    cafes_df = pd.read_csv("data/cafes.csv")

    from model_training import analyze_turnover_and_revenue
    
    print("분석 시작") # 로그
    summary = analyze_turnover_and_revenue(reservations_df, cafes_df)

    print(summary)

