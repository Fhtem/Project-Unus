import pickle

#inventory = {"amanda" : {}, "neo" : {}, "kari" : {}, "kade" : {}, "storm" : {}, "emily" : {}, "jacob" : {}, "keegan" : {}}
inventory = pickle.load(open("Dnd_Inventories.p", "rb"))

# creates list for do_names method
character_list = []
for key in inventory:
    character_list.append(key)


# add item(s) to char's inventory
def add_item(inventory, char):
    print (inventory[char])
    item_add = input('Item to add: ')
    if item_add == 'n':
        print ('Aborting add')
    else:
        # while loop to check if value is a number
        while True:
            try:
                item_add_number = int(input('Add amount:'))
                # if the key is already there, add to the value, if it isn't, create a new key and print char's inventory
                if item_add in inventory[char]:
                    inventory[char][item_add] += item_add_number
                else:
                    inventory[char][item_add] = item_add_number
                print (inventory[char])
                break
            except ValueError:
                print ('That\'s not a number')

# remove item(s) from char's inventory
def remove_item(inventory, char):
    print (inventory[char])
    remove_item = input('Item to remove: ')
    if remove_item == 'n':
        print ('Aborting remove')
    elif remove_item in inventory[char]:
        print ('Type in amount to remove or \'all\'')
        # while loop to check if remove_item_number is a number/all
        while True:
            remove_item_number = input('Remove amount: ')
            if remove_item_number == 'all':
                # remove all of item and print inventory of char
                del inventory[char][remove_item]
                print (inventory[char])
                break
            else:
                try:
                    remove_int = int(remove_item_number)
                    # if input is an integer, remove item(s) and print inventory of char
                    inventory[char][remove_item] -= remove_int
                    print (inventory[char])
                    break
                except ValueError:
                    if remove_item_number == 'all':
                        inventory[char].pop(remove_item, None)
                        break
                    else:
                        print ('That\'s not a number')
    else:
        print ('That item isn\'t in the inventory')







print ('Welcome to the Dungeons & Dragons inventory manager\n')
print ('Make sure to quit properly, so everything is saved. To quit, type in \'n\'\n')
# while loop that repeats entire program, ends with a message
while True:
    # just making sure that the inventory is equal to itself
    inventory = inventory
    print (character_list)
    char = input('Character to manage: ')
    if char == 'n':
        break
    elif char in inventory:
        while True:
            # add/remove/list inventory
            inpt = input('Type \'add\', \'remove\', or \'list\': ')
            if inpt == 'add':
                # add item(s) of character
                add_item(inventory, char)
                break
            elif inpt == 'remove':
                # if the person's inventory is empty, don't remove stuff
                if len(inventory[char]) == 0:
                    print (inventory[char])
                    print ('This list is empty. There is nothing to remove.')
                else:
                    # remove item(s) of character
                    remove_item(inventory, char)
                break
            elif inpt == 'list':
                # list inventory of char
                print (char + '\'s inventory:', inventory[char])
                break
            elif inpt == 'n':
                break
            else:
                print ('That\'s not an acceptable input.')
    else:
        print ('That person isn\'t in the list.')


#end of loop lines
print ('Pickling...')
pickle.dump(inventory, open('Dnd_Inventories.p', 'wb'))
print ('Pickling complete')
