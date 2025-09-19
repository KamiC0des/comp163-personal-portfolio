monthly_budget = {
    "Food" : 300,
    "Entertainment" : 130,
    "Books" : 125,
    "Transportation" : 100
}
study_hrs = {
    "Programming" : 6,
    "Math" : 4,
    "English" : 3,
    "History" : 3
}

total_monthly_budget = monthly_budget["Food"] + monthly_budget["Entertainment"] + monthly_budget["Books"] + monthly_budget["Transportation"]
daily_food_budget = monthly_budget["Food"] / 30
annual_budget = total_monthly_budget * 12
total_study_hrs = study_hrs["Programming"] + study_hrs["Math"] + study_hrs["English"] + study_hrs["History"]
study_cost_per_hr = monthly_budget["Books"] / total_study_hrs

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${total_monthly_budget}")
print(f"Food: ${monthly_budget["Food"]} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget["Entertainment"]}")
print(f"Books: ${monthly_budget["Books"]}")
print(f"Transportation: ${monthly_budget["Transportation"]}")
print(f"Annual Projection: ${annual_budget}")