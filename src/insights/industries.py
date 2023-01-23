from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)
    industries = []
    for job in jobs_list:
        if len(job["industry"]) > 0:
            if job["industry"] not in industries:
                industries.append(job["industry"])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_filter = list()
    for job in jobs:
        if job["industry"] == industry:
            list_filter.append(job)
    return list_filter
