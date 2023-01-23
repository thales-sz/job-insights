from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as file:
        data = csv.DictReader(file)
        jobs_list = [*data]
    return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    job_types = []
    for job in jobs_list:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list_filter = list()
    for job in jobs:
        if job["job_type"] == job_type:
            list_filter.append(job)
    return list_filter
