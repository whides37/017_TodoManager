from task import Task
import json

class TaskManager:

    def __init__(self):
        self.tasks = []
        self.load_data()

        #タスク追加
        def add_task(self,title,deadline_str):
            task = Task(title,deadline_str)
            self.tasaks.append(task)
            self.save.data()

        #タスク削除
        def remove_task(self,title):
            for task in self.tasks:
                if task.title ==title:
                    self.tasks.remove(task)
                    self.save.data()
                    return
            raise KeyError("そのタスクは存在しません")
        
        #完了処理
        def complete_task(self,title):
            for task in self.tasks:
                if task.title == title:
                    task.mark_completed()
                    self.save_data()
                    return
            raise KeyError("そのタスクは存在しません")
        
        #一覧表示
        def list_tasks(self):
            return [str(task)for task in self.tasks]
        
        #期限切れタスク表示
        def list_overdue_tasks(self):
            return [str(task)for task in self.tasks if task.is_overdue()]