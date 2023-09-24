import os

import openai
from django.core.files.storage import FileSystemStorage


openai.api_key = "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"


def transcribe_audio(audio_file):    
    FileSystemStorage().save("uploads/audio.wav", audio_file)

    with open("uploads/audio.wav", "rb") as f:
        response = openai.Audio.transcribe(
            model="whisper-1",
            file=f,
            response_format="text",
            language="ru",
        )

        f.close()

        os.remove("uploads/audio.wav")

        return response


def generate_answer(transcript: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Your name is Jerry. You are pedestrian smartboard. You need to help people with their questions.",
            },
            {
                "role": "user",
                "content": transcript,
            },
        ],
        functions=[
            {
                "name": "get_bus_route",
                "description": "Get the bus route and current locations of the buses",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bus_number": {
                            "type": "integer",
                            "description": "The number of the bus",
                        },
                    },
                    "required": ["bus_number"],
                },
            },
        ],
        max_tokens=300,
    )

    response_message = response["choices"][0]["message"]

    if response_message.get("function_call"):
        function_name = response_message["function_call"]["name"]
        function_args = response_message["function_call"]["arguments"]
        return function_name, function_args
    else:
        message = response_message["content"]
        return "message", message
