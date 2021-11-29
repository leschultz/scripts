#!/bin/bash

COMP=$1

echo "Making POSCAR for ${COMP}"
python3 ~/scripts/random_cell/gen_poscar.py ${COMP}

echo "Making PBE POTCAR for ${COMP}"
bash ~/scripts/random_cell/gen_potcar.sh ${COMP}
