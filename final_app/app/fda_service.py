import requests


class FDAService:

    BASE_URL = "https://api.fda.gov/drug/event.json"

    def search(self, drug_name: str, limit=3):

        params = {
            "search": f"patient.drug.medicinalproduct:{drug_name}",
            "limit": limit
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:
            return None

        data = response.json()

        side_effects = []

        for result in data.get("results", []):
            reactions = result.get("patient", {}).get("reaction", [])
            for r in reactions:
                side_effects.append(r.get("reactionmeddrapt"))

        return side_effects