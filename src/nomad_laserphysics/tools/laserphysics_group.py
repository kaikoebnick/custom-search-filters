import json
import os
import threading

LOCK = threading.Lock()


class LaserphysicsGroup:
    def __init__(self, data_dir="/app/.volumes/laserphysicsgroup",
                 counter_file="laserphysicsgroup.json"):
        self.data_dir = data_dir
        self.counter_file = os.path.join(data_dir, counter_file)
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f:
                json.dump({"coauthors": []}, f)


    def get_coauthors(self):
        """Reads coauthors"""
        with LOCK:
            if not os.path.exists(self.counter_file):
                data = {"coauthors": []}
            else:
                with open(self.counter_file) as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = {"coauthors": []}

            return data["coauthors"]