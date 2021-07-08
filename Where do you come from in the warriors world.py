from tkinter import *
import tkinter as tk
import tkinter.simpledialog
root = tk.Tk()
riverclan = 0
thunderclan = 0
shadowclan = 0
windclan = 0
tribeofrushingwater = 0
bloodclan = 0
sundrownplace = 0
twoleghomes = 0
welcome_message = tkinter.simpledialog.askstring (\
'Welcome', 'Welcome to "Where Do You Come From in the Warriors World! \
Push A and then enter to begin when ready! \
(Case sensitive, please use a capital A)')
if welcome_message == 'A':
    favouritepartofbooks = tkinter.simpledialog.askstring (\
    'Favourite Part of Books', 'First off, choose one thing that you enjoy the most about the Warriors series:  \
    A: The evil characters. \
    B: The forbidden relationships. \
    C: The Starclan dreams. \
    D: The drama :3. \
    E: The chill parts!')
    wheretolive = tkinter.simpledialog.askstring (\
    'Where to Live', "Great! Now, choose a place you'd want to stay: \
    A: By the ocean. \
    B: In a comfy, welcoming home. \
    C: In a forest cottage. \
    D: In a tiny, old city appartment. \
    E: On a remote mountainside. \
    F: Sleeping under the stars.")
    genreofbook = tkinter.simpledialog.askstring (\
    'Genre of Book', "Choose a genre of books from this list: \
    A: Fantasy. \
    B: Romance. \
    C: Action. \
    D: Mystery. \
    E: Survival. \
    F: Horror.")
    bestmedicinecat = tkinter.simpledialog.askstring (\
    'Best Medicine Cat', "Out of these four medecine cats, choose one you think is the best! \
    A: Mothwing. \
    B: Runningnose. \
    C: Spottedleaf. \
    D: Kestrelflight.")
    bestleader = tkinter.simpledialog.askstring (\
    'Best Leader', "Out of these leaders, which one do you think is the best? \
    A: Bramblestar. \
    B: Scourge. \
    C: Firestar. \
    D: Bluestar. \
    E: Leopardstar. \
    F: Onestar. \
    G: Rowanstar.")
    herbs = tkinter.simpledialog.askstring ('Herbs', "Herbs? \
A: I have no idea about them and that they do. \
B: Herbs are for softies. \
C: That's for our healer to deal with. \
D: Our clan uses multiple herbs for all kinds of problems.")
else:
    print ("Okay!")
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
if herbs == 'A':
    twoleghomes += 1
    sundrownplace += 1
if herbs == 'B':
    bloodclan += 1
if herbs == 'C':
    tribeofrushingwater += 1
if herbs == 'D':
    thunderclan += 1
    riverclan += 1
    shadowclan += 1
    windclan += 1
if riverclan == max(riverclan, thunderclan, shadowclan, windclan,\
 tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Riverclan!")
elif thunderclan == max(riverclan, thunderclan, shadowclan, windclan,\
 tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Thunderclan!")
elif shadowclan == max(riverclan, thunderclan, shadowclan, windclan,\
 tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Shadowclan!")
elif windclan == max(riverclan, thunderclan, shadowclan, windclan,\
 tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in Windclan!")
elif tribeofrushingwater == max(riverclan, thunderclan, shadowclan, windclan,\
 tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in the Tribe of Rushing Water!")
elif bloodclan == max(riverclan, thunderclan, shadowclan, windclan,\
 tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live with the cats of Bloodclan!")
elif sundrownplace == max(riverclan, thunderclan, shadowclan, windclan,\
 tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live by the Sundrownplace! Maybe you've met Midnight, too!")
elif twoleghomes == max(riverclan, thunderclan, shadowclan, windclan,\
 tribeofrushingwater, bloodclan, sundrownplace, twoleghomes):
    answer = ("You live in a comfortable twoleg nest with your housefolk!")
else:
    answer = ("Your answer is a tie!")
tkinter.messagebox.showinfo('Your Result', (answer))
