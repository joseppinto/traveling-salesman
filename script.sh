module load matlab/9.2.0
cd ~/tp1-algp/

string=""

for n_nodes in 4 8 16 32 64 128 256 512 1024 2000
do
	for n_procs in 1 2 4 #8 16
	do
		string="${string}disp('${n_nodes}, ${n_procs}');travelingMain(${n_nodes}, ${n_procs});"	
	done
done

matlab -nodisplay -nosplash -nodesktop -r "cd('src/traveling_salesman/');${string}exit;" > out/output.txt
python transform_output.py out/output.txt out/output.csv
