WORKOUTS = {
    "weight loss": ["Walking", "Skipping", "Cycling", "Plank"],
    "muscle gain": ["Pushups", "Squats", "Deadlifts"],
    "general fitness": ["Yoga", "Stretching", "Jogging"]
}

def workout_goal(goal):
    return WORKOUTS.get(goal.lower(), ["Light exercise & stretching"])
