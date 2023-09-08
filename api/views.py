from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from datetime import datetime

class StageOneTask(GenericAPIView):

    def get(self,request:Request):
        slackName = request.GET.get('slack_name','no name set') #getting the slack name from the url 

        trackName = request.GET.get('track','no track set') # getting the track name from the url 

        Day = datetime.now()
        currentDay = Day.strftime("%A") # getting the current day and coverting to string formart

        utcTime = datetime.utcnow()
        utc = utcTime.strftime('%Y-%m-%dT%H:%M:%SZ') # getting the current uct time in string formart

        responseData = {
            "slack_name": slackName,
            "current_day": currentDay,
            "utc_time": utc,
            "track": trackName,
            "github_file_url": "https://github.com/Abas-dev/hngx_stageOne/blob/main/api/views.py",
            "github_repo_url": "https://github.com/Abas-dev/hngx_stageOne.git",
            "status_code": status.HTTP_200_OK
        }

        return Response(data=responseData,status=status.HTTP_200_OK)
    


