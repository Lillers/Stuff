riverclan = 0
thunderclan = 0
shadowclan = 0
windclan = 0
tribeofrushingwater = 0
bloodclan = 0
sundrownplace = 0
twoleghomes = 0
welcome_message = input ('Welcome to "Where Do You Come From in the Warriors World! \n \
 Push A and then enter to begin when ready! \n \
 (Case sensitive, please use a capital A)\n')
if welcome_message == 'A':
    favouritepartofbooks = input ('First off, choose one think that you enjoy the most about the Warriors series: \n \
     A: The evil characters. \n \
     B: The forbidden relationships. \n \
     C: The Starclan dreams.\n \
     D: The drama :3. \n \
     E: The chill parts! \n')
    wheretolive = input ("Great! Now, choose a place you'd want to stay: \n \
    A: By the ocean. \n \
    B: In a comfy, welcoming home. \n \
    C: In a forest cottage. \n \
    D: In a tiny, old city appartment. \n \
    E: On a remote mountainside. \n \
    F: Sleeping under the stars. \n")
    genreofbook = input ("Choose a genre of books from this list: \n \
    A: Fantasy. \n \
    B: Romance. \n \
    C: Action. \n \
    D: Mystery. \n \
    E: Survival. \n \
    F: Horror. \n")
    bestmedicinecat = input ("Out of these four medecine cats, choose one you think is the best! \n \
    A: Mothwing. \n \
    B: Runningnose. \n \
    C: Spottedleaf. \n \
    D: Kestrelflight. \n")
    bestleader = input ("Out of these leaders, which one do you think is the best? \n \
      A: Bramblestar. \n \
      B: Scourge. \n \
      C: Firestar. \n \
      D: Bluestar. \n \
      E: Leopardstar. \n \
      F: Onestar. \n \
      G: Rowanstar. \n")
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
    if bestmedicinecat == 'A':
        riverclan += 1
    if bestmedicinecat == 'B':
        shadowclan += 1
    if bestmedicinecat == 'C':
        thunderclan += 1
    if bestmedicinecat == 'D':
        windclan += 1
    if bestleader == 'A':
        sundrownplace += 1
    if bestleader == 'B':
        bloodclan += 1
    if bestleader == 'C':
        twoleghomes += 1
    if bestleader == 'D':
        thunderclan += 1
    if bestleader == 'E':
        riverclan += 1
    if bestleader == 'F':
        windclan += 1
    if bestleader == 'G':
        shadowclan += 1

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
    answer = ("Your answer is a tie!")
print (answer)
