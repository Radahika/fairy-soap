from flask import Flask, redirect, url_for, render_template
import OpenTokSDK

app = Flask(__name__)

app.config.from_object(__name__)

api_key = "44957712"
api_secret = "108189ddd501fdf197903f725ac87fb7fda5c5ae"

opentok_sdk = OpenTokSDK.OpenTokSDK(api_key, api_secret)

if __name__ == '__main__':
    app.run()
