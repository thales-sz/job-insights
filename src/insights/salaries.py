from typing import Union, List, Dict
from .jobs import read


def is_numeric_value(value) -> bool:
    salary_types = [int, str]
    if type(value) not in salary_types:
        return False
    if isinstance(value, str) and not value.isnumeric():
        return False
    return True


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    max_salary = int()
    for job in jobs_list:
        if is_numeric_value(job["max_salary"]):
            if max_salary < int(job["max_salary"]):
                max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    min_salary = get_max_salary(path)
    for job in jobs_list:
        if is_numeric_value(job["min_salary"]):
            if min_salary > int(job["min_salary"]):
                min_salary = int(job["min_salary"])
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    keys = ["min_salary", "max_salary"]
    for key in keys:
        if key not in job:
            raise (ValueError)
        if not is_numeric_value(job[key]):
            raise (ValueError)
    min = int(job["min_salary"])
    max = int(job["max_salary"])
    if min > max or not is_numeric_value(salary):
        raise (ValueError)
    return min <= int(salary) <= max


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filter_list = list()
    if is_numeric_value(salary) and int(salary) >= 0:
        for job in jobs:
            if int(job["min_salary"]) < int(job["max_salary"]):
                if matches_salary_range(job, salary):
                    filter_list.append(job)
    return filter_list
