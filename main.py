from extractor import extract_and_save
from db_loader import init_db, load_csv_to_db, run_queries


def main():
    extract_and_save()
    init_db()
    load_csv_to_db()
    run_queries()


if __name__ == "__main__":
    main()
