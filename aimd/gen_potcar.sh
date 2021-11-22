#!/bin/bash

POTS=~/potentials/vasp/
REC=${POTS}vasp_pots.csv
COMP=$1

# Remove potcar if it exist
if [ -f ./POTCAR ]; then
        rm ./POTCAR
fi

# Generate POTCAR
for i in $(grep -Eo '[[:alpha:]]+' <<<${1}); do
        POT=$(grep ${i} ${REC} | grep yes)
        POT=$(echo ${POT} | awk -F "," '{print $2}')
        POT=$(find ${POTS} -type d -name ${POT} | grep pbe)
        cat ${POT}/POTCAR >> ./POTCAR
done
