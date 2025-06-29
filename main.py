# main.py
from agent.decision_agent import handle_question
from termcolor import colored

def print_help():
    print(colored("📘 คำสั่งพิเศษ:", "cyan"))
    print(colored("  /exit     - ออกจากโปรแกรม", "cyan"))
    print(colored("  /clear    - ล้างประวัติการสนทนา", "cyan"))
    print(colored("  /help     - แสดงคำสั่งทั้งหมด", "cyan"))

def run_cli():
    print(colored("🤖 สวัสดี! พิมพ์คำถามของคุณ (พิมพ์ /help เพื่อดูคำสั่ง)", "green"))
    history = []
    try:
        while True:
            question = input(colored("❓: ", "yellow")).strip()

            if not question:
                print(colored("⚠️ กรุณาพิมพ์คำถามครับ", "red"))
                continue

            # -- คำสั่งพิเศษ -- #
            if question.lower() in ["/exit", "exit", "quit"]:
                print(colored("👋 ขอบคุณที่ใช้งานครับ!", "green"))
                break
            if question.lower() in ["/clear"]:
                history.clear()
                print(colored("🧹 ล้างประวัติเรียบร้อย", "blue"))
                continue
            if question.lower() in ["/help"]:
                print_help()
                continue

            # -- ประมวลผลคำถาม -- #
            history.append(question)
            answer = handle_question(question, history)
            print(colored(f"💬: {answer}\n", "green"))

    except KeyboardInterrupt:
        print(colored("\n👋 ออกจากโปรแกรมแล้วครับ", "green"))

if __name__ == "__main__":
    run_cli()
