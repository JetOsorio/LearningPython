from ereader_class import Kindlefire

my_kindle_fire = Kindlefire('Amazon', 'kindle fire', 'colour screen', '12 hour battery life', '1280 * 800' )
print(my_kindle_fire.get_ereader_name())

my_kindle_fire.firescreen.describe_screen()