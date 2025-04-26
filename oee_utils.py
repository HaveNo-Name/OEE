def calculate_oee(row):
    try:
        operating_time = row['operating_time']  # Updated to match the transformed column name
        planned_time = row['planned_production_time']  # Same here
        good_count = row['good_count']  # Same here
        reject_count = row['reject_count']  # Same here
        ideal_cycle_time = row['ideal_cycle_time']  # Same here

        availability = operating_time / planned_time if planned_time else 0
        performance = (ideal_cycle_time * (good_count + reject_count)) / operating_time if operating_time else 0
        quality = good_count / (good_count + reject_count) if (good_count + reject_count) else 0

        oee = availability * performance * quality * 100
        return round(oee, 2)
    except Exception as e:
        print(f"Error calculating OEE: {e}")
        return 0.0
