```python
from datetime import datetime, timezone

class DateService:
    """
    Service layer class responsible for providing date-related business logic.
    Adheres to Clean Architecture principles by encapsulating the logic of 
    retrieving the current date/time.
    """

    @staticmethod
    def get_current_utc_date() -> datetime:
        """
        Returns the current date and time in UTC.

        Returns:
            datetime: Current UTC datetime object
        """
        return datetime.now(timezone.utc)
```