from appwrite.client import Client
import os


# This is your Appwrite function
# It's executed each time we get a request
def main(context):
    return context.res.text(context.req.body_text)
