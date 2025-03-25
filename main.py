import ibbe
import sara
import mickus
import anton

def handle_name(namn):
    if namn == "ibbe":
        ibbe.hello()
    elif namn == "mickus":
        mickus.hello()
    elif namn == "anton":
        anton.hello()
    elif namn == "sara":
        sara.hello()
    else:
        print("Okänt namn!")

def handle_food(namn):
    if namn == "ibbe":
        ibbe.food()
    elif namn == "mickus":
        mickus.food()
    elif namn == "anton":
        anton.food()
    elif namn == "sara":
        sara.food()
    else:
        print("Ingen matinfo tillgänglig för detta namn.")

def handle_drink(namn):
    if namn == "ibbe":
        ibbe.drink()
    elif namn == "mickus":
        mickus.drink()
    elif namn == "anton":
        anton.drink()
    elif namn == "sara":
        sara.drink()
    else:
        print("Ingen dryckesinfo tillgänglig för detta namn.")

def main():
    namn = input("Ange namn: ").lower()
    handle_name(namn)
    handle_food(namn)
    handle_drink(namn)

main()

