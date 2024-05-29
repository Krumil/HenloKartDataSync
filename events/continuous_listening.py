from config.web3 import web3, contract
from events.handlers import handle_event
import time


def continuous_listening(latest_block):
    while True:
        try:

            # Poll for new PlayerCommitted events
            player_committed_filter = contract.events.PlayerCommitted.create_filter(
                fromBlock=latest_block
            )
            player_committed_entries = player_committed_filter.get_new_entries()
            for event in player_committed_entries:
                handle_event(event)

            # Poll for new RaceFinished
            race_finished_filter = contract.events.RaceFinished.create_filter(
                fromBlock=latest_block
            )
            race_finished_entries = race_finished_filter.get_new_entries()

            for event in race_finished_entries:
                handle_event(event)

            latest_block = web3.eth.block_number
            time.sleep(10)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            time.sleep(10)
