from tkinter import Tk, Label
from PIL import Image, ImageTk

def main():
#Welcome to story time!
#this program will tell a bedtime story based on the choices of the narrator
#the answer must be written in lower case for the program to go on 
    potion_ingredients = ["bat wings", "mandrake", "vervain", "milk", "owl feathers"]
    root = Tk()
    root.title("Image Display")
    # Load the image at the beginning of the adventure using PIL
    image = Image.open("avventura.jpg")
    photo = ImageTk.PhotoImage(image)
    # Create a label to hold the image
    label = Label(root, image=photo)
    label.pack()
    # Run the application
    root.mainloop()

    #start the adventure
    print("Good morning adventurer! Let's start this adventure!") 
    name = input("What's your name? ")
    print(greet(name))
    #choose the protagonist of the story
    protagonist = input("Who do you want to be today: a witch or a soldier? ")
    #tell the story of the witch
    if protagonist =="witch":
       print("Great choice! Ready to obtain magic powers?")
       magic_power = input("What can you do: heal or fly? ")
       if magic_power == "heal":
           print("Let's gather all the ingredients for our magic healing potion, then!")
           make_potion(potion_ingredients)
           #display image of the potion
           root = Tk()
           root.title("Image Display")
           image = Image.open("pozione.jpg")
           photo = ImageTk.PhotoImage(image)
           label = Label(root, image=photo)
           label.pack()
           root.mainloop()
           input()
           print("There is a lost prince in the forest.. He fought with a creature of the night and he's wounded. You heal him with your powers and he grants you a part of the kingdom.")
       else: 
           input("You fly high over the kingdom, but suddendly you spot something... Smoke.. Fire!!!")
           print("The forest is on fire and needs to be saved. You fly over the fire and help the citizens of the kindgom to save the realm. They start calling you The Good Witch.")
    #tell the story of the soldier
    else:
       print("Great choice! Ready to fight with some monsters?")
       monster = input("A creature is coming towards you... What is it: a dragon or a sea-monster? ")
       if monster == "dragon":
          print(fight(monster))
          input()
          print("Careful dear soldier! Dragons are smart and fiery creatures.. He spits fire at you, but you manage to survive.")
       else:
          print(fight(monster))
          input()
          print("The sea-monster tries to drag you into the ocean, you manage to escape with the help of a mermaid.")
    input("Not bad for a first time adventurer... Now get your reward!")
    root = Tk()
    root.title("Image Display")
    # Load the image at the end of the adventure using PIL
    image = Image.open("sfondo3.jpg")
    photo = ImageTk.PhotoImage(image)
    # Create a label to hold the image
    label = Label(root, image=photo)
    label.pack()
    # Run the application
    root.mainloop()
    input()
    print("You didn't think it was an actual reward, did you?")
    print("See you at the next bedtime story!")
    
        
def make_potion(potion_ingredients):
    for element in potion_ingredients:
        print(element)

def greet(name):
    return "Welcome, intrepid" + " "+ str(name)+ "!"

def fight(monster):
    return "You punch the " + monster + "!"



if __name__ == "__main__":
    main()