from appwrite.client import Client
import os


# This is your Appwrite function
# It's executed each time we get a request
def main(context):
    context.log(context.req.body_json)
    return context.res.json(context.req.body_json)
