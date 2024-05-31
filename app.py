# from events.continuous_listening import continuous_listening
from events.initial_fetch import initial_fetch


def main():
    start_block = 14820784
    latest_block = 15132605
    initial_fetch(start_block, latest_block)
    # print("Latest block: ", latest_block)
    # continuous_listening(latest_block)


if __name__ == "__main__":
    main()
