#Problem Statement: Merchant's Guide to Galaxy

romanvalues = {"i": 1,"v": 5,"x": 10,"l": 50,"c": 100,"d": 500,"m": 1000} #Dictionary for mapping roman numbers to their values

intergalactic_values = {} #Dictionary for mapping intergalactic names to values (eg. glob,prok etc)

metals = {} #Dictionary for mapping earth metals to their values (eg. Gold,Silver)


def display(s): #Function to print out results
    print(s)


def galactic_to_numeric(word): #It converts galactic and roman values to numeric values.

    value = 0 #
    try: #Error Handling
        romanchar = [intergalactic_values[i] for i in word]
    except:
        return -1

    while romanchar:
        d = romanchar.pop(0)
        if romanchar and romanchar[0] > d:
            value -= d #If the roman number is followed by a larger roman number
        else:
            value += d

    return value


def processing_input(line):
    word = line.lower().split()

    if not word:
        return display("No Input Given")

    #Handling Input where eg. "glob is I"
    if len(word) == 3 and word[1] == "is":
        key = word[0]
        val = word[2]


        if not val in romanvalues:
            return display("Not a Valid digit")
        intergalactic_values[key] = romanvalues[val]
        return

    #Handling inputs where for eg. "glob glob Silver is 34 credits"
    if len(word) > 4 and word[-1] == "credits" and word[-3] == "is":
        word.pop() #Removes the last word ("credits")
        try:
            val = float(word[-1]) # Converts the String["34"] to float [34.00]
        except:
            return display("'%s' is not a valid numeric value" % word[-1]) #Error Handling if the second last word is not a number

        word.pop()
        word.pop()
        metal = word.pop() #Storing the metal name
        n = galactic_to_numeric(word)

        if n < 0:
            return display("That's not a valid Galactic number")

        metals[metal] = val / n
        return

    #Handling the input where "how much is .....?"
    if word[0:3] == ["how", "much", "is"]:
        word = word[3:]
        if word[-1] == "?":
            word.pop()

        n = galactic_to_numeric(word)
        if n < 0:
            return display("Not a valid Galactic number")

        print(" ".join(word), "is", n) # Displaying output
        return

    #Handling the input where "how many credits is.......?"
    if word[0:4] == ["how", "many", "credits", "is"]:
        word = word[4:] #Removes ["how", "many", "credits", "is"] from the word list
        if word[-1] == "?":
            word.pop()

        metal = word.pop()
        if metal not in metals: #If metal is not present it will handle the error
            return display("I don't know of the trading good")

        n = galactic_to_numeric(word)
        if n < 0:
            return display("Not a valid Galactic Number")

        print(" ".join(word), metal, "is", int(n * metals[metal]), "Credits") #Display Output
        return

    return display("I have no idea what you are talking about")

print("--------------------------------------WELCOME TO INTERGALACTIC CONVERSION PROGRAM--------------------------------------")
print("You are one of the remaining trader left. To continue further you must input all the galactic units you want to convert")

#Taking Input from the user
count = int(input("How many galactic inputs do you want to enter ?:"))


for i in range(0,count):
        processing_input(input())


count1 = int(input("How many galactic queries do you want to ask ?:"))
for i in range(0,count1):
        processing_input(input())

print("Thanking for using this program. Have fun Trading !!!!!")

