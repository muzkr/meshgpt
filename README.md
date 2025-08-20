# meshgpt - Chat Bot for Meshtastic

Meshtastic chat bot with locally deployed Phi-3-mini (4B params) as text generation model.

## Installation

### Prerequisites

To run the Meshtastic Weather Bot, you will need the following:

1. **Python 3.x**: The bot is built with Python 3.7 or newer.
2. **Required Python Libraries**:  
   - `meshtastic` — To interface with the Meshtastic device.
   - `pubsub` — To handle asynchronous messaging and events.
   - `requests` — To fetch weather data from the Open-Meteo API.
   - `pytz` — For timezone handling (used to ensure all times are returned in the correct timezone, e.g., UTC+8 for Beijing Time).

Install all dependencies using:

```bash
pip install meshtastic pubsub requests pytz
```

### Setup

1. Clone the repository or download the code.
2. Install the required dependencies by running the above `pip` command.
3. Adjust the configuration in `bot.py` based on your connection type:
   - **For Serial Connection**: Set the correct serial port (e.g., `/dev/ttyUSB0` on Linux, `COM9` on Windows).
   - **For WiFi Connection**: Set the Meshtastic device's hostname (e.g., the IP address of your WiFi device).

## Running the Bot

Once you have installed the necessary dependencies and configured your connection, you can run the bot using the following command:

```bash
python bot.py --connection-type <serial|wifi> --hostname <hostname> --serial-port <serial_port>
```

- **`--connection-type`**: Choose between `serial` (for USB serial connections) or `wifi` (for WiFi-based Meshtastic devices).
- **`--hostname`**: The hostname or IP address of your Meshtastic device (for WiFi connection).
- **`--serial-port`**: The serial port where your Meshtastic device is connected (for Serial connection).

For serial:
```bash
python bot.py --connection-type serial --serial-port COM9
```

or for WiFi:

```bash
python bot.py --connection-type wifi --hostname <hostname>
```

## Code Structure

### `bot.py`

The main script that runs the Meshtastic bot. It handles:
- Connecting to the Meshtastic device (either via serial or WiFi).
- Listening for incoming messages and processing weather-related commands (`#weather`).
- Sending private messages with weather forecasts to the requesting user.

### `weather.py`

LLM text generation

## License

This project is licensed under the MIT License. Please refer to the LICENSE file for more details.

## Acknowledgments

This repository was forked & adapted from [hayschan/outdoorMeshBot](/hayschan/outdoorMeshBot), with most of the source code relating to  communication and interaction logic (`bot.py`) unchanged.
