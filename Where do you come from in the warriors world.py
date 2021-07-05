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
if riverclan == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Riverclan!")
if thunderclan == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Thunderclan!")
if shadowclan == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Shadowclan!")
if windclan == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Windclan!")
if tribeofrushingwater == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in the Tribe of Rushing Water!")
if bloodclan == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live with the cats of Bloodclan!")
if sundrownplace == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live by the Sundrownplace! Maybe you've met Midnight, too!")
if twoleghomes == max(riverclan, thunderclan, shadowclan, windclan, tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in a comfortable twoleg nest with your housefolk!")
print (answer)
    
                         
            

        
        
        
        

        
    
