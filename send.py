import os
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

MESAJ = ":soccer: Hey folks!⚽  Your friendly Product reminder service is here — at your command. 🫡"

WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]

bugun = datetime.now(ZoneInfo("Europe/Istanbul"))
ilk_sali_mi = (bugun.weekday() == 1) and (bugun.day <= 7)

if ilk_sali_mi:
    yanit = requests.post(WEBHOOK_URL, json={"text": MESAJ}, timeout=15)
    yanit.raise_for_status()
    print(f"Mesaj gonderildi: {bugun.date()}")
else:
    print(f"Bugun gonderim yok ({bugun.date()})")
