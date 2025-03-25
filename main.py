import ibbe
import sara
import mickus
import anton

def main():
    namn = input("Ange namn: ")
    food = input ("Ange mat")
    if namn == "ibbe":
        ibbe.hello()
    elif namn == "mickus":
        mickus.hello()
    elif namn == "anton":
        anton.hello()
    elif food == "anton":
        anton.food()
    elif food == "mickus":
        mickus.food()
    elif food == "ibbe":
        ibbe.food()
    elif food == "sara":
        sara.food()
    
    else:
        print("Okänt namn!")

main()
