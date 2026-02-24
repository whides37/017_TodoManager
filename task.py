import json

class Task:

    #JSONを読み込む
    def __init__(self,json_path ="students_data.json"):
        self.json_path = json_path
        try:
            with open(json_path,"r",encoding="utf=8")as f:
                self.students = json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            self.students ={}

    #