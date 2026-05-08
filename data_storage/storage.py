import os
import json
import csv
class StorageManager:
    def init(self, filename="calc_history"):
        self.json_file = f"{filename}.json"
        self.csv_file = f"{filename}.csv"
        self.unique_operators = set()

    def save_state(self, history: list):
        with open(self.json_file, 'w') as f:
            json.dump(history, f, indent=4)
        with open(self.csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Number 1", "Operator", "Number 2", "Result"])
            for entry in history:
                writer.writerow([
                    entry['id'], entry['num1'], entry['op'], 
                    entry['num2'], entry['result']
                ])
        for entry in history:
            self.unique_operators.add(entry['op'])
    def load_state(self) -> list:
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as f:
                return json.load(f)
        return[]

def history_generator(history_list):
    for item in history_list:
        yield f"[{item['id']}] {item['num1']} {item['op']} {item['num2']} = {item['result']}"