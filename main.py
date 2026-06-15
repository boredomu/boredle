# This program converts .CSV into a separate .JSON
import json
import builtins

# Settings
csv_path = r"./Heardle Data - CSV.csv"
json_export_path = r"./Heardle Data - JSON.json"
row_length = 4

# Variable declarations
single_quote = "'"
double_quote = "\""
delimiter = ","
single_space = " "
dash_with_space = "- "
read_permission = "r"
write_permission = "w"
encoding = "utf-8"
default_buffering = -1
last_char = -1
single_char_backwards = -1
row_number = 0
default_zero_value = 0
first_char = 0
single_increment = 1
second_char = 1
song_data = []
key_array = []

with open(csv_path, read_permission, default_buffering, encoding) as csv_file:
    current_line = csv_file.readline()

    # Get all the song info from a given row
    while current_line:
        string_list = current_line.split(delimiter)
        string_list_length = len(string_list)

        key_array_index = default_zero_value
        if row_number > default_zero_value:
            string_list_index = default_zero_value
            individual_song = {}
            multiple_artists = False

            # Take a look at all the parsed row strings
            while string_list_index < string_list_length:
                current_string = string_list[string_list_index].strip()
                
                # If there are multiple artists
                if current_string[first_char] == double_quote or multiple_artists:
                    if string_list_index == default_zero_value:
                        multiple_artists = True

                    individual_song[key_array[key_array_index]] = current_string[second_char:]
                    string_list_index += single_increment
                    current_string = string_list[string_list_index].strip()

                    last_character = current_string[last_char]
                    if last_character == double_quote:
                        multiple_artists = False
                        individual_song[key_array[key_array_index]] += delimiter + single_space + current_string[:last_char]
                        key_array_index += single_increment
                else:
                    dash_with_space_found = current_string.find(dash_with_space)
                    if dash_with_space_found > default_zero_value:
                        current_string = current_string[:(dash_with_space_found + single_char_backwards)]

                    individual_song[key_array[key_array_index]] = current_string
                    key_array_index += single_increment

                string_list_index += single_increment
            song_data.append(individual_song)
        else:
            # This branch is only reached for the very first row of the CSV file
            while key_array_index < row_length:
                current_string = string_list[key_array_index].strip()
                key_array.append(current_string)

                key_array_index += single_increment
        
        current_line = csv_file.readline()
        row_number += single_increment

with open(json_export_path, write_permission) as json_file:
    song_data = json.dumps(song_data)
    json_file.write(song_data)