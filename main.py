from pathlib import Path

import pandas as pd
import requests


BASE_DIR = Path(__file__).resolve().parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
GOLD_DIR = BASE_DIR / "data" / "gold"


SOURCES = [
    {
        "url": "https://rosstat.gov.ru/storage/mediabank/02-23-01.xlsx",
        "year": 2023,
        "period": "январь-июнь",
    },
    {
        "url": "https://rosstat.gov.ru/storage/mediabank/02-23-02.xlsx",
        "year": 2023,
        "period": "январь-сентябрь",
    },
    {
        "url": "https://rosstat.gov.ru/storage/mediabank/02-23-03.xlsx",
        "year": 2023,
        "period": "январь-декабрь",
    },
]


def download_file(url: str, path: Path) -> None:
    """
    Скачать файл по URL и сохранить его локально.

    Необходимо предусмотреть:
    - проверку HTTP-статуса;
    - обработку ошибок соединения;
    - отсутствие повторной загрузки существующего файла;
    - создание директории назначения.
    """
    pass


def read_source_file(path: Path) -> pd.DataFrame:
    """
    Прочитать исходный Excel-файл.

    Необходимо самостоятельно определить:
    - нужный лист;
    - структуру заголовков;
    - начало и конец таблицы;
    - способ формирования названий колонок.
    """
    pass


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Очистить и нормализовать данные.

    Необходимо обработать:
    - числовые значения;
    - пропуски;
    - специальные значения;
    - названия регионов;
    - даты и периоды;
    - названия колонок.
    """
    pass


def transform_data(
    df: pd.DataFrame,
    year: int,
    period: str,
) -> pd.DataFrame:
    """
    Привести данные к структуре, необходимой для формирования gold-слоя.
    """
    pass


def build_gold_table(data: list[pd.DataFrame]) -> pd.DataFrame:
    """
    Объединить данные всех источников и сформировать gold_salary.

    Необходимо самостоятельно определить:
    - гранулярность;
    - ключ;
    - правила дедупликации;
    - состав итоговых полей.
    """
    pass


def validate_gold_table(df: pd.DataFrame) -> None:
    """
    Проверить качество итоговой таблицы.

    Минимальные проверки:
    - уникальность ключа;
    - обязательные поля;
    - типы данных;
    - корректность числовых показателей;
    - отсутствие неожиданных дубликатов.
    """
    pass


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    GOLD_DIR.mkdir(parents=True, exist_ok=True)

    processed_data = []

    for source in SOURCES:
        filename = Path(source["url"]).name
        raw_file = RAW_DIR / filename

        download_file(
            url=source["url"],
            path=raw_file,
        )

        df = read_source_file(raw_file)

        df = clean_data(df)

        df = transform_data(
            df=df,
            year=source["year"],
            period=source["period"],
        )

        processed_data.append(df)

    gold = build_gold_table(processed_data)

    validate_gold_table(gold)

    gold_path = GOLD_DIR / "gold_salary.csv"
    gold.to_csv(
        gold_path,
        index=False,
        sep=";",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
