from impyrial.length.core import inches_to_feet, inches_to_yards

# Define tests for inches_to_feet function
def test_inches_to_feet():
	# Check that 12 inches is converted to 1.0 foot
    assert inches_to_feet(12) == 1.0
    # Check that 2.5 feet is converted to 30.0 inches
    assert inches_to_feet(2.5, reverse=True) == 30.0

'''
pytest output:
repl:~/workspace/mypackages/impyrial$ pytest
=========================================================== test session starts ===========================================================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
Matplotlib: 3.4.3
Freetype: 2.6.1
rootdir: /home/repl/workspace/mypackages/impyrial
plugins: mock-3.8.2, mpl-0.16.1
collected 3 items                                                                                                                         

tests/length/test_core.py .                                                                                                         [ 33%]
tests/weight/test_core.py ..                                                                                                        [100%]

============================================================ 3 passed in 0.15s ============================================================
'''