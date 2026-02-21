size=int(input("Enter the no of songs in your playlist:"))
song=[0]*size
for i in range(size):
    song[i]=int(input(f"Enter the time duration of the track {i+1}: "))
inv=False
dup=False
for time in song:
    if time<=0:
        inv=True
        break
if inv:
    print("Category: Invalid Playlist")
    print("Reason: The song durations are invalid.")
    print("Analysis Stopped!")
else:
    total=sum(song)
    count=len(song)
    diff=max(song)-min(song)
    for i in range(size):
        for j in range(i+1, size):
            if song[i]==song[j]:
                dup=True
                break
        if dup:
            break
    category=""
    message=""
    if total<300:
        category="Too Short"
        message = "Try adding a few more songs"
    elif total>3600:
        category = "Too Long"
        message = "Consider reducing the number of songs"
    elif dup:
        category="Repetitive"
        message="Try adding more songs"
    elif diff>=30:
        category="Balanced"
        message="Good Job!! Its very well structured"
    else:
        category="Irregular"
        message="Durations are too similar"
    if count<=5:
        insight="You prefer short and quick playlists!!"
    elif count<=20:
        insight="You enjoy listening sessions!!"
    else:
        insight="You enjoy deep listening sessions!!"
    print("\n----- Playlist Summary -----")
    print("Total Duration:",total,"seconds")
    print("Songs:",count)
    print("Category:", category,"Playlist")
    print("Recommendation:", message)
    print("Insight:",insight)
    print("----------------------------\n")
