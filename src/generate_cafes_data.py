import pandas as pd # type: ignore
import uuid
import os

def generate_cafes():
    cafes = [
        {
            "cafe_id": str(uuid.uuid4()),
            "name": "아너카페",
            "location": "서울 노원구 동일로192다길 9",
            "max_seats": 60,
            "noise_levels": "low",
            "seat_fee": 8000,
            "max_shared_seats": 4
        },
        {
            "cafe_id": str(uuid.uuid4()),
            "name": "블루마일스커피로스터즈",
            "location": "서울 노원구 동일로190길 65 2층",
            "max_seats": 20,
            "noise_levels": "high",
            "seat_fee": 7000,
            "max_shared_seats": 8
        },
        {
            "cafe_id": str(uuid.uuid4()),
            "name": "카페 오어낫",
            "location": "서울 노원구 동일로184길 69-9 1층",
            "max_seats": 15,
            "noise_levels": "medium",
            "seat_fee": 3000,
            "max_shared_seats": 4
        },
        {
            "cafe_id": str(uuid.uuid4()),
            "name": "무이로 커피",
            "location": "서울 노원구 동일로186길 77-7 1층",
            "max_seats": 18,
            "noise_levels": "high",
            "seat_fee": 4000,
            "max_shared_seats": 4
        },
        {
            "cafe_id": str(uuid.uuid4()),
            "name": "오르름",
            "location": "서울 노원구 노원로1길 121 1층",
            "max_seats": 28,
            "noise_levels": "low",
            "seat_fee": 4000,
            "max_shared_seats": 8
        }
    ]
    return pd.DataFrame(cafes)

if __name__ == "__main__":
    # 데이터프레임 생성
    cafes_df = generate_cafes()

    # data 폴더 없으면 생성
    os.makedirs("data", exist_ok=True)

    # CSV 저장
    cafes_df.to_csv("data/cafes.csv", index=False)
    print("데이터 저장 완료: data/cafes.csv")
