from config.web3 import web3, contract
from events.handlers import handle_event
import time


def continuous_listening(latest_block):
    while True:
        try:
            # Create new event filters from the latest block
            race_finished_filter = contract.events.RaceFinished.create_filter(
                fromBlock=latest_block
            )
            player_committed_filter = contract.events.PlayerCommitted.create_filter(
                fromBlock=latest_block
            )

            # Poll for new events
            race_finished_entries = race_finished_filter.get_new_entries()
            player_committed_entries = player_committed_filter.get_new_entries()

            for event in player_committed_entries:
                handle_event(event)

            for event in race_finished_entries:
                handle_event(event)

            latest_block = web3.eth.block_number  # Update to the latest block
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            time.sleep(5)
