from appwrite.client import Client
from youtube_transcript_api import YouTubeTranscriptApi
import os


# This is your Appwrite function
# It's executed each time we get a request
def main(context):
    # Why not try the Appwrite SDK?
    #
    # client = (
    #     Client()
    #     .set_endpoint("https://cloud.appwrite.io/v1")
    #     .set_project(os.environ["APPWRITE_FUNCTION_PROJECT_ID"])
    #     .set_key(os.environ["APPWRITE_API_KEY"])
    # )

    # The `ctx.req` object contains the request data
    if context.req.method == "GET":
        video_id = context.req.query["video_id"]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        context.log(transcript)
        # Send a response with the res object helpers
        # `ctx.res.send()` dispatches a string back to the client
        return context.res.json(transcript)

    # `ctx.res.json()` is a handy helper for sending JSON
    return context.res.json(
        {
            "motto": "Build like a team of hundreds_",
            "learn": "https://appwrite.io/docs",
            "connect": "https://appwrite.io/discord",
            "getInspired": "https://builtwith.appwrite.io",
        }
    )
