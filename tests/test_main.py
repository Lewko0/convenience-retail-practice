from src.retail.main import PROCESS_STAGES


def test_process_has_ten_stages():
    assert len(PROCESS_STAGES) == 10
