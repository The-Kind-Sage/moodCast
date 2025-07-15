import datetime

# Basic emotion-to-weather mapping
weather_map = {
    "happy": "Sunny with radiant bursts of joy ☀️",
    "sad": "Rainy with scattered showers of introspection 🌧️",
    "angry": "Thunderstorms with lightning bolts of rage ⛈️",
    "anxious": "Foggy with whispers of uncertainty 🌫️",
    "excited": "Electrifying with sparks of anticipation ⚡",
    "tired": "Overcast with drowsy drizzles 🌥️",
    "curious": "Partly cloudy with bright patches of inquiry 🌤️",
    "lonely": "Cold front with distant echoes 🌬️",
}

def analyze_mood(input_text):
    input_lower = input_text.lower()
    for mood, forecast in weather_map.items():
        if mood in input_lower:
            return forecast
    return "Unpredictable with sudden mood swings 🌪️"

def main():
    print("Welcome to MoodCast CLI ☁️")
    mood_input = input("How are you feeling today?\n> ")

    print("\nAnalyzing mood... 🔍")
    forecast = analyze_mood(mood_input)

    print(f"\nMood Forecast: {forecast}\n")

    # Logging session
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("moodcast_log.txt", "a") as log:
        log.write(f"{timestamp} | Mood: {mood_input} | Forecast: {forecast}\n")

    print("Your mood has been logged to moodcast_log.txt ✅")

if __name__ == "__main__":
    main()
