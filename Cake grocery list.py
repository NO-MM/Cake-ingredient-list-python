# Cake grocery list organized by category
cake_grocery_list = {
    "Dry Ingredients": ["flour", "sugar", "baking powder", "salt"],
    "Wet Ingredients": ["eggs", "milk", "vannilla extract", "vegetable oil"],
    "Toppings": ["chocolate chips", "nuts", "sprinkles", "fruit"],
    "Frosting Ingredients": ["butter", "powdered sugar", "cream cheese", "cocoa powder"]
}

# Interactive loop
while True:
    print("\nChoose an action:")
    print("1. Add ingredient")
    print("2. Remove ingredient")
    print("3. Show grocery list")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        category = input("Enter category name: ")
        ingredient = input("Enter ingredient to add: ")    
    

        #Add ingredient using dictionary and list
        if category in cake_grocery_list:
            if ingredient not in cake_grocery_list[category]:
                cake_grocery_list[category].append(ingredient)
                print(f"☑ Added '{ingredient}' to '{category}'")
            else:
                print(f"ℹ '{ingredient}' already exist in '{category}'")
        
        else:
            cake_grocery_list[category] = [ingredient]
            print(f"🆕 Created category '{category}' and added '{ingredient}'")

    elif choice == "2":
        category = input("Enter category name: ")
        ingredient = input("Enter ingredient to remove: ")
    
        # Remove ingredient using dictionary and list
        if category in cake_grocery_list:
            if ingredient in cake_grocery_list[category]:
                cake_grocery_list[category].remove(ingredient)
                print(f"🗑 Removed '{ingredient}' from '{category}'")
                if len(cake_grocery_list[category]) == 0:
                    del cake_grocery_list[category]
                    print(f"🚫 Removed empty category '{category}'")
            else:
                print(f"⚠ Ingredient'{ingredient}' not found in '{category}'")
        else:
            print(f"⚠ Category '{category}' does not exist.")
        
    elif choice == "3":
        print("\n🍰 Cake Grocery List 🍰")
        for category in cake_grocery_list:
            print(f"\n 📁 {category}:")
            print("-------------")
            for item in cake_grocery_list[category]:
                print(f" 🧁 {item}")
                
    elif choice == "4":
        print("😋Happy Baking!😋")
        break
    
    else:
        print("❌ Invalid choice. Please enter 1,2,3, or 4.")
