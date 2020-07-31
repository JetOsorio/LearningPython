class Ereader():
    def __init__(self, make, model, backlight, battery, screen_type):
        # Initialize the attributes to describe an ereader
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type
        self.library_count = 0

    def get_ereader_name(self):
        # return a formatted descriptive name for our ereadername
        long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
        return long_name.title()

    def read_library_count(self):
        if self.library_count != 1:
            print("You have " + str(self.library_count) + " books in your library")
        else:
            print("You have " + str(self.library_count) + " book in your library")

    def update_library_count(self, ebook_count):
        self.library_count = ebook_count

    def increment_library_count(self, purchased_ebooks):
        # Adds new ebooks to library count
        self.library_count += purchased_ebooks

class Screen():
    #Create a class to model the screen of a kindle fire
    def __init__(self, screen_resolution = '1280 * 800'):
        #Initialise te screen's attributes
        self.screen_resolution = screen_resolution

    def describe_screen(self):
        # Print out some marketing text about Kindle Fire
        print("\nFire HD 8 features a widescreen " + self.screen_resolution + " HD screen")

# Child Class
class Kindlefire(Ereader):
    # Represents aspects of an ereader specific to a Kindle Fire.
    # Then initialise attributes specific to a kindle fire.

    def __init__(self, make, model, backlight, battery, screen_type):
        # initialise attributes for the kindle fire

        super().__init__(make, model, backlight, battery, screen_type)
        # 'super' function helps python make connection between parent and child classes
        # Tells Python to call 'init' method from parent class, which allows it to use all attributes in parent class
        self.firescreen = Screen() #tells python to create new instance
