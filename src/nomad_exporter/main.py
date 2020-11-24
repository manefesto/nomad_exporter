from prometheus_client import start_http_server, Summary, Counter, Gauge
import nomad
import time
from os import environ

listen_ip = "127.0.0.1" if environ.get("NOMAD_EXPORTER_IP") is None else environ.get("NOMAD_EXPORTER_IP")
listen_port = 9001 if environ.get("NOMAD_EXPORTER_PORT") is None else environ.get("NOMAD_EXPORTER_PORT")
nomad_addr="127.0.0.1" if environ.get("NOMAD_ADDR") is None else environ.get("NOMAD_ADDR")

nomad_server = nomad.Nomad(host="nomad_addr")
const_job_status = ["pending", "running", "dead"]
const_node_status = ["dead", "initializing", "ready"]

def deployments_count():
  return len(nomad_server.deployments.get_deployments())

def jobs_count(job_status):
  status=[]
  for job in nomad_server.jobs.get_jobs():
    if job["Status"] == job_status:
      status.append(job["Name"])
  return len(status)

def nodes_count():
  return len(nomad_server.nodes.get_nodes())

if __name__ == '__main__':
  nomad_deployments = Gauge('nomad_deployments', 'Count of deployments')
  nomad_jobs = Gauge("nomad_jobs","Current count of jobs",["state"])
  nomad_job = Gauge("nomad_job","Job status(-1 dead, 0 pending, 1 running)",["name"])
  nomad_nodes = Gauge("nomad_nodes", "Count of nodes")
  nomad_node = Gauge("nomad_node", "Status of node(-1 dead, 0 initializing, 1 ready)", ["node"])
  print("NOMAD_ADDR: {}, BIND_IP: {}, BIND_PORT: {}".format(nomad_addr, listen_ip, listen_port))
  start_http_server(port=9001, addr="0.0.0.0",)
  while True:
    """
    deployments counter
    """
    nomad_deployments.set(deployments_count())
    """
    """
    nomad_nodes.set(nodes_count())
    """
    job status counter
    """
    for job_status in const_job_status:
      nomad_jobs.labels(state=job_status).set(jobs_count(job_status))
    """
    get for every job status
    """
    for get_job in nomad_server.jobs.get_jobs():
      if get_job["Status"] == "running":
        nomad_job.labels(name=get_job["Name"]).set(1)
      elif get_job["Status"] == "dead":
        nomad_job.labels(name=get_job["Name"]).set(-1)
      elif get_job["Status"] == "pending":
        nomad_job.labels(name=get_job["Name"]).set(0)
    for node in nomad_server.nodes.get_nodes():
      if node["Status"] == "dead":
        node_status = -1
      elif node["Status"] == "initializing":
        node_status = 0
      elif node["Status"] == "ready":
        node_status = 1
      nomad_node.labels(node=node["Name"]).set(node_status)
    time.sleep(5)