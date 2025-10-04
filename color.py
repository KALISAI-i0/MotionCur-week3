import random
import time

# 🎨 Mood/Event to Outfit Mapping
outfit_suggestions = {
    "happy": {
        "colors": ["yellow", "pink"],
        "outfits": [
            "a sunny yellow t-shirt with denim shorts ☀️",
            "a pink blouse with white jeans 💕",
            "a yellow hoodie with blue jeans 🌼"
        ]
    },
    "calm": {
        "colors": ["blue", "white"],
        "outfits": [
            "a sky-blue shirt with beige pants 🌤️",
            "a white hoodie with light jeans 🤍",
            "a blue t-shirt with khaki trousers 🌊"
        ]
    },
    "confident": {
        "colors": ["red", "black"],
        "outfits": [
            "a bold red shirt with black jeans 🔥",
            "a sleek black suit with a red tie 🕴️",
            "a red dress with black heels ❤️"
        ]
    },
    "energetic": {
        "colors": ["orange", "yellow"],
        "outfits": [
            "an orange tank top with joggers 💪",
            "a yellow hoodie with ripped jeans ⚡",
            "an orange t-shirt with shorts ☀️"
        ]
    },
    "stressed": {
        "colors": ["green", "blue"],
        "outfits": [
            "a mint green sweater with cream trousers 🍃",
            "a navy blue tee with white shorts 🌊",
            "a soft green hoodie with beige pants 🌿"
        ]
    },
    "interview": {
        "colors": ["blue", "black", "white"],
        "outfits": [
            "a navy blazer with white shirt and black pants 💼",
            "a black dress with subtle accessories 👩‍💼",
            "a white shirt with blue slacks 👔"
        ]
    },
    "date": {
        "colors": ["red", "black"],
        "outfits": [
            "a red dress with black heels ❤️",
            "a black shirt with red accents 💋",
            "a red top with black trousers 💞"
        ]
    },
    "party": {
        "colors": ["gold", "red", "black"],
        "outfits": [
            "a glittery gold top with black skirt 🎉",
            "a red sequin dress with heels 💃",
            "a black leather jacket with gold accents 🕺"
        ]
    },
    "casual outing": {
        "colors": ["green", "white"],
        "outfits": [
            "a white t-shirt with green joggers 🧢",
            "a green flannel over white tee 👟",
            "a comfy white hoodie with khaki pants ☁️"
        ]
    }
}

# 💬 Fashion Quotes
fashion_quotes = [
    "“Style is a way to say who you are without having to speak.” – Rachel Zoe",
    "“Fashion fades, style is eternal.” – Yves Saint Laurent",
    "“You can never be overdressed or overeducated.” – Oscar Wilde",
    "“Dress like you’re already famous.” – Unknown",
    "“Life’s too short to wear boring clothes.” – Cushnie et Ochs"
]

# 🧠 Function to Get Outfit
def get_outfit(user_input):
    user_input = user_input.lower().strip()
    if user_input in outfit_suggestions:
        suggestion = random.choice(outfit_suggestions[user_input]["outfits"])
        print(f"\n✨ You’re feeling {user_input}. Try wearing {suggestion}")
        print(random.choice(fashion_quotes))
        
        # Optional: Save history
        save_to_history(user_input, suggestion)
    else:
        print("\n😅 Sorry, I don’t have suggestions for that mood/event yet.")
        print("Try one of these: happy, calm, confident, energetic, stressed, interview, date, party, casual outing.")

# 💾 Save history to file
def save_to_history(mood, suggestion):
    try:
        with open("outfit_history.txt", "a", encoding="utf-8") as file:
            file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {mood.title()}: {suggestion}\n")
    except Exception as e:
        print(f"⚠️ Could not save history: {e}")

# 🎯 Main Function
def main():
    print("👕 Welcome to the Mood-Based Outfit Recommender 👗")
    print("Tell me your current mood or event, and I’ll suggest a stylish outfit!\n")
    time.sleep(1)

    while True:
        user_input = input("👉 Enter mood or event (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("\n👋 Thanks for using the Outfit Recommender! Stay stylish!")
            break
        get_outfit(user_input)
        print("-" * 60)

# 🚀 Run Program
if __name__ == "__main__":
    main()
