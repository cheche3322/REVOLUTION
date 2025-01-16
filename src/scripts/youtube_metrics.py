from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY, CHANNEL_ID

# Initialize YouTube Data API
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Function to get YouTube channel statistics
def get_channel_stats(channel_id=CHANNEL_ID):
    request = youtube.channels().list(
        part='statistics',
        id=channel_id
    )
    response = request.execute()
    stats = response['items'][0]['statistics']
    return stats

# Fetch channel statistics
if __name__ == "__main__":
    stats = get_channel_stats()
    print("Subscribers:", stats['subscriberCount'])
    print("Views:", stats['viewCount'])
    print("Videos:", stats['videoCount'])
