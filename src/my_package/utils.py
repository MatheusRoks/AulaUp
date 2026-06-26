from collections.abc import Callable

from rich.console import Console# type: ignore

console = Console(markup=True, log_path=False, log_time=False)# type: ignore
rprint = console.log# type: ignore


def make_print(style: str) -> Callable[..., None]:

    def fake_print(*values: object) -> None:
        return console.log(*values, style=style)# type: ignore

    return fake_print


def sep_print() -> None:
    rprint(f"\n{80 * '―'}\n", style="yellow")


red_print = make_print(style="red")
green_print = make_print(style="green")
yellow_print = make_print(style="yellow")
blue_print = make_print(style="blue")
magenta_print = make_print(style="magenta")
cyan_print = make_print(style="cyan")