# Channel Desk

Local operating desk for a USA and UK YouTube research slate. It ranks 100 differentiated channel opportunities, stores the public evidence behind the scores, and refuses to mark a video scheduled when quality control or account access is missing.

Nothing in this repository creates a YouTube channel, uploads a video, or reports revenue. Those actions need the owner's Google account and a finished master file.

## Run

```bash
python3 -m ops --host 0.0.0.0 --port 8080
```

Open `http://127.0.0.1:8080`.

## Checks

```bash
python3 -m unittest discover -s tests -v
```

The desk uses the Python standard library only.
