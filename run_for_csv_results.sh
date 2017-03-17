if [ $# -eq 0 ]
        then
                dir=here_are_results
else
        dir=$1
fi
hive -hiveconf cwd=$PWD -hiveconf dir=$dir -f hive_script.hql