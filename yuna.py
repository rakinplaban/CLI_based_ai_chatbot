from llm import ask_yuna
from rich.console import Console

console = Console()
console.print("[bold blue]Yuna:[/bold blue] Heya~ I'm Yuna! Let's chat 💫")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            console.print("[bold blue]Yuna:[/bold blue] See you soon~ 🌸")
            break

        reply = ask_yuna(user_input)
        console.print(f"[bold blue]Yuna:[/bold blue] {reply}")

    except KeyboardInterrupt:
        console.print("\n[bold blue]Yuna:[/bold blue] Bye-bye~ ✨")
        break
    except Exception as e:
        console.print(f"[red]Oops! Error:[/red] {e}")
