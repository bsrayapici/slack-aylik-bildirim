import os
import sys
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

MESAJ = ":memo: *Aylik takip dokumani hatirlatmasi* - Orhan Bey'in sunumu icin. Dokuman: <https://docs.google.com/presentation/d/16XJ7Tu98OErNzDe9FnYxvoYYlCRnrqjf/edit|Sunuma git> \n:sparkles: Iyi sunumlar!"

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

if not WEBHOOK_URL:
    print("Error: SLACK_WEBHOOK_URL is not set in environment", file=sys.stderr)
    sys.exit(1)

try:
    bugun = datetime.now(ZoneInfo("Europe/Istanbul"))
except Exception as e:
    # Fallback to UTC if ZoneInfo is unavailable for some Python versions/environments
    print(f"Warning: unable to set timezone Europe/Istanbul: {e}. Using UTC.", file=sys.stderr)
    from datetime import timezone
    bugun = datetime.now(timezone.utc)

# True when today is Tuesday (weekday()==1) and it's within the first 7 days of the month
ilk_sali_mi = (bugun.weekday() == 1) and (bugun.day <= 7)

if ilk_sali_mi:
    try:
        yanit = requests.post(WEBHOOK_URL, json={"text": MESAJ}, timeout=15)
        yanit.raise_for_status()
    except requests.RequestException as e:
        print(f"Mesaj gonderilirken hata olustu: {e}", file=sys.stderr)
        sys.exit(2)
    print(f"Mesaj gonderildi: {bugun.date()}")
else:
    print(f"Bugun gonderim yok ({bugun.date()})")
