'''

This Program was made by Yannik Ott for the Semax AG Developer Assessment

3. Create a project which can:
    a. List all system processes by name including its PID, memory usage, and owner
    b. List system processes by owner including its PID, Memory usage, and process name.


For this to work I used Win10, psutil 5.8.0 and python 3.8.3

pip install psutil

'''

import psutil
# psutil is a tool for system monitoring
# for every process in psutil.process_iter I fetch the name including its PID, memory usage, and owner
# to save I use a dictionary

def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
        
        try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo)

        # according to the psutil documentation this try/except solves a lot of problems
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass

    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    for proc in listOfProcObjects:
        processInfo = ''
        for key in proc:
            processInfo += str(proc[key])+ ' '
        print(processInfo)
    return listOfProcObjects

def printSortedByName()




def printSortedByOwner()


if __name__ == '__main__':
   getListOfProcessSortedByMemory()
   
   
   printSortedByName()
   
   
   #printSortedByOwner()