import requests
import datetime
import csv
import os
# import тут должна быть библиотечка Python для работы с Excel


def download_File_From_Site(link: str, path_to_save: str):
    """
    Скачивает файлы с сайта

    :param link: строка содержащая ссылку на файл
    :param path_to_save: строка содержащая путь для сохранения
    :return: ответ сервера
    """
    # ТУТ ДОЛЖЕН БЫТЬ КОД ДЛЯ СКАЧКИ ФАЙЛА
    return


def delete_file(path_to_file: str):
    """
    Функция удаления файлов

    :param path_to_file: путь к удаляемому файлу
    """
    # Код для удаления
    return


def convert_xlsx_to_csv(path_to_xlsx: str, path_to_csv: str, header: list = [], separator: str = ";",
                        sheet_number: int = 1, first_row: int = 0, last_row: int = 0,
                        first_column: int = 0, last_column: str = 0, encoding: str = 'utf-8'):
    """
    Функция конвертирования xlsx файла в csv с учётом листа для конвертирования, ячеек которые нужно выбрать из файла,
    заголовка для ячеек (если нужно)

    :param path_to_xlsx: путь к эксель файлу
    :param path_to_csv: путь к csv файлу для сохранения
    :param header: список заголовка
    :param separator: разделитель в csv файле (по умолчанию ';')
    :param sheet_number: номер листа xlsx файла
    :param first_row: первая строка xlsx файла
    :param last_row: последняя строка xlsx файла
    :param first_column: первая колона xlsx файла
    :param last_column: последняя колона xlsx файла
    :param encoding: кодировка итогового csv файла
    """
    # КОД ДЛЯ КОНВЕРТАЦИИ
    return

if __name__ == '__main__':
    links_for_download = [
        'https://rosstat.gov.ru/storage/mediabank/02-23-01.xlsx',
        'https://rosstat.gov.ru/storage/mediabank/02-23-02.xlsx',
        'https://rosstat.gov.ru/storage/mediabank/02-23-03.xlsx'] # список файлов для закачки
    # Блок кода для закачки файлов
    # КОД

    #Блок кода конвертации полученных файлов
    # КОД

    # Блок кода удаления скаченных ранее xlsx
    # КОД
