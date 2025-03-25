import ibbe
import sara
import mickus
import anton

def main():
    namn = input("Ange namn: ")
    if namn == "ibbe":
        ibbe.hello()
    elif namn == "mickus":
        mickus.hello()
    elif namn == "anton":
        anton.hello()
    else:
        print("Okänt namn!")

main()
