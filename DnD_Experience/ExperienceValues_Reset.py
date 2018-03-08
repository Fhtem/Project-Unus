import pickle

xp_values = pickle.load(open("ExperienceValues.p", "rb"))

for key in xp_values:
    xp_values[key] = 0

pickle.dump(xp_values, open('ExperienceValues.p', 'wb'))
