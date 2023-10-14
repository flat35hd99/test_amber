#!/bin/bash
#PBS -l ncpus=4:ngpus=1
#PBS -l walltime=00:10:00

# New cluster system
if [[ `hostname` == pbs* ]];
then
	module load amber/20_cuda11.7
	prefix=/home/users/wataru/research/test_amber
else
	module load cuda/11.7
	module load amber/xxx
	prefix=/home/users/dar/research/test_amber
fi


output=$prefix/output/$PBS_JOBID
mkdir -p $output

work=/lwork/users/$USER/$PBS_JOBID
cd $work

pmemd.cuda -O \
	-i $prefix/md.in \
	-p $prefix/RAMP1.prmtop \
	-c $prefix/RAMP1_eq7.rst7 \
	-ref $prefix/RAMP1_eq7.rst7 \
	-o RAMP1_md.mdout \
	-r RAMP1_md.rst7 \
	-x RAMP1_md.crd.nc \
	-frc RAMP1_md.force.nc

cp * $output


