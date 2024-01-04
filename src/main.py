from pathlib import Path
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

with open(Path.cwd()/"src"/"lost_debit_card.wav","rb") as audio_file:
  transcript = openai.Audio.transcribe("whisper-1",audio_file)
  #print(transcript)

  response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
          {"role": "system", "content": "You are a sentiment classification bot, print out if the user is happy or sad"},
          {"role": "user", "content": transcript.text}
      ],
      temperature=0.7,
      max_tokens=150,
  )

  response_message = response["choices"][0]["message"]
  print(response_message)