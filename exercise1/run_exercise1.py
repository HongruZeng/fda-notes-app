from fda_client import FDAClient


def main():

    client = FDAClient()

    drug_name = input("Enter drug name: ")
    limit = int(input("Limit: "))
    skip = int(input("Skip (pagination): "))

    data = client.search_events(drug_name, limit, skip)

    if not data:
        print("No results found.")
        return

    summaries = client.extract_summary(data)

    for i, summary in enumerate(summaries, start=1):

        print(f"\n--- Report {i} ---")
        print("Country:", summary["country"])
        print("Serious:", summary["serious"])
        print("Side Effects:", summary["side_effects"])


if __name__ == "__main__":
    main()