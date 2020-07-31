class Ereader():
    def __init__(self, make, model, backlight, battery, screen_type):
        #Initialize the attributes to describe an ereader
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type
        self.library_count = 0

    def get_ereader_name(self):
        #return a formatted descriptive name for our ereadername
        long_name = self.make + ' - ' +self.model + ' - ' + self.backlight + ' - ' + self.battery +' - ' + self.screen_type
        return long_name.title()

    def read_library_count(self):
        if self.library_count != 1:
            print("You have " + str(self.library_count) + " books in your library")
        else:
            print("You have " + str(self.library_count) + " book in your library")

    def update_library_count(self, ebook_count):
        self.library_count = ebook_count

my_new_ereader = Ereader('Amazon kindle', 'paperwhite', 'adjustable backlight', 'several months of battery life ', '300 bpi')
print(my_new_ereader.get_ereader_name())
my_new_ereader.update_library_count(69)
my_new_ereader.read_library_count()