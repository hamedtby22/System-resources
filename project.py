import psutil;

#Processor information
cpu_percent = psutil.cpu_percent(interval=1,percpu=True)
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq().current

#Memmory information
mem = psutil.virtual_memory()
mem_total = mem.total
mem_used = mem.used
mem_empty = mem.available

#Disk information
disk = psutil.disk_usage('/')
disk_total = disk.total
disk_used = disk.used

#CPU temperature 
#warnning: This function works only for Linux and is not yet applicable for Windows
temps = psutil.sensors_temperatures()
cpu_temp = temps['coretemp'][0].current

log = {
    'cpu_percent':cpu_percent,
    'cpu_freq':cpu_freq,
    'cpu_count':cpu_count,
    'mem_total': mem_total,
    'mem_used': mem_used,
    'mem_empty':mem_empty,
    'disk_total':disk_total,
    'disk_used':disk_used,
    'cpu_temp':cpu_temp,

}

print(log)