#!/bin/bash

COMP=$1

echo "Making POSCAR for ${COMP}"
python3 $(pwd)/gen_poscar.py ${COMP}

echo "Making PBE POTCAR for ${COMP}"
bash $(pwd)/gen_potcar.sh ${COMP}
