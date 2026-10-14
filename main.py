from rich.console import Console
from engine import Question
import logging
console = Console()

questions = [
    Question("پایتخت ژاپن کدام است؟", ["توکیو", "کیوتو", "اوساکا", "سئول"], "A"),
    Question("خروجی len('سلام') چیست؟", ["3", "4", "5", "خطا"], "B"),
    Question("بزرگ‌ترین سیاره‌ی منظومه‌ی شمسی؟", ["زمین", "زحل", "مشتری", "نپتون"], "C"),
    Question("نماد شیمیایی طلا چیست؟", ["Ag", "Au", "Fe", "Gd"], "B"),
    Question("شاهنامه اثر کیست؟", ["حافظ", "سعدی", "فردوسی", "مولوی"], "C"),
]

def show_menu():
    console.print("\n[bold cyan]⚔  Quiz Battle  ⚔[/bold cyan]")
    console.print("[bold green]۱)[/bold green] بازی جدید")
    console.print("[bold red]۲)[/bold red] خروج")


def play():
    total = len(questions)
    score = 0
    correct_count = 0

    for i, (text, options, correct) in enumerate(questions, start=1):
        console.print(f"\n[bold cyan]سؤال {i} از {total}:[/bold cyan] {text}")
        for letter, opt in zip("ABCD", options):
            console.print(f"  [bold]{letter})[/bold] {opt}")

        answer = input("جواب تو (A-D): ").strip().upper()

        if answer == correct:
            console.print(" درست!", style="bold green")
            score += 10
            correct_count += 1
        else:
            console.print(f" غلط! جواب درست: {correct}", style="bold red")

    return score, correct_count, total

def show_results(score, correct_count, total):
    percent = correct_count / total * 100
    console.print("\n بازی تمام شد!", style="bold yellow")
    console.print(f"   امتیاز تو: [bold green]{score}[/bold green]")
    console.print(f"   درست: {correct_count} از {total}  ([bold]{percent:.0f}٪[/bold])")

while True:
    show_menu()
    choice = input("انتخاب تو (۱ یا ۲): ").strip()
    if choice == '2':
        console.print("خداحافظ!", style="bold cyan")
        break
    if choice != "1":
        continue
    
    score, correct_count, total = play()
    show_results(score, correct_count, total)

    