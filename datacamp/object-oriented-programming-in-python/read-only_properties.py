import pandas as pd
from datetime import datetime


# MODIFY the class to use _created_at instead of created_at
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)

        # Add a read-only property: _created_at

    @property
    def created_at(self):
        return self._created_at


# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1, 2], "col2": [3, 4]})