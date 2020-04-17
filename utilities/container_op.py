#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import urllib2
import os
import commands
import time
from database_manager.dbOps import dbOps
from database_manager.setup import mgInstance

# URL of Nginx server
params_tmpl = "?user_name=%s&project_name=%s&instance_id=%s"


def upload_code(user_name, project_name, instance_id):
    """
    Upload code AND build image
    Create repo user -> create repo -> push code -> build image
    Pass request to LB to choose a worker (in build_image process)
    """
    command = 'sh /root/workspace/EDM/utilities/auto_repo.sh ' + user_name + ' ' + project_name + ' ' + instance_id
    print('upload_code: ' + command)
    os.system(command)


def start_container(base_path, username, domain_model_name, file_id):
    """
    Start containers
    """
#       Jun Guo : the past way to run the server

#        server_path = "/" + "Server" + "/" #+ "Server.js"
#        final_path = base_path + user_path + instance_path + server_path

#        child_process = sp.Popen(["npm", "run", "launch"], cwd=final_path)
#        # Temporary solution..
#        time.sleep(0.5)

#        if child_process.poll() == None:
#            flash('Successful to run the specified instance')
#        else:
#            flash('Failed to run the specified instance')

#     _code,serviceCount = commands.getstatusoutput("docker service ls | grep " + file_id + "_web | awk '{print $4}' | cut -d / -f 1")

#     if serviceCount == '0':
#         print "service stopped, restarting ... "
# #       os.system("docker service update --replicas 1 " + file_id + "_db")
# #       os.system("docker service update --replicas 1 " + file_id + "_web")
#         os.system("docker service scale " + file_id + "_db=1 " + file_id + "_web=1")
            
#         dbOps.registerRunningInstance(mgInstance.mongo, username, domain_model_name, file_id)
#         return True
#     else:
#         print "no service"

  
#     user_path = "/" + username
#     instance_path = "/" + domain_model_name + "/" + file_id
#     final_path = base_path + user_path + instance_path
#     # Jun Guo :  create stack
#     os.system('docker stack deploy -c ' + final_path + '/docker-compose.yaml ' + file_id)

#     # Get published port
#     _code,port = commands.getstatusoutput('docker service inspect --format "{{ (index .Endpoint.Ports 0).PublishedPort }}" ' + file_id + "_web")

#     # Jun Guo : Check whether service is available
#     retry_time, iter_no = 50, 0
#     _code,state = commands.getstatusoutput("docker service ps " + file_id + "_web | awk '{print $6}' | sed -n '2p'")
        
#     while state != 'Running' and iter_no < retry_time:
#         _code,state = commands.getstatusoutput("docker service ps " + file_id + "_web | awk '{print $6}' | sed -n '2p'")  
#         time.sleep(0.5)
#         iter_no += 1   

#     if iter_no >= 50:
#         return False
#     else:
#         dbOps.registerRunningInstance(mgInstance.mongo, username, domain_model_name, file_id)
#         return True
    cmd = "bash ./utilities/start_container.sh {} {} {} {}".format(base_path, username, domain_model_name, file_id)
    _code,output = commands.getstatusoutput(cmd)
    print(output)
    status = output.split("\n")[-1]
    if status == "False":
        return False
    else:
        return True


def stop_container(user_name, project_name, instance_id):
    """
    Stop containers
    """
    return


def delete_container(user_name, project_name, instance_id):
    return

def refresh_container(user_name, project_name, instance_id):
    return

def make_request(addr, method_name, user_name, project_name, instance_id):
    return

if __name__ == '__main__':
    print('test')


