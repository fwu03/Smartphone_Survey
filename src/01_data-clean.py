# coding: utf-8

# 01_data-clean.ipynb
#
# TEAM: Fan Wu, Bailey Lei, Makkaoui Mohamad
# DATE: April 3, 2019
#
# PURPOSE: The script takes a raw smartphone dataset and generates a clean dataset through cleaning
#          the unnecessary data, renaming dataset headers, and modifying data types.
#
# INPUT:
#     - Raw Dataset: "smartphone.csv"
#
# OUTPUT:
#     - Clean Dataset: "smartphone_clean.csv"
#
# ARGUMENTS:
#     ARG1 = input file path
#     ARG2 = output file path
#
# USAGE: "python src/01_data-clean.py data/smartphone.csv data/smartphone_clean.csv"

import sys
import pandas as pd

def main():

    '''main function: grab the arg1 and arg2 as input file path and output file path'''

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    data_wrangling(input_file, output_file)

def data_wrangling(input_file, output_file):

    '''data_wrangling function takes two arguments (i.e. input_file path and output_file path),
       and generate a clean dataset'''

    #import raw dataset
    df = pd.read_csv(input_file)


    #drop unnecessary data
    drop_columns = ['Internal ID', 'First name', 'Last name', 'Email', 'Status', 'Do you own a smartphone?', 'Do you own a personal computer/laptop?']
    for col in drop_columns:
        df.drop(col, axis=1, inplace=True)

    #rename the dataframe columns
    rename_columns = {'What smartphone operating system/platform do you have?': 'smartphone_OS',
                      'What is your level of satisfaction using your current phone/phone OS?': 'num_smartphone_OS',
                      'How long ago did you purchase your current phone (years ago)?': 'smartphone_OS_years',
                      'What was your previous smartphone platform?': 'pre_smartphone_OS',
                      'If you were to purchase a smartphone today, what OS will be running on it?': 'future_smartphone_OS',
                      'What is the most common smartphone OS among your family members?': 'family_smartphone_OS',
                      'Whats the most common smartphone OS among your friend group?': 'friend_smartphone_OS',
                      'What operating system is running on your PC?': 'PC_OS',
                      'What is your level of satisfaction using your current laptop?': 'num_PC_OS',
                      'How long ago did you purchase your current PC (years ago)?': 'PC_OS_years',
                      'If you were to purchase a laptop today, what operating system will be running it?': 'future_PC_OS',
                      'What laptop operating system is used/required at your place of employment/study?': 'workplace_PC_OS'}

    df = df.rename(index=str, columns=rename_columns)

    #modify the data type
    df.smartphone_OS_years = df.smartphone_OS_years.str[:1]
    df["smartphone_OS_years"] = pd.to_numeric(df["smartphone_OS_years"])

    df.PC_OS_years = df.PC_OS_years.str[:1]
    df["PC_OS_years"] = pd.to_numeric(df["PC_OS_years"])

    #Output the dataframe to csv file
    df.to_csv(output_file, index=False)


#call main function
if __name__ == '__main__':
    main()
