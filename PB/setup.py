from cx_Freeze import setup, Executable

setup(
    name = "21",
    version = "0.1",
    description = "Blackjack",
    executables = [Executable("privat_bank.py")]
)