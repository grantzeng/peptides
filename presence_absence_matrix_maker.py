#!/usr/bin/env python3

import pandas as pd

def generate_presence_absence_matrix(data):

    df = pd.read_excel(data)

    #
    #   Make the matrix/dataframe to populate with presence/absence
    #

    locations = df.columns[2:].tolist()
    peptides = df['Peptide ID'].unique().tolist()
    presence_absence_matrix = pd.DataFrame(0, index=peptides, columns=locations)

    #
    #   Populate presence absence matrix
    #

    # - This may break since column/location name is hard coded here
    df = df.loc[:, 'T29':]

    # Loop through adjacency list to populate adjacency matrix
    for location in df.columns:
        print(f'Looking at {location}: ', end='')

        for peptide in df[location]:
            if pd.isna(peptide):
                continue

            print(f'{peptide} ', end='')

            # Change this to += 1 if you want counts
            presence_absence_matrix[location][peptide] = 1

        print('\n\n')


    with pd.ExcelWriter('output.xlsx', mode='w+') as writer:
        presence_absence_matrix.to_excel(writer)

if __name__ == '__main__':
    generate_presence_absence_matrix('test_peptide_grant.xlsx')