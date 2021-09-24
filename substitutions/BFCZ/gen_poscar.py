from itertools import permutations
from pymatgen import Structure

import pandas as pd
import numpy as np
import random
import os


if __name__ == '__main__':

    swap = ['Y', 'Fe', 'Co', 'Zr']
    rem = ['O']
    rem_num = 3
    sample = 100

    structure = Structure.from_file('POSCAR')
    coords = structure.frac_coords
    species = list(map(str, structure.species))
    lattice = structure.lattice

    df = pd.DataFrame(coords, columns=['x', 'y', 'z'])
    df['species'] = species

    keep = df[~df['species'].isin(swap+rem)]
    swap = df[df['species'].isin(swap)]
    rem = df[df['species'].isin(rem)]

    # Get unique list of swaps
    swap_perm = set(permutations(swap['species'], swap.shape[0]))
    rem_perm = set(permutations(rem.index, rem_num))

    # Sample randomly
    swap_perm = random.sample(swap_perm, sample)
    rem_perm = random.sample(rem_perm, sample)

    # Get every combination of swaps and removals
    count = 0
    for i, j in zip(swap_perm, rem_perm):
        new_swap = swap.copy()
        new_swap['species'] = i
        new_rem = rem[~rem.index.isin(j)]
        pos = pd.concat([keep, new_swap, new_rem])
        pos.sort_values(by=['species'], inplace=True)

        structure = Structure(
                              lattice,
                              pos['species'],
                              pos[['x', 'y', 'z']].values
                              )

        os.makedirs('run_{}'.format(count), exist_ok=True)
        structure.to(filename='run_{}/POSCAR'.format(count))
        count += 1
