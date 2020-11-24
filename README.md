# nomad_exporter

# build

build container

```
docker build -t nomad_exporter:0.0.1 -f docker/Dockerfile .
```


# run

Used variables:

NOMAD_EXPORTER_IP - exporter bind ip(default 127.0.0.1)

NOMAD_EXPORTER_PORT - exporter bind port(default 9001)

NOMAD_ADDR - nomad address (default http://127.0.0.1:4646)

Run container:

```
docker run -e NOMAD_EXPORTER_IP=0.0.0.0 -e NOMAD_EXPORTER_PORT=9001 -e NOMAD_ADDR=http://192.168.0.1:4646 --rm -d nomad_exporter:0.0.1

```

# example metrics

```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 96.0
python_gc_objects_collected_total{generation="1"} 250.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 63.0
python_gc_collections_total{generation="1"} 5.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="6",patchlevel="8",version="3.6.8"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 3.5596288e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.1618688e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.60568944476e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 2257.27
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 9.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP nomad_deployments Count of deployments
# TYPE nomad_deployments gauge
nomad_deployments 1.0
# HELP nomad_jobs Current count of jobs
# TYPE nomad_jobs gauge
nomad_jobs{state="pending"} 1.0
nomad_jobs{state="running"} 2.0
nomad_jobs{state="dead"} 1.0
# HELP nomad_job Job status(-1 dead, 0 pending, 1 running)
# TYPE nomad_job gauge
nomad_job{name="traefik"} 1.0
nomad_job{name="echo"} 0.0
nomad_job{name="nginx"} 1.0
# HELP nomad_nodes Count of nodes
# TYPE nomad_nodes gauge
nomad_nodes 3.0
# HELP nomad_node Status of node(-1 dead, 0 initializing, 1 ready)
# TYPE nomad_node gauge
nomad_node{node="node1"} 1.0
nomad_node{node="node2"} 0.0
nomad_node{node="node3"} 1.0
```