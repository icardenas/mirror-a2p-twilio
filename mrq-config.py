import os
import uuid

""" Redis and MongoDB settings
"""
#MongoDB settings
MONGODB_JOBS = os.environ.get("MONGODB_URI") #MongoDB URI for the jobs, scheduled_jobs & workers database.Defaults to mongodb://127.0.0.1:27017/mrq
MONGODB_LOGS = "1" #MongoDB URI for the logs database."0" will disable remote logs, "1" will use main MongoDB.Defaults to 1
MONGODB_LOGS_SIZE = None #If provided, sets the log collection to capped to that amount of bytes.
NO_MONGODB_ENSURE_INDEXES = None #If provided, skip the creation of MongoDB indexes at worker startup.

#Redis settings
REDIS = os.environ.get("REDIS_URL")  #Redis URI.Defaults to redis://127.0.0.1:6379
REDIS_PREFIX = "mrq" #Redis key prefix.Default to "mrq".
REDIS_MAX_CONNECTIONS = 1000 #Redis max connection pool size.Defaults to 1000.
REDIS_TIMEOUT = 30 #Redis connection pool timeout to wait for an available connection.Defaults to 30.

"""General MrQ settings
"""
TRACE_GREENLETS = False #Collect stats about each greenlet execution time and switches.Defaults to False.
TRACE_MEMORY = False #Collect stats about memory for each task. Incompatible with `GREENLETS` > 1. Defaults to False.
TRACE_IO = False #Collect stats about all I/O operations.Defaults to True.
PRINT_MONGODB = False #Print all MongoDB requests.Defaults to False.
TRACE_MEMORY_TYPE = "" #Create a .png object graph in trace_memory_output_dir with a random object of this type.
TRACE_MEMORY_OUTPUT_DIR = "memory_traces" #Directory where to output .pngs with object graphs.Defaults to folder memory_traces.
PROFILE = False #Run profiling on the whole worker.Defaults to False.
NAME = uuid.uuid4() #Specify a different name.
QUIET = False #Don\'t output task logs.Defaults to False.
CONFIG = None #Path of a config file.
WORKER_CLASS = "mrq.worker.Worker" #Path to a custom worker class.Defaults to "mrq.worker.Worker".
VERSION = False #Prints current MRQ version.Defaults to  False.
NO_IMPORT_PATCH = False #Skips patching __import__ to fix gevent bug #108.Defaults to False.
ADD_NETWORK_LATENCY = 0 #Adds random latency to the network calls, zero to N seconds. Can be a range (1-2)').Defaults to 0.
DEFAULT_JOB_RESULT_TTL = 1209600 #Seconds the results are kept in MongoDB when status is success. 1209600 seconds which are 2 weeks.
DEFAULT_JOB_ABORT_TTL = 86400 #Seconds the tasks are kept in MongoDB when status is abort.Defaults to 86400 seconds which is 1 day.
DEFAULT_JOB_CANCEL_TTL = 86400 #Seconds the tasks are kept in MongoDB when status is cancelDefaults to 86400 seconds which is 1 day.
DEFAULT_JOB_TIMEOUT = 3600 #In seconds, delay before interrupting the job.Defaults to 3600 seconds which is 1 hour.
DEFAULT_JOB_MAX_RETRIES = 3 #Set the status to "maxretries" after retrying that many times.Defaults to 3 seconds.
DEFAULT_JOB_RETRY_DELAY = os.environ.get("DEFAULT_JOB_RETRY_DELAY", 7200) #Seconds before a job in retry status is requeued again.Defaults to 3 seconds.
USE_LARGE_JOB_IDS = False #Do not use compacted job IDs in Redis. For compatibility with 0.1.x only. Defaults to

""" mrq-worker settings
"""
mrq_queues = 'high, medium, low, default'
QUEUES = mrq_queues # The queues to listen on.Defaults to default , which will listen on all queues.
DEQUEUE_STRATEGY = "sequential"
MAX_JOBS = 0 #Gevent:max number of jobs to do before quitting. Workaround for memory leaks in your tasks. Defaults to 0
MAX_MEMORY = 0 #Max memory (in Mb) after which the process will be shut down. Use with PROCESS = [1-N] to have supervisord automatically respawn the worker when this happens.Defaults to 1
GREENLETS = os.environ.get("MRQ_GREENLETS", 10)  #Max number of greenlets to use.Defaults to 1.
PROCESSES = os.environ.get("MRQ_PROCESSES", 4) #Number of processes to launch with supervisord.Defaults to 0.
SUPERVISORD_TEMPLATE = "supervisord_templates/default.conf" #Path of supervisord template to use. Defaults to supervisord_templates/default.conf.
SCHEDULER = False #Run the scheduler.Defaults to False.
SCHEDULER_INTERVAL = 60 #Seconds between scheduler checks.Defaults to 60 seconds, only ints are acceptable.
REPORT_INTERVAL = 10.5 #Seconds between worker reports to MongoDB.Defaults to 10 seconds, floats are acceptable too.
REPORT_FILE = "" #Filepath of a json dump of the worker status. Disabled if none.
ADMIN_PORT = 0 #Start an admin server on this port, if provided. Incompatible with --processes.Defaults to 0
ADMIN_IP = "127.0.0.1" #IP for the admin server to listen on. Use "0.0.0.0" to allow access from outside.Defaults to 127.0.0.1.
LOCAL_IP = "" #Overwrite the local IP, to be displayed in the dashboard.
MAX_LATENCY = 1  #Max seconds while worker may sleep waiting for a new job.Can be < 1 and a float value.

""" mrq-dashboard settings
"""
DASHBOARD_HTTPAUTH = os.environ.get("DASHBOARD_HTTPAUTH", "admin:admin") #HTTP Auth for the Dashboard. Format is user:pass
DASHBOARD_QUEUE = "default" #Default queue for dashboard actions.
DASHBOARD_PORT = os.environ.get("PORT", 7777) #Use this port for mrq-dashboard.Defaults to port 5555.
DASHBOARD_IP = "0.0.0.0" #Bind the dashboard to this IP. Default is 0.0.0.0, use 127.0.0.1 to restrict access.
PAUSED_QUEUES_REFRESH_INTERVAL = 0 #Seconds between worker refreshes of the paused queues list.
