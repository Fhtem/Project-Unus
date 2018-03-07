import pickle

xp_values = pickle.load(open("ExperienceValues.p", "rb"))
print (xp_values)

def try_xp_gain():
    while True:
        try:
            xp_gain = int(input("Experience gained: "))
            break
        except ValueError:
            print ("That be no integer! To quit, type \"0\"")
    return xp_gain

def xp_values_gain(character):
    end = False
    while end == False:
        xp_gain = try_xp_gain()
        if xp_gain != 0:
            xp_values[character] += xp_gain
        elif xp_gain == 0:
            end = True
        else:
            print ("To stop adding, type \"0\"")
    else:
        print (xp_values.items())

def character_checker():
    fin = False
    while fin == False:
        character = input("XP gainer: ")
        if character in xp_values:
            xp_values_gain(character)
        elif character == "n":
            fin = True
        else:
            print ("That person isn't in the list. To quit, type \"n\"")
    else:
        print (xp_values.items())

character_checker()

pickle.dump(xp_values, open('ExperienceValues.p', 'wb'))
