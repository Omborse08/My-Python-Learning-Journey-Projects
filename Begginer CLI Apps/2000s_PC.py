Your_Mood = {
    "sad": [
        "lonely", "sad", "down", "depressed", "tired", "broken",
        "empty", "gloomy", "crying", "hopeless", "worthless"
    ],
    
    "happy": [
        "happy", "excited", "fun", "joy", "glad", "smiling",
        "peaceful", "content", "chill", "relaxed", "grateful"
    ],
    
    "angry": [
        "angry", "mad", "furious", "annoyed", "irritated",
        "rage", "pissed", "agitated", "frustrated"
    ],
    
    "anxious": [
        "nervous", "anxious", "worried", "scared", "tense",
        "stressed", "panicking", "afraid", "shaky", "overthinking"
    ],
    
    "bored": [
        "bored", "lazy", "idle", "dull", "unmotivated",
        "blank", "meh", "tired", "wasting time"
    ]
}
while True:
    print("🧠 AI Therapist CLI – How are you feeling today?")
    mood = input(">> ").lower().split(" ")

    detected = None
    for key, value in Your_Mood.items():
        for word in mood:
            if word in value:
                detected = key 
                break   
        if detected:
            break
    

    print("\nAnalyzing...")
    if detected:
        print(f"\nDetected Mood: {detected}")
        if detected == "sad":
            print("\nTip> Don't be a sad")
        elif detected == "happy":
            print("\nTip> Be a Happy Always! ")
        elif detected == "angry":
            print("\nTip> Take a Deep breath! ")
        elif detected == "anxious":
            print("\nTip>  don't Afrade of anything! ")
        elif detected == "bored":
            print("\nTip> Do few fun activities! ")

    else:
        print("\n> Sorry, I couldn't understand your mood 😔")
        print("> Try using words like 'sad', 'happy', 'angry', etc.")