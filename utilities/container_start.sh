#!/bin/bash

serviceCount=$(docker service ls | grep ${4}_web | awk '{print $4}' | cut -d / -f 1)
if [[ ${serviceCount} = "0" ]]
then
    echo "service stopped, restarting ... "
    docker service scale ${4}_db=1 ${4}_web=1
    echo "True"
else
    echo "no service"
    user_path="/${2}"
    instance_path="/${3}/${4}"
    final_path="${1}${user_path}${instance_path}"

    docker stack deploy -c ${final_path}/docker-compose.yaml ${4}

    retry_time=50
    iter_no=0
    state=$(docker service ps ${4}_web | awk '{print $6}' | sed -n '2p')

    while [[ ${state} != "Running" && ${iter_no} -lt ${retry_time} ]]
    do
        state=$(docker service ps ${4}_web | awk '{print $6}' | sed -n '2p')  
        sleep 0.5
        iter_no=`expr ${iter_no} + 1`
    done

    if [[ ${iter_no} -gt ${retry_time} ]]
    then
        echo "False"
    else
        echo "True"
    fi
fi


