import pandas as pd
import uuid
import random
import os
from datetime import datetime, timedelta

def generate_reservations_per_cafe(cafes_df, per_cafe=100):
    reservations = []

    for _, cafe in cafes_df.iterrows():
        cancelled_count = 0
        cafe_id = cafe['cafe_id']
        max_shared = cafe['max_shared_seats']

        for _ in range(per_cafe):
            # 날짜/시간 생성
            start_date = datetime.now() - timedelta(days=random.randint(0, 30))
            start_hour = random.randint(9, 23)  # 오전 8시 ~ 밤 12시
            start_time = start_date.replace(hour=start_hour, minute=0, second=0, microsecond=0)
            end_time = start_time + timedelta(hours=random.randint(1, 4))

            # 상태(status) 생성 (cancelled는 15건 제한)
            possible_status = ['reserved', 'completed', 'cancelled']
            if cancelled_count >= 15:
                possible_status.remove('cancelled')
            status = random.choice(possible_status)
            if status == 'cancelled':
                cancelled_count += 1

            reservations.append({
                "reservation_id": str(uuid.uuid4()),
                "start_time": start_time.strftime('%Y-%m-%d %H:%M:%S'),
                "end_time": end_time.strftime('%Y-%m-%d %H:%M:%S'),
                "people_count": random.randint(1, max_shared),
                "status": status,
                "order_amount": random.randint(6000, 30000),
                "user_id": str(uuid.uuid4()),
                "cafe_id": cafe_id
            })

    return pd.DataFrame(reservations)


if __name__ == "__main__":
    cafes_df = pd.read_csv("data/cafes.csv")
    reservations_df = generate_reservations_per_cafe(cafes_df, per_cafe=100)

    os.makedirs("data", exist_ok=True)
    reservations_df.to_csv("data/reservations.csv", index=False)
    print("카페별 예약 100건씩 총 {}건 생성, data/reservations.csv 저장 완료".format(len(reservations_df)))
