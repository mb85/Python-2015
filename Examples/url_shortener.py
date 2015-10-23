#!/usr/bin/env python3
# coding: utf-8

import sys
import requests

with open("api_key") as f:
    API_KEY = f.read()


def main():
    args = sys.argv[1:]
    if args:
        long_url = args[0]
        base_url = "https://www.googleapis.com/urlshortener/v1/url"

        data = {
            "longUrl": long_url
        }

        params = {
            "key": API_KEY
        }

        try:
            resp = requests.post(base_url, json=data, params=params)
            resp_data = resp.json()

            if resp.status_code == 200:
                print(resp_data.get("id", ""))

            else:
                err_data = resp_data.get("error")
                code = err_data.get("code", "")
                message = err_data.get("message", "")
                print("Error: {} {}".format(code, message), file=sys.stderr)
                return 1

        except requests.RequestException as e:
            print(e.strerror if e.strerror else "")
            return 1

if __name__ == '__main__':
    raise SystemExit(main())
