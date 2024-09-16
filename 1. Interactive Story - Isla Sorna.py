print('''
*******************************************************************************
                                 <\               _
                                  \ \          _/{
                           _       \ \       _-   -_
                         /{        / `\   _-     - -_
                       _~  =      ( @  \ -        -  -_
                     _- -   ~-_   \( =\ \           -  -_
                   _~  -       ~_ | 1 :\ \      _-~-_ -  -_
                 _-   -          ~  |V: \ \  _-~     ~-_-  -_
              _-~   -            /  | :  \ \            ~-_- -_
           _-~    -   _.._      {   | : _-``               ~- _-_
        _-~   -__..--~    ~-_  {   : \:}
      =~__.--~~              ~-_\  :  /
                                 \ : /__
                                //`Y'--
                               <+    -  \ 
*******************************************************************************
''')
print("Welcome to Isla Sorna.")
print("Your mission is to find the missing little boy.")
print("You stepped out of the airplane and you hear a lady speaking through a megaphone")

initial_direction = input("Would you like to go left and ignore her or go right and follow her?\nType left or right:\n").lower()

if initial_direction == "left":
    print("You ignore the woman and continue along the path until you come upon a river.")
    swim_or_wait = input("Do you wish to swim or do you want to wait for the boat to come?\nType swim or wait:\n").lower()
    if swim_or_wait == "wait":
        print("A boat comes and takes you safely across the shore and you land in front of an overturned supply truck. "
              "You wonder what is inside of it.")
        bunker_or_no_bunker = input("Do you open the truck or ignore the truck?\nType truck or no truck:\n").lower()
        if bunker_or_no_bunker == "truck":
            print("You open the truck and find the missing child.\n"
                  "Suddenly you hear the Spinosaurus coming and the ground is shaking.")
            stay_coast_inland = input("Do you stay in the truck, run to the coast or head inland?\n"
                                      "Type stay, coast or inland:\n").lower()
            if stay_coast_inland == "inland":
                print("You both head inland, reuniting with your group. "
                      "After an exciting adventure, US Marines come and save your team.\n"
                      "You sit on the helicopter and watch the Pteradactyls fly by.\nYOU WIN!")
            elif stay_coast_inland == "coast":
                print("You both head to the coast but are accosted by a large group of Compsognathus.\n"
                      "You are both eaten alive\nGAME OVER!")
            elif stay_coast_inland == "stay":
                print("You stayed really still and the Spinosaurus went by safely.\nYou wait a few minutes and leave. "
                      "Reuniting with the remaining members of your group you come across an aviary.")
                enter_or_nah = input("Do you enter the aviary or do you stay outside\nType inside or outside:\n").lower()
                if enter_or_nah == "inside":
                    print("You go inside and had a wonderful adventure avoiding Pteradactyls and got to safety.\n"
                          "US Marines come and save your team. "
                          "You sit on the helicopter and watch the Pteradactyles fly by.\nYOU WIN!")
                else:
                    print("You stay outside and go around the aviary. "
                          "All looked well until your team came across a T-rex and a Spinosaurus fighting.\n"
                          "They stop fighting to devour your team.\nGAME OVER!")
            else:
                print("You left the truck but stayed around the area and the Spinosaurus located your scent. "
                      "He ate you both.\nGAME OVER!")
        else:
            print("You decided not to open the truck. The boy runs out of food and dies.\nGAME OVER!")
    else:
        print("You decide to swim. The Mosasaurus comes and eats you and your entire party.\nGAME OVER!")
else:
    print("You follow the woman with the megaphone. The Spinosaurus Rex comes out and eats your entire party.\nGAME OVER!")