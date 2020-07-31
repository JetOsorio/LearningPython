import ereader_class

my_bw_ereader = ereader_class.Ereader('amazon', 'paperweight', 'adjustable backlight', 'several months of battery life', '300 bpi')
print(my_bw_ereader.get_ereader_name())

my_colour_ereader = ereader_class.Kindlefire('amazon', 'kindle fire', 'colour screen', '12 hours of battery', '1280 * 800')
print(my_colour_ereader.get_ereader_name())