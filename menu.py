import showindustries
import showcompanies


def showmenu():
    print("Choose:")
    print("(1) Show industries")
    print("(2) Show companies")


def choosetask():
    try:
        task = input("Selection?")
        task = str(task)
    except:
        print("\nInput not received")
    else:
        print("You picked: " + task)
        if task == "1":
            showindustries.show()
        elif task == "2":
            showcompanies.show()
        else:
            print("That is NOT a choice!")


showmenu()
choosetask()

