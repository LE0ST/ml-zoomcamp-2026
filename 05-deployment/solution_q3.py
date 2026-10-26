import pickle
from model import normalize_record

client = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41,
}

with open("pipeline.bin", "rb") as f:
    pipeline = pickle.load(f)

record = normalize_record(client)
prob = float(pipeline.predict_proba([record])[0, 1])
print(f"Conversion probability: {prob:.6f}")
print(f"Rounded to 3 decimals: {round(prob, 3)}")
