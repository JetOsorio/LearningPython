from ereader_class import * #Least preffered method bcause it is harder to know where error would come from

my_bw_ereader = Ereader('amazon', 'paperweight', 'adjustable backlight', 'several months of battery life', '300 bpi')
print(my_bw_ereader.get_ereader_name())

my_colour_ereader = Kindlefire('amazon', 'kindle fire', 'colour screen', '12 hours of battery', '1280 * 800')
print(my_colour_ereader.get_ereader_name())