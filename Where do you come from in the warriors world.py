riverclan = 0
thunderclan = 0
shadowclan = 0
windclan = 0
tribeofrushingwater = 0
bloodclan = 0
sundrownplace = 0
twoleghomes = 0
welcome_message = input ('Welcome to "Where Do You Come From in the Warriors World!" push A and then enter to begin when ready! (Case sensitive, please use a capital A)')
if welcome_message == 'A':
    favouritepartofbooks = input ('First off, choose one think that you enjoy the most about the Warriors series - A: The evil characters. B: The forbidden relationships. C: The Starclan dreams. D: The drama :3. E: The chill parts!')
    wheretolive = input ("Great! Now, choose a place you'd want to stay - A: By the ocean. B: In a comfy, welcoming home. C: In a forest cottage. D: In a tiny, old city appartment. E: On a remote mountainside. F: Sleeping under the stars.")
    genreofbook = input ("Choose a genre of books from this list - A: Fantasy. B: Romance. C: Action. D: Mystery. E: Survival. F: Horror.")
    if favouritepartofbooks == 'A':
        bloodclan += 1
        shadowclan += 1
    if favouritepartofbooks == 'B':
        thunderclan += 1
        windclan += 1
        shadowclan += 1
    if favouritepartofbooks == 'C':
        tribeofrushingwater += 1
        sundrownplace += 1
    if favouritepartofbooks == 'D':
        riverclan += 1
        windclan += 1
        tribeofrushingwater += 1
    if favouritepartofbooks == 'E':
        sundrownplace += 1
        twoleghomes += 1
    if wheretolive == 'A':
        sundrownplace +=1
    if wheretolive == 'B':
        thunderclan += 1
        twoleghomes += 1
    if wheretolive == 'C':
        shadowclan += 1
        riverclan += 1
    if wheretolive == 'D':
        bloodclan += 1
    if wheretolive == 'E':
        tribeofrushingwater += 1
    if wheretolive == 'F':
        windclan += 1
    if genreofbook == 'A':
        riverclan += 1
    if genreofbook == 'B':
        twoleghomes += 1
        sundrownplace += 1
    if genreofbook == 'C':
        thunderclan += 1
    if genreofbook == 'D':
        windclan += 1
    if genreofbook == 'E':
        tribeofrushingwater += 1
        shadowclan += 1
    if genreofbook == 'F':
        bloodclan += 1
if riverclan == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Riverclan!")
elif thunderclan == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Thunderclan!")
elif shadowclan == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Shadowclan!")
elif windclan == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Windclan!")
elif tribeofrushingwater == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in the Tribe of Rushing Water!")
elif bloodclan == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live with the cats of Bloodclan!")
elif sundrownplace == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live by the Sundrownplace! Maybe you've met Midnight, too!")
elif twoleghomes == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in a comfortable twoleg nest with your housefolk!")
else:
    answer = ("Your answer is a tie! Maybe try again?")
print (answer)
    
                         
            

        
        
        
        

        
    
