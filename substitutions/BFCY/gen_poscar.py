from itertools import permutations
from pymatgen import Structure
import pandas as pd
import numpy as np
import random


if __name__ == '__main__':

    grab = 10
    swap = ['Y', 'Fe', 'Co', 'Zr']
    rem = ['O']

    structure = Structure.from_file('POSCAR')
    coords = structure.frac_coords
    species = list(map(str, structure.species))

    df = pd.DataFrame(coords, columns=['x', 'y', 'z'])
    df['species'] = species

    keep = df[~df['species'].isin(swap+rem)]
    swap = df[df['species'].isin(swap)]
    rem = df[df['species'].isin(rem)]

    # Get unique list of swaps
    swap_perm = set(permutations(swap['species'], swap.shape[0]))

    # Remove once every cite
    rem_perm = []
    cond = np.array([True]*rem.shape[0])
    for i in range(rem.shape[0]):
        indx = cond.copy()
        indx[i] = False

        rem_perm.append(indx)

    # Get every combination of swaps and removals
    orders = []
    for i in swap_perm:
        new_swap = swap.copy()
        new_swap['species'] = i
        for j in rem_perm:
            pos = pd.concat([keep, new_swap, rem[j]])
            orders.append(pos)

    # Grab random subset
    random.shuffle(orders)
    positions = orders[:grab]

    for i in positions:
        print(i)

    #structure.to(filename='POSCAR')
