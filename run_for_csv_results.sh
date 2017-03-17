dir=$1
hive -hiveconf cwd=$PWD -hiveconf dir=$dir -f hive_script.hql