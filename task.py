from detetime import datetime
import json

class Task:

    #JSONを読み込む
    def __init__(self,title,deadline_str):
        self.title = title

        #文字列をdatetimeに変換
        try:
            self.deadline = datetime.strptime(deadline_str,"%Y-%m-%d")
        except ValueError:
            raise ValueError("日付はYYYY-MM-DD形式で入力してください")
        self.completed = False

    #
    def mark_completed(self):
        self.completed = True

    def is_overdue(self):
        return datetime.now() > self.deadline and not self.completed
    
    def __str__(self):
        status = "完了" if self.completed else "未完了"
        return f"{self.title}| 期限:{self.deadline.date()} | 状態:{status}" 