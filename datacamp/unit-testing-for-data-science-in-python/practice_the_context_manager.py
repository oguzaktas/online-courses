import pytest

# Fill in with a context manager that will silence the ValueError
with pytest.raises(ValueError):
    raise ValueError

try:
    # Fill in with a context manager that raises Failed if no OSError is raised
    with pytest.raises(OSError):
        raise ValueError
except:
    print("pytest raised an exception because no OSError was raised in the context.")

with pytest.raises(ValueError) as exc_info:
    raise ValueError("Silence me!")
# Check if the raised ValueError contains the correct message
assert exc_info.match("Silence me!")