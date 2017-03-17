if [ $# -eq 0 ]
	then
		dir='results_in_here'
else
	dir=$1
fi
hive -hiveconf cwd=$PWD -hiveconf dir=$dir -f hive_script.hql