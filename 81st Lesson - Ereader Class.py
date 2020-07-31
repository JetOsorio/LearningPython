class Ereader():
    def __init__(self, make, model, backlight, battery, screen_type):
        #Initialize the attributes to describe an ereader
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type

    def get_ereader_name(self):
        #return a formatted descriptive name for our ereadername
        long_name = self.make + ' - ' +self.model + ' - ' + self.backlight + ' - ' + self.battery +' - ' + self.screen_type
        return long_name.title()


my_new_ereader = Ereader('Amazon kindle', 'paperwhite', 'adjustable backlight', 'several months of battery life ', '300 bpi')
print(my_new_ereader.get_ereader_name())