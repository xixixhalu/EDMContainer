#!/bin/bash

m1=$(docker service update --replicas 0 ${4}_web)
m2=$(docker service update --replicas 0 ${4}_db)

sleep 5

serviceCount=$(docker service ls | grep ${4}_web | awk '{print $4}' | cut -d / -f 1)
if [[ ${serviceCount} = "0" ]]
then
    echo "Successful to stop the specified instance"
    echo "True"
else
    echo "Failed to stop the specified instance"
    echo "False"
fi