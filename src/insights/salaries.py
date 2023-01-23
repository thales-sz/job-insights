from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    max_salary = int()
    for job in jobs_list:
        if len(job["max_salary"]) > 0 and job["max_salary"] != 'invalid':
            if max_salary < int(job["max_salary"]):
                max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    min_salary = get_max_salary(path)
    for job in jobs_list:
        if len(job["min_salary"]) > 0 and job["min_salary"] != 'invalid':
            if min_salary > int(job["min_salary"]):
                min_salary = int(job["min_salary"])
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if job["max_salary"] < 0 or job["min_salary"] < 0:
        raise ValueError
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    min = int(job["min_salary"])
    max = int(job["max_salary"])
    if min > max:
        raise ValueError
    print(job["min_salary"], job["max_salary"], salary)
    if min < int(salary) and max > int(salary):
        return True
    return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
