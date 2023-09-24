import re
import sys
import requests as r

for url in sys.stdin:
    url = url.strip() 

    try:
        c = r.get(url)
        result = c.text
        code = f"{result}"

        comment = "<!--.*?-->"

        match = re.findall(comment, code)

        if match:
            print("\n", "Comments Found ;)", "\n \n \n", url, ":", "\n")

            for i in range(0, len(match)):
                print(match[i])

        else:
            print(url,": No Comments Found :(")

    except Exception as e:
        print(f"Error!")
