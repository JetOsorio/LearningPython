file_path = 'C:/Users/User/PycharmProjects/Learning/text-files/copy_of_movies'

with open(file_path) as file_object: #'open' function needs name of file to open and looks for file in directory
    contents = file_object.read()
    print(contents.strip())
    #automatically closes file when access is no longer required
