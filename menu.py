import showindustries
import showcompanies
import calculations
import simplecalc


def showmenu():
    print("Choose:")
    print("(1) Show industries")
    print("(2) Show companies")
    # print("(3) Calculate company value")
    print("(3) Calculate company value (for 7 years)")


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
        elif task == "3":
            # print(calculations.future_compounded_asset_amount(years))
            print(calculations.future_compounded_asset_amount())
            # print(simplecalc.maincalc())
        else:
            print("That is NOT a choice!")


showmenu()
choosetask()

