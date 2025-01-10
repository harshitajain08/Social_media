import os
import openai
import asyncio
from aiohttp import ClientSession
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Ensure the API key is available
if not openai_api_key:
    print("API key is missing. Please check your .env file.")
    exit(1)

# Set the OpenAI API key
openai.api_key = openai_api_key

async def fetch_engagement_data(post_type):
    """Simulate fetching engagement data asynchronously."""
    await asyncio.sleep(1)  # Simulating network delay
    # Replace this with actual database fetching logic if needed
    if post_type == 'carousel':
        return {"likes": 150, "shares": 30, "comments": 20}
    elif post_type == 'reels':
        return {"likes": 200, "shares": 50, "comments": 40}
    elif post_type == 'static':
        return {"likes": 100, "shares": 10, "comments": 5}
    else:
        return None

async def generate_insight(avg_likes, avg_shares, avg_comments):
    """Generate insights based on average engagement metrics."""
    prompt = f"Given the following metrics - Average Likes: {avg_likes}, Average Shares: {avg_shares}, Average Comments: {avg_comments}, provide insights."
    
    response = await openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content']

async def main(post_type):
    data = await fetch_engagement_data(post_type)
    
    if data:
        avg_likes = data["likes"]
        avg_shares = data["shares"]
        avg_comments = data["comments"]
        
        insight = await generate_insight(avg_likes, avg_shares, avg_comments)
        
        print(f"Average Likes: {avg_likes}, Average Shares: {avg_shares}, Average Comments: {avg_comments}")
        print(f"Insights: {insight}")
    else:
        print("No data found for the specified post type.")

if __name__ == "__main__":
    post_type_input = input("Enter post type (carousel/reels/static): ")
    asyncio.run(main(post_type_input))