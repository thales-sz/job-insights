from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    mock = {
        "title": "Motorista",
        "salary": "3000",
        "type": "full time",
    }
    assert read_brazilian_file("tests/mocks/brazilians_jobs.csv")[1] == mock
