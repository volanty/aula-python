import pandas as pd


class LeadConverter:

    def __init__(self):
        self.max_leads = 100

    def converter(self):
        df = pd.DataFrame({"name": ["Elizeu", "Jurema", "Elizabeth"], "age": [40, 20, 30], "sex": ["m", "f", "f"]})
        return df.describe().to_string()

    def get_lead_id(self, lead_id: str = "abc"):
        print("lead " + lead_id)
