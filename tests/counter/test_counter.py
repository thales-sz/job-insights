from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "Remote") == 352
    assert count_ocurrences("data/jobs.csv", "On site") == 19
