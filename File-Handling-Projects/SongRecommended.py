print("🎧 Welcome to Emotion-Based Music Recommender 🎧")
feels = input("\nHow are you feeling today? → ").lower()
name = ["sad","happy","angry","motivated","romantic"]
if feels in name:
    position = 0
    while True:
        song = "Songs/" + feels + '.txt'
        print(f"📝 Reading songs from: {song}")
        print(f"\n📍 Reading at Byte Position: {position}")
        with open(song,'r') as file:
            file.seek(0,2)
            end_position = file.tell()
            file.seek(position)
            if position >= end_position:
                print("\n🎵 You listened to all songs!")
                mood = input("\nDo you want to restart the playlist? (y/n): ")
                if mood == "y":
                    position = 0
                else:
                    print("\n🔥 Tip: Music is therapy. Hope you feel better soon!")
                    break
                    
            else:
                print(f"\n> Songs: {file.readline().strip()}")
                print(f"> Songs: {file.readline().strip()}")
                position = file.tell()

        again = input("\nWant more recommendations? (y/n): ")
        match again:
            case "y":
                print(f"\n📍 File position before reread: {position}")

            case "n":
                print("\n🔥 Tip: Music is therapy. Hope you feel better soon!")
                break
            case _:
                print("\nInvalid Options! ")
else:
    print("\nList Not Available")