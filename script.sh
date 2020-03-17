module load matlab/9.2.0
cd ~/tp1-algp/

string=""

for n_nodes in 4 8 16 32 64 128 256 512 1024 2048 4096 8192 
do
	for n_procs in 8
	do
		for area in 10 100 1000
		do
			for circle in true false
			do
				string="${string}disp('${n_nodes}, ${n_procs}, ${area}, ${circle}');travelingMain(${n_nodes}, ${n_procs}, ${area}, ${circle});"	
			done
		done
	done
done

matlab -nodisplay -nosplash -nodesktop -r "cd('src/traveling_salesman/');${string}exit;" > out/output.txt
python transform_output.py out/output.txt out/output.csv
