from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    mock = [{
        "min_salary": "5000",
        "max_salary": "15000",
        "date_posted": "2000-10-31",
    }, {
        "min_salary": "2000",
        "max_salary": "9000",
        "date_posted": "2003-03-05",
    }, {
        "min_salary": "3000",
        "max_salary": "10000",
        "date_posted": "2020-03-15",
    }]
    first_order = [mock[0], mock[2], mock[1]]
    second_order = [mock[1], mock[2], mock[0]]
    sort_by(mock, "max_salary")
    assert mock == first_order
    sort_by(mock, "min_salary")
    assert mock == second_order
