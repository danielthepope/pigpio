import pickle
leds = [24, 23, 22, 21, 18, 17]

# All you need to do is paste the output from Excel into this script, complete
# the variables and run it. No sudo required.
filename = "animation.seq" # Rename this, but keep the .seq!

# Paste the Excel output over this sample

animation = []
animation.append([[leds[0],1],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
animation.append([[leds[0],0.5],[leds[1],1],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
animation.append([[leds[0],0.2],[leds[1],0.5],[leds[2],1],[leds[3],0],[leds[4],0],[leds[5],0]])
animation.append([[leds[0],0],[leds[1],0.2],[leds[2],0.5],[leds[3],1],[leds[4],0],[leds[5],0]])
animation.append([[leds[0],0],[leds[1],0],[leds[2],0.2],[leds[3],0.5],[leds[4],1],[leds[5],0]])
animation.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0.2],[leds[4],0.5],[leds[5],1]])
animation.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0.2],[leds[5],0.5]])
animation.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0.2]])
animation.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
animation.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],1]])
animation.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],1],[leds[5],0.5]])
animation.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],1],[leds[4],0.5],[leds[5],0.2]])
animation.append([[leds[0],0],[leds[1],0],[leds[2],1],[leds[3],0.5],[leds[4],0.2],[leds[5],0]])
animation.append([[leds[0],0],[leds[1],1],[leds[2],0.5],[leds[3],0.2],[leds[4],0],[leds[5],0]])
animation.append([[leds[0],1],[leds[1],0.5],[leds[2],0.2],[leds[3],0],[leds[4],0],[leds[5],0]])
animation.append([[leds[0],0.5],[leds[1],0.2],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
animation.append([[leds[0],0.2],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
animation.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])


# Now don't delete this bit
print "Just be aware that this will save whatever you pasted to",filename
if raw_input("Is that OK (just say 'yes')") == 'yes':
    print "Cool. I'll just save that."
    pickle.dump(animation, open(filename, "wb"))
    print "Done."
else:
    print "OK, I won't do anything."
