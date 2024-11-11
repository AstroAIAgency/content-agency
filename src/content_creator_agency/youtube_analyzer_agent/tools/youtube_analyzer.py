from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import googleapiclient.discovery

class YouTubeAnalyzerTool(BaseTool):
    """
    A tool for analyzing YouTube channels using the YouTube Data API.
    """
    keywords: str = Field(..., description="Keywords to search for competitor channels.")

    def run(self):
        """
        Searches for competitor channels using keywords and analyzes their video statistics.
        """
        api_key = os.getenv("YOUTUBE_API_KEY")
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

        # Search for channels using the provided keywords
        search_request = youtube.search().list(
            part="snippet",
            q=self.keywords,
            type="channel",
            maxResults=5
        )
        search_response = search_request.execute()

        # Collect channel IDs from the search results
        channel_ids = [item['snippet']['channelId'] for item in search_response['items']]

        # Fetch statistics for each channel
        report = []
        for channel_id in channel_ids:
            # Fetch channel details
            channel_request = youtube.channels().list(
                part="snippet,statistics,contentDetails",
                id=channel_id
            )
            channel_response = channel_request.execute()
            channel_info = channel_response.get("items", [])[0]
            channel_title = channel_info["snippet"]["title"]
            subscriber_count = channel_info["statistics"]["subscriberCount"]
            uploads_playlist_id = channel_info["contentDetails"]["relatedPlaylists"]["uploads"]

            # Fetch videos from the uploads playlist
            playlist_request = youtube.playlistItems().list(
                part="snippet,contentDetails",
                playlistId=uploads_playlist_id,
                maxResults=5
            )
            playlist_response = playlist_request.execute()

            # Collect video statistics
            videos = []
            for item in playlist_response['items']:
                video_id = item['contentDetails']['videoId']
                video_request = youtube.videos().list(
                    part="snippet,statistics",
                    id=video_id
                )
                video_response = video_request.execute()
                video_info = video_response.get("items", [])[0]
                video_title = video_info["snippet"]["title"]
                view_count = video_info["statistics"].get("viewCount", 0)
                comment_count = video_info["statistics"].get("commentCount", 0)
                like_count = video_info["statistics"].get("likeCount", 0)

                videos.append({
                    "title": video_title,
                    "views": view_count,
                    "comments": comment_count,
                    "likes": like_count
                })

            report.append({
                "channel_title": channel_title,
                "subscribers": subscriber_count,
                "videos": videos
            })

        return report

if __name__ == "__main__":
    tool = YouTubeAnalyzerTool(keywords="AI technology")
    print(tool.run())
