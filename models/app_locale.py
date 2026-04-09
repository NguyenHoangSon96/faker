from dataclasses import dataclass


@dataclass(frozen=True)
class AppLocale:
    code: str
    name: str
    locale: str
