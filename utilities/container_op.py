#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os
import commands

def start_container(base_path, username, domain_model_name, file_id):
    """
    Start containers
    """
    cmd = "bash ./utilities/container_start.sh {} {} {} {}".format(base_path, username, domain_model_name, file_id)
    _code,output = commands.getstatusoutput(cmd)
    print(output)
    status = output.split("\n")[-1]
    if status == "False":
        return False
    else:
        return True

def stop_container(base_path, username, domain_model_name, file_id):
    """
    Stop containers
    """
    cmd = "bash ./utilities/container_stop.sh {} {} {} {}".format(base_path, username, domain_model_name, file_id)
    _code,output = commands.getstatusoutput(cmd)
    print(output)
    status = output.split("\n")[-1]
    if status == "False":
        return False
    else:
        return True

def delete_container(file_id):
    cmd = "bash ./utilities/container_delete.sh {}".format(file_id)
    _code,output = commands.getstatusoutput(cmd)
    print(output)
    return



        

