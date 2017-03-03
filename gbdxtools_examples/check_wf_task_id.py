#!/usr/bin/python

#############################################################################################
#
#  check_wf_task_status.py
#
#  Created by: Dave Loomis
#              Digitalglobe GBD Solutions
#
#  Version 0.1: Jun 15, 2016
#               - check the wf status and task status of given WF using gbdxtools
#
#  Usage: python check_wf_task_status.py workflow_id (required)
#
#
#############################################################################################

from gbdxtools import Interface
import sys

# instantiate gbdxtools
gbdx = Interface()
# get the workflow id from command line
workflow_id = sys.argv[1]
workflow = gbdx.Workflow( [] )  # instantiate a blank workflow
workflow.id = workflow_id

# print the status
print
print(str(workflow.id) + " status --> " + workflow.status["state"] + " : " + workflow.status['event'])
print("----------------------------------")

task_status = {}
for e in workflow.events :
    if e['state'] == 'pending' and e['task'] not in task_status :
        task_status[e['task']] = e['state'] + ":" + e["event"]
    if e['state'] == 'running' and e['task'] in task_status and 'complete' not in task_status[e['task']]  :
        task_status[e['task']] = e['state'] + ":" + e["event"]
    if e['state'] == 'complete' :
        #task_status[e['task']] = e['state'] + ":" + e["event"]
        task_status[e['task']] = e['state'] + ":" + e["event"] + " : " + e["note"]

print"COMPLETE"
for k,v in task_status.iteritems() :
    if 'complete' in v :
        print(k + " --> " + v)
print
print"RUNNING"
for k,v in task_status.iteritems() :
    if 'running' in v :
        print(k + " --> " + v)
print
print"PENDING"
for k,v in task_status.iteritems() :
    if 'pending' in v :
        print(k + " --> " + v)
print