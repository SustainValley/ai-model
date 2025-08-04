import pandas as pd
import uuid
import os
import random

def generate_seats(cafes_df):
    seats = []
    for _, row in cafes_df.iterrows():
        cafe_id = row['cafe_id']
        max_seats = row['max_seats']
        for i in range(max_seats):
            seat_id = str(uuid.uuid4())
            seats.append({
                'seat_id': seat_id,
                'seat_type': 'table',
                'cafe_id': cafe_id
            })
    return pd.DataFrame(seats)

def generate_reservation_seats(reservations_df, seats_df):
    reservation_seats = []
    # 좌석을 카페별로 모아둠
    seats_by_cafe = seats_df.groupby('cafe_id')['seat_id'].apply(list).to_dict()

    for _, res in reservations_df.iterrows():
        res_id = res['reservation_id']
        cafe_id = res['cafe_id']
        people_count = res['people_count']

        available_seats = seats_by_cafe.get(cafe_id, [])
        # 랜덤으로 people_count 개 좌석 선택 (중복없이)
        chosen_seats = random.sample(available_seats, min(people_count, len(available_seats)))

        for seat_id in chosen_seats:
            reservation_seats.append({
                'reservation_id': res_id,
                'seat_id': seat_id
            })

    return pd.DataFrame(reservation_seats)

if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)

    cafes_df = pd.read_csv('data/cafes.csv')
    reservations_df = pd.read_csv('data/reservations.csv')

    seats_df = generate_seats(cafes_df)
    seats_df.to_csv('data/seats.csv', index=False)
    print('seats.csv 생성 완료')

    reservation_seats_df = generate_reservation_seats(reservations_df, seats_df)
    reservation_seats_df.to_csv('data/reservation_seats.csv', index=False)
    print('reservation_seats.csv 생성 완료')
