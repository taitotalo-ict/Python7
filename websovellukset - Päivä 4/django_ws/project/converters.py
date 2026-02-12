from datetime import date

class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value: str) -> int:
        return int(value)

    def to_url(self, value: int) -> str:
        return "%04d" % value

class DateConverter:
    # YYYY-MM-DD
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> date:
        try:
            new_value = date.fromisoformat(value)
        except:
            raise ValueError()
        return new_value

    def to_url(self, value: date) -> str:
        return value.isoformat()
        