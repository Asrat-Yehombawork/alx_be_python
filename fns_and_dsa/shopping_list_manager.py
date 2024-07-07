 
def add_items(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_items(shopping_list):
    item = input('Enter the item name to be removed:')
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item} has being removed'")
    else: print('item does not exist ')

def view_list(shopping_list):
    if not shopping_list:
        print("The shopping list is currently empty.")
    else:
        print("Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")    

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            return add_items(shopping_list)
             
        elif choice == '2':
           return remove_items(shopping_list)
        
        elif choice == '3':
           return view_list(shopping_list)
             
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()      