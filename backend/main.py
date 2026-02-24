from task_manager import TaskManager

def main ():
    manager = TaskManager()

    while True:
        print("\n==== タスク管理 ====")
        print("1.タスク追加")
        print("2.タスク削除")
        print("3.タスク完了")
        print("4.タスク一覧表示")
        print("5.期限切れタスク表示")
        print("6.終了")

        choice = input("番号を選んでください")

        try:
            if choice == "1":
                title = input("タスク名：")
                deadline = input("期限(YYYY-MM-DD):")
                manager.add_task(title,deadline)
                print("タスクを追加しました。")

            elif choice == "2":
                title = input("削除するタスク名：")
                manager.remove_task(title)
                print("削除しました。")

            elif choice == "3":
                title = input("完了するタスク名：")
                manager.complete_task(title)
                print("完了にしました。")

            elif choice == "4":
                tasks = manager.list_tasks()
                if not tasks:
                    print("タスクはありません")
                else:
                    for t in tasks:
                        print(t)

            elif choice =="5":
                overdue = manager.list_overdue_tasks()
                if not overdue:
                    print("期限切れタスクはありません。")
                else:
                    for t in overdue:
                        print(t)

            elif choice =="6":
                print("終了します。")
                break
            else:
                print("無効な番号です。")

        except Exception as e:
            print(f"エラー：{e}")

if __name__ == "__main__":
    main()