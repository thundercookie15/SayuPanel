from typing import Any


def get_pages(filename): ...


header_pattern: Any
footer_pattern: Any


def remove_header(page): ...


def remove_footer(page): ...


def clean_pages(): ...


def save_clean() -> None: ...
