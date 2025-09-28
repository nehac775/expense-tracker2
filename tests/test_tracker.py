import src.tracker as tracker

def test_add_and_load():
    tracker.add_expense(10, "Food", "Test meal")
    df = tracker.load_expenses()
    assert "Food" in df["Category"].values
