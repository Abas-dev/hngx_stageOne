from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request

class StageOneTask(GenericAPIView):

    def get(self,request:Request):
        ...