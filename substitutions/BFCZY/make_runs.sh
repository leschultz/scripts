#!/bin/bash

python3 gen_poscar.py

for i in $(find . -type d -name 'run_*'); do

	cp KPOINTS ${i}
	cp POTCAR ${i}
	cp INCAR ${i}
done
