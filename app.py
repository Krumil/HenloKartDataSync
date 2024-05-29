# app.py
from config.db import database
from events.continuous_listening import continuous_listening
from events.initial_fetch import initial_fetch


def main():
    start_block = 14820784
    latest_block = initial_fetch(start_block)
    continuous_listening(latest_block)


if __name__ == "__main__":
    main()
