import requests
from openpyxl import Workbook
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


def fetch_hardware(page):
    url = f"https://servicespub.prod.api.aws.grupokabum.com.br/catalog/v2/products-by-category/hardware?page_number={page}&page_size=100&facet_filters=&sort=most_searched&is_prime=false&payload_data=products_category_filters&include=gift"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(
            f"Erro ao fazer a requisição: url{url}, status_code: {response.status_code}"
        )
        raise err

    l_products = [
        {
            "id": x["id"],
            "name": x["attributes"]["title"],
            "price": x["attributes"]["price"],
            "price_with_discount": x["attributes"]["price_with_discount"],
            "quantity_available": x["attributes"]
            .get("offer", {})
            .get("quantity_available", 0)
            if x["attributes"].get("offer")
            else 0,
            "score_of_ratings": x["attributes"]["score_of_ratings"],
            "number_of_ratings": x["attributes"]["number_of_ratings"],
            "photos-g": str(x["attributes"]["photos"]["g"]),
            "warranty": x["attributes"]["warranty"],
        }
        for x in response.json()["data"]
    ]

    return l_products


def hardware_data():
    url = "https://servicespub.prod.api.aws.grupokabum.com.br/catalog/v2/products-by-category/hardware?page_number=1&page_size=100&facet_filters=&sort=most_searched&is_prime=false&payload_data=products_category_filters&include=gift"
    response = requests.get(url)
    total_pages = response.json()["meta"]["total_pages_count"]
    total_products = []

    start = datetime.now()

    with ThreadPoolExecutor(
        max_workers=5
    ) as executor:  # Utilizando ThreadPoolExecutor para paralelizar as requisições
        futures = [
            executor.submit(fetch_hardware, page) for page in range(1, total_pages + 1)
        ]
        for i, future in enumerate(futures, 1):
            print(f"Processando página {i} de {total_pages}...")
            total_products.extend(future.result())

    print(f"total time para as reqs -> {datetime.now() - start}")
    return total_products


def to_excel(data, file_name):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Hardware Products"

    # Adiciona o cabeçalho
    headers = [
        "ID",
        "Name",
        "Price",
        "Price with Discount",
        "Quantity Available",
        "Score of Ratings",
        "Number of Ratings",
        "Photos (g)",
        "Warranty",
    ]
    sheet.append(headers)

    for item in data:
        sheet.append(list(item.values()))

    workbook.save(file_name)
    print(f"Arquivo Excel salvo como '{file_name}'")


def main():
    hardware_products = hardware_data()
    to_excel(hardware_products, file_name="hardware_products.xlsx")


if __name__ == "__main__":
    main()
