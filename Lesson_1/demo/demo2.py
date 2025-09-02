DRINKS: list[str] = ["latte", "cappuccino", "espresso", "americano"]

def order_prompt() -> str:
    print("What would you like to order?\n")
    for i, drink in enumerate(DRINKS):
        print(f"{i + 1}. {drink}")

    while True:
        order_num: int = int(input("Please enter a number: "))
        if order_num in range(1, len(DRINKS) + 1):
            break
        else:
            print("\nInvalid choice, please try again.")

    order: str = DRINKS[order_num - 1]

    match order_num:
        case 1 | 2 | 3:
            order += add_whipped_cream()
        case 4:
            raise ValueError("\nYou can't order an americano, we're sold out!")
    
    return order

def add_whipped_cream() -> str: 
    answer: str = input("Would you like whipped cream? (y/n): ")

    return " with whipped cream" if answer == "y" else ""

def order_complete_prompt() -> str:
    return input("Is your order complete? (y/n): ")

if __name__ == '__main__':
    full_order: list[str] = []

    order_complete: bool = False
    while not order_complete:
        try:
            order: str = order_prompt()
        except ValueError as e:
            print(e)
        else:
            print(f"\nYou ordered a {order}")
            full_order.append(order)

        if order_complete_prompt() == "y":      
            order_complete: bool = True

    if len(full_order) > 0:
        print(f"\nYou ordered: {', '.join(full_order)}")
    else:
        print("\n... you didn't order anything.")