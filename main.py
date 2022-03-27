# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from week0.animations import woot
from week0.animations import skater
from week0 import swap
from week0 import tree
from week0 import matrix
from week1 import listprin
from week1 import fibonacci
from week2 import factorial
from week2 import mathfunction

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = []

week0_sub_menu = [
  ["Swap", swap.test_swap],
  ["Tree", tree.treefunc],
  ["Matrix", matrix.format_tester],
  ["Woot", woot.boathouse],
  ["Skater", skater.skating],
]

week1_sub_menu = [
  ["List", listprin.tester],
  ["Fiboancci", fibonacci.fibonacci_results],
]

week2_sub_menu = [
  ["Factorial", factorial.testee],
  ["Prime Math", mathfunction.test_prime],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0", week0_submenu])
    menu_list.append(["Week 1", week1_submenu])
    menu_list.append(["Week 2", week2_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def week0_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, week0_sub_menu)
def week1_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, week1_sub_menu)
def week2_submenu():
  title = "Function Submenu" + banner
  buildMenu(title, week2_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except ValueError:
          print(f"Not a number: {choice}")
        # traps all other errors
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again



if __name__ == "__main__":
    menu()
