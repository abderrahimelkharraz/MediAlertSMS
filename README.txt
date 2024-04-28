

1. Imports necessary modules like `schedule`, `vonage`, `time`, and `os`.
2. Retrieves Vonage API key and secret from environment variables.
3. Creates a Vonage client and SMS object.
4. Defines a list of phone numbers to send messages to.
5. Defines a function `send_message_to_numbers()` to send messages to the numbers in the list.
6. Schedules the function `send_message_to_numbers()` to be executed daily at specific times.
7. Runs the scheduler in an infinite loop.

