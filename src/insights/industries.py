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
    """Filters a list of jobs by industry

    Parameter
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
