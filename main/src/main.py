from youtube_transcript_api import YouTubeTranscriptApi

# This is your Appwrite function
# It's executed each time we get a request
def main(context):
    try:
        # The `ctx.req` object contains the request data
        if context.req.method == "GET":
            videoId = context.req.query.get("videoId")
            
            if videoId is None:
                raise ValueError("videoId parameter is missing")

            transcript = YouTubeTranscriptApi.get_transcript(videoId)

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
    except Exception as e:
        # Handle exceptions here
        error_message = str(e)
        context.log(error_message)
        return context.res.status(500).json({"error": error_message})
