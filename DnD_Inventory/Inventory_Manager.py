import pickle


class Inventory(object):
    # init function
    def __init__(self, inventory_file):
        self.inventory_file = inventory_file
        self.character_list = []
        self.inventory = pickle.load(open(self.inventory_file, "rb"))
        # appends names for character_list
        for key in self.inventory:
            self.character_list.append(key)
    #inventory = {"amanda" : {}, "neo" : {}, "kari" : {}, "kade" : {}, "storm" : {}, "emily" : {}, "jacob" : {}, "keegan" : {}}


    # add item(s) to char's inventory, sub method of manage_inv
    def add_item(self, inventory, char):
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

    # remove item(s) from char's inventory, sub method of manage_inv
    def remove_item(self, inventory, char):
        print (inventory[char])
        while True:
            remove_item = input('Item to remove: ')
            if remove_item == 'n':
                print ('Aborting remove')
                break
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
                break
            else:
                print ('That item isn\'t in the inventory')

    # while loop that repeats entire program, ends with a message
    def manage_inv(self):
        print ('Welcome to the Dungeons & Dragons inventory manager\n')
        print ('Make sure to quit properly, so everything is saved. To quit, type in \'n\'\n')

        while True:
            # just making sure that the inventory is equal to itself
            inventory = pickle.load(open(self.inventory_file, "rb"))
            print (self.character_list)
            char = input('Character to manage: ')
            if char == 'n':
                break
            elif char in inventory:
                while True:
                    # add/remove/list inventory
                    inpt = input('Type \'add\', \'remove\', or \'list\': ')
                    if inpt == 'add':
                        # add item(s) of character
                        self.add_item(inventory, char)
                        pickle.dump(inventory, open(self.inventory_file, 'wb'))
                        break
                    elif inpt == 'remove':
                        # if the person's inventory is empty, don't remove stuff
                        if len(inventory[char]) == 0:
                            print (inventory[char])
                            print ('This list is empty. There is nothing to remove.')
                        else:
                            # remove item(s) of character
                            self.remove_item(inventory, char)
                            pickle.dump(inventory, open(self.inventory_file, 'wb'))
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

    # only use this when first pickling a file or adding characters
    def manage_chars(self):
        # loop to add/remove characters
        while True:

            print (self.character_list)

            inpt = input('\'add\' or \'remove\' a char: ')
            if inpt == 'add':
                char = input('Character to add: ')
                if char == 'n':
                    pass
                else:
                    self.inventory[char] = {}
            elif inpt == 'remove':
                if inpt in self.inventory:
                    del self.inventory[char]
                else:
                    print ('That person isn\'t in the list')
            elif inpt == 'n':
                break
            else:
                print ('\'%s\' isn\'t an acceptable entry' % (inpt))
        pickle.dump(inventory, open(self.inventory_file, 'wb'))



eggcellentbros = Inventory('eggcellent_bros_inv.p')
faggotrons = Inventory('faggotrons_inv.p')

faggotrons.manage_chars()
