# Twitter Ticker Tape

Screens tend to keep me awake in the evening so I wondered if I could print out my Twitter home timeline, live, as I read a book in the evening.

Here’s the final project in action:

![A POS58 receipt printer printing out textual tweets](https://github.com/healeycodes/twitter-ticker-tape/blob/master/in-action.gif)

See my [**blog post**](https://healeycodes.com/twitter-ticker-tape/) for more extensive documentation and a beginner-friendly explanation of the project.

<br>

### Install

_Tested with: Python 3.5.3, Raspbian GNU/Linux 9 (stretch)_

`pip3 install -r requirements.txt`

<br>

### Setup

Set your Twitter API keys inside `config.py` or export them as environmental values.

- `CONSUMER_KEY`
- `CONSUMER_SECRET`
- `ACCESS_TOKEN`
- `ACCESS_TOKEN_SECRET`

If you're using a different printer to POS58 then export the vendor id and product id as environmental values.

- `ID_VENDOR`
- `ID_PRODUCT`

<br>

### Run

`python3 poller.py`

<br>

### License

MIT.
