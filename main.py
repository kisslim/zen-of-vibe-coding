#!/usr/bin/env python3
"""
Virtual Vibe Coder - AI-assisted development on Arch Linux
"""

import argparse
from vibe_coder.core import VirtualVibeCoder
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
import readline  # For better input handling

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Virtual Vibe Coder")
    parser.add_argument("--model", default="deepseek-r1:8b", help="Ollama model to use")
    args = parser.parse_args()
    
    console.print(Panel.fit(
        "[bold cyan]Virtual Vibe Coder[/bold cyan]\n"
        "[italic]AI-assisted development on Arch Linux[/italic]",
        border_style="cyan"
    ))
    
    # Initialize the vibe coder
    try:
        vibe_coder = VirtualVibeCoder(model_name=args.model)
        console.print("[green]✓ Vibe Coder initialized successfully[/green]")
        console.print(vibe_coder.get_environment_info())
    except Exception as e:
        console.print(f"[red]Error initializing Vibe Coder: {e}[/red]")
        return
    
    console.print("\n[bold]Vibe Coding Principles Active:[/bold]")
    console.print("• Runnable is better than beautiful")
    console.print("• Verified is better than explicit") 
    console.print("• The compiler is the final arbiter of truth")
    console.print("• Thinking mode is not a waste of time\n")
    
    # Interactive loop
    while True:
        try:
            user_input = console.input("[bold yellow]🎯 Vibe Coder > [/bold yellow]")
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            elif user_input.lower() in ['help', '?']:
                console.print("""
[bold]Available commands:[/bold]
• [cyan]help[/cyan] - Show this help
• [cyan]info[/cyan] - Show environment information  
• [cyan]clear[/cyan] - Clear conversation history
• [cyan]quit[/cyan] - Exit the Vibe Coder

[bold]Examples:[/bold]
• "Create a Python web server on port 8000"
• "Write a script to backup my documents"
• "Set up a Rust project with cargo"
• "Install and configure nginx"
                """)
                continue
            elif user_input.lower() == 'info':
                console.print(vibe_coder.get_environment_info())
                continue
            elif user_input.lower() == 'clear':
                vibe_coder.conversation_history.clear()
                console.print("[green]Conversation history cleared[/green]")
                continue
            elif not user_input.strip():
                continue
                
            with console.status("[bold green]Vibing...[/bold green]"):
                response = vibe_coder.process_request(user_input)
            
            console.print(Panel(
                Markdown(response),
                title="🤖 Vibe Coder Response",
                border_style="green"
            ))
            
        except KeyboardInterrupt:
            console.print("\n[yellow]Exiting Vibe Coder...[/yellow]")
            break
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    main()