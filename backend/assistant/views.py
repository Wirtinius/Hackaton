from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import transcribe_audio, generate_answer


class GenerateView(APIView):
    def post(self, request):
        audio_file = request.FILES.get("audio_file")
        
        if not audio_file:
            return Response({"error": "No audio file provided."}, status=400)

        transcription = transcribe_audio(audio_file)
        
        function, args = generate_answer(transcription)
        
        return Response({"function": function, "args": args})


def video(request):
    return render(request, "WEB_UIKITS.html")
