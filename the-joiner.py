# the joiner


import os
import pandas as pd

art1 = '''
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀█░█▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌                     ▐░▌    ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄            ▐░▌    ▐░▌       ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌           ▐░▌    ▐░▌       ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀            ▐░▌    ▐░▌       ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
     ▐░▌     ▐░▌       ▐░▌▐░▌                     ▐░▌    ▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌          ▐░▌     ▐░▌  
     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄█░▌    ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
      ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                                          
'''

art2 = '''
 ____                                                            __                                ___                             __                       
/\  _`\                                                         /\ \                              /\_ \                           /\ \                      
\ \ \/\ \    ___     ___      __          __  __     __     __  \ \ \___                      __  \//\ \    _ __    __     __     \_\ \  __  __             
 \ \ \ \ \  / __`\ /' _ `\  /'__`\       /\ \/\ \  /'__`\ /'__`\ \ \  _ `\                  /'__`\  \ \ \  /\`'__\/'__`\ /'__`\   /'_` \/\ \/\ \            
  \ \ \_\ \/\ \L\ \/\ \/\ \/\  __/  __   \ \ \_\ \/\  __//\ \L\.\_\ \ \ \ \  __  __  __    /\ \L\.\_ \_\ \_\ \ \//\  __//\ \L\.\_/\ \L\ \ \ \_\ \  __       
   \ \____/\ \____/\ \_\ \_\ \____\/\ \   \/`____ \ \____\ \__/.\_\\ \_\ \_\/\_\/\_\/\_\   \ \__/.\_\/\____\\ \_\\ \____\ \__/.\_\ \___,_\/`____ \/\_\      
    \/___/  \/___/  \/_/\/_/\/____/\ \/    `/___/> \/____/\/__/\/_/ \/_/\/_/\/_/\/_/\/_/    \/__/\/_/\/____/ \/_/ \/____/\/__/\/_/\/__,_ /`/___/> \/_/      
                                    \/        /\___/                                                                                         /\___/         
                                              \/__/                                                                                          \/__/          
'''

art3 = '''
                                   _                  
         /'                      /' `\                
       /'                      /'     )               
     /'__                    /' (___,/'____     ,____ 
   /'    )  /'    /        /'     )  /'    )   /'    )
 /'    /' /'    /'       /'      /'/(___,/'  /'    /' 
(___,/(__(___,/(__   (,/' (___,/' (________/'    /(__ 
            /'                                        
    /     /'                                          
   (___,/'                                            
'''

def process_csv_directory(directory_path, output_file):
    # Create an empty list to store the DataFrames
    df_list = []

    # Iterate through all the CSV files in the directory
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.csv'):
            # Read the CSV file into a Pandas DataFrame
            df = pd.read_csv(directory_path + '/' + file_name)

            # Add the DataFrame to the list
            df_list.append(df)

    # Concatenate the DataFrames into a single DataFrame
    master_df = pd.concat(df_list)

    # Save the master DataFrame to a CSV file
    master_df.to_csv(output_file, index=False)

def main():
    print(art1)
    # Get the directory path from the user
    directory_path = input('Enter the directory path: ')

    # Get the output file path from the user
    output_file = input('Enter the output file path: ')

    # Process the CSV files in the directory
    process_csv_directory(directory_path, output_file)
    print(art2)
    print(art3)
if __name__ == '__main__':
    main()
