# Part B: Shopping List Manager

shopping_list = []

while True:
    choice = input("\nMenu - Type 'add', 'remove', 'show', or 'done': ").strip().lower()
    
    if choice == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' has been added to your list.")
        
    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your list.")
        else:
            print("That item is not on your list.")
            
    elif choice == "show":
        print("\n--- Current Shopping List ---")
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for item in shopping_list:
                print(f"- {item}")
        print("-----------------------------")
        
    elif choice == "done":
        print("Goodbye! Happy shopping!")
        break
        
    else:
        print("Invalid choice. Please choose 'add', 'remove', 'show', or 'done'.")
