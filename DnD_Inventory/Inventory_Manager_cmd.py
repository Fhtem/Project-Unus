import cmd
import pickle
# set inventory equal to pickle file
inventory = pickle.load(open("Dnd_Inventories.p", "rb"))

def update_pickle():
    pickle.dump(inventory, open('Dnd_Inventories.p', 'wb'))

# creates list for do_names method
character_list = []
for key in inventory:
    character_list.append(key)

#cmd function that will be called at the end in a cmdloop
class CharacterSelect(cmd.Cmd):

    intro = 'Welcome to the Dungeons & Dragons inventory manager. Type \'help\' for a list of commands.'

    prompt = '> '

    def do_names(self):
        '''This prints a list of all current character options.'''
        print (character_list)

    def do_add(self, char):
        '''Adds items/currency to a person's inventory, in lowercase. If adding gear, just add 1 of the item.'''
        print (inventory[char])
        item_add = input('Item to add: ')
        # while loop to check if value is a number
        while True:
            try:
                item_add_number = int(input('Amount:'))
                break
            except ValueError:
                print ('That\'s not a number')
        # if the key is already there, add to the value, if it isn't, create a new key
        if item_add in inventory[char]:
            inventory[char][item_add] += item_add_number
        else:
            inventory[char][item_add] = item_add_number
        # update the pickle file
        update_pickle()

    def do_remove(self, char):
        '''Removes items/currency to a person's inventory. To remove all of an item, enter \'all\' for the amount.'''
        print (inventory[char])
        remove_item = input('Item to remove: ')
        remove_item_number = input('Amount: ')
        # while loop to check if value is a number/all
        while True:
            try:
                remove_item_number = input('Amount: ')
                remove_int = int(remove_item_number)
                # everything after this will execute if input is an integer
                inventory[char][remove_item] -= remove_item_number
                break
            except ValueError:
                if remove_item_number == 'all':
                    inventory[char].pop(remove_item, None)
                    break
                else:
                    print ('That\'s not a number')
        # update the pickle file
        update_pickle()
    def do_EOF(self, args):
        '''Quits the program.'''
        print ('Quitting')
        return True


if __name__ == '__main__':
    CharacterSelect().cmdloop()
