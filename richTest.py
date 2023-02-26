# info on Rich 
# from rich import print;

# print("Hello, [bold red]Rich[/] :snake:");

# See all supported emoji's by running python -m rich.emoji 

# The approve print function is not generally what is used to create a better interaction, use Console since it allows be a better interaction.

from rich.console import Console; 
from rich.theme import Theme; # provides option to give additional pretext to content

console = Console(width=40, theme=Theme({"warning": "red on yellow"})); # if you don't specify the width, it will use the whole width of the terminal
#theme is kind of line adding styling inline.

console.print("Hello, [bold red]Rich[/] :wrapped_gift:");
# rule added decorative line
console.rule(f"[bold blue]:leafy_green: ADD LINE HERE :leafy_green:[/]\n");
console.print("Ops", style="warning");