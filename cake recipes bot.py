import time

def greet_user():
    print("Welcome to CakeBot! 🧁")
    time.sleep(2)
    print("I can help you find cake ingredients and recipes.")
    time.sleep(2)
    
def ask_cake_type():
    cake_type = input("What kind of cake are you interested in? (e.g., chocolate cake, vanilla cake): ").strip().lower()
    return cake_type

def get_recipe(cake_type):
    recipes = {
        "chocolate cake": {
            "ingredients": ["2 cups flour", "1 cup cocoa powder", "1.5 cups sugar", "2 eggs", "1 cup milk"],
            "steps": ["Preheat oven to 180 C", "Mix dry ingredients", "Add eggs and milk", "Bake for 30 minutes"]
        },
        "vanilla cake":{
            "ingredients": ["2 cups flour", "1 cup sugar", "2 eggs", "1 cup milk", "1 tbsp vanilla extract"],
            "steps": ["Preheat oven to 180 C", "Mix dry ingredients", "Add eggs, milk, and vanilla", "Bake for 25 minutes"]
        }
    }
    return recipes.get(cake_type, None)

def show_recipe(recipe):
    print("\nIngredients:")
    for item in recipe["ingredients"]:
        print(f"🍰 {item}")
    print("\nSteps:")
    for step in recipe["steps"]:
        print(f"- {step}")
        
def sign_up():
    email = input("\nWould you like to sign up for the lates cake recipes? Enter your email: ").strip()
    print(f"Thank you! We'll send new recipes to {email} 🧁")
    
def main():
    greet_user()
    cake_type = ask_cake_type()
    recipe = get_recipe(cake_type)
    if recipe:
        show_recipe(recipe)
    else:
        print("Sorry, I don't have that recipe yet.")
    sign_up()
    
if __name__ == "__main__":
    main()