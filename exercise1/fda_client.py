import requests


class FDAClient:

    BASE_URL = "https://api.fda.gov/drug/event.json"

    def search_events(self, drug_name: str, limit=5, skip=0):

        params = {
            "search": f"patient.drug.medicinalproduct:{drug_name}",
            "limit": limit,
            "skip": skip
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:
            return None

        return response.json()

    def extract_summary(self, data):

        if not data or "results" not in data:
            return []

        summaries = []

        for result in data["results"]:

            country = result.get("primarysourcecountry", "Unknown")
            serious = result.get("serious", "Unknown")

            reactions = result.get("patient", {}).get("reaction", [])

            side_effects = [
                r.get("reactionmeddrapt", "Unknown")
                for r in reactions
            ]

            summaries.append({
                "country": country,
                "serious": serious,
                "side_effects": side_effects
            })

        return summaries