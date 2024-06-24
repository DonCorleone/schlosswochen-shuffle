import random

def assign_weeks_with_waitlist(reservations, max_slots=4):
    # Create a dictionary to count slots for each week
    week_slots = {1: 0, 2: 0, 3: 0}
    assignments = []
    waitlist = []
    
    # Shuffle reservations to randomize selection
    random.shuffle(reservations)
    
    for reservation in reservations:
        assigned = False
        for preferred_week in reservation["preferences"]:
            if week_slots[preferred_week] < max_slots:
                assignments.append({"user_id": reservation["user_id"], "assigned_week": preferred_week})
                week_slots[preferred_week] += 1
                assigned = True
                break
        
        if not assigned:
            waitlist.append({"user_id": reservation["user_id"], "preferences": reservation["preferences"]})

    return assignments, waitlist

# Example usage
reservations = [
    {"user_id": 1, "preferences": [1]},
    {"user_id": 2, "preferences": [2, 3]},
    {"user_id": 3, "preferences": [1, 3, 2]},
    {"user_id": 4, "preferences": [2]},
    {"user_id": 5, "preferences": [3, 1]},
    {"user_id": 6, "preferences": [1, 3]},
    {"user_id": 7, "preferences": [2, 3]},
    {"user_id": 8, "preferences": [1, 2]},
    {"user_id": 9, "preferences": [3]},
    {"user_id": 10, "preferences": [1, 2, 3]},
    {"user_id": 11, "preferences": [2, 3]},
    {"user_id": 12, "preferences": [1, 3]},
    {"user_id": 13, "preferences": [2, 1]},
    {"user_id": 14, "preferences": [3, 1]},
    {"user_id": 15, "preferences": [1, 2]},
    {"user_id": 16, "preferences": [3]},
    {"user_id": 17, "preferences": [1, 2, 3]},
    {"user_id": 18, "preferences": [2, 3]},
    {"user_id": 19, "preferences": [1, 3]},
    {"user_id": 20, "preferences": [2, 1]},
    {"user_id": 21, "preferences": [3, 1]},
    {"user_id": 22, "preferences": [1, 2]},
    {"user_id": 23, "preferences": [3]},
    {"user_id": 24, "preferences": [1, 2, 3]},
    {"user_id": 25, "preferences": [2, 3]},
    {"user_id": 26, "preferences": [1, 3]},
    {"user_id": 27, "preferences": [2, 1]},
    {"user_id": 28, "preferences": [3, 1]},
    {"user_id": 29, "preferences": [1, 2]},
    {"user_id": 30, "preferences": [3]},
    {"user_id": 31, "preferences": [1, 2, 3]},
    {"user_id": 32, "preferences": [2, 3]},
    {"user_id": 33, "preferences": [1, 3]},
    {"user_id": 34, "preferences": [2, 1]},
    {"user_id": 35, "preferences": [3, 1]},
    {"user_id": 36, "preferences": [1, 2]},
    {"user_id": 37, "preferences": [3]},
    {"user_id": 38, "preferences": [1, 2, 3]},
    {"user_id": 39, "preferences": [2, 3]},
    {"user_id": 40, "preferences": [1, 3]},
    {"user_id": 41, "preferences": [2, 1]},
    {"user_id": 42, "preferences": [3, 1]},
    {"user_id": 43, "preferences": [1, 2]},
    {"user_id": 44, "preferences": [3]},
    {"user_id": 45, "preferences": [1, 2, 3]},
    {"user_id": 46, "preferences": [2, 3]},
    {"user_id": 47, "preferences": [1, 3]},
    {"user_id": 48, "preferences": [2, 1]},
    {"user_id": 49, "preferences": [3, 1]},
    {"user_id": 50, "preferences": [1, 2]}
    # Add more reservations as needed
]

assigned_weeks, waitlist = assign_weeks_with_waitlist(reservations, max_slots=10)
for assignment in assigned_weeks:
    print(f"User {assignment['user_id']} assigned to week {assignment['assigned_week']}")
print("\nWaitlist:")
for entry in waitlist:
    print(f"User {entry['user_id']} on waitlist with preferences {entry['preferences']}")