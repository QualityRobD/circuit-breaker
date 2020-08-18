# Python Libraries
from time import sleep


class CircuitBreaker:
    """
    Used to create a slowdown to prevent actions from constantly recurring
    """
    def __init__(self, max_seconds: int):
        self.sleep_time = 2
        self.safety_counter = 1
        self.max_wait = max_seconds
        self.time_slept = 0

    def wait_and_continue(self):
        # checks if time spent sleeping OR the next amount to sleep is greater than the max wait
        if (self.time_slept <= self.max_wait) and (self.sleep_time <= self.max_wait):
            self.time_slept += self.sleep_time
            self.safety_counter += 1
            self.sleep_time *= self.safety_counter
            final_sleep = True
        else:
            # final sleep for max wait time
            self.sleep_time = self.max_wait
            final_sleep = False

        sleep(self.sleep_time)
        return final_sleep
