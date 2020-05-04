from rest_framework.views import APIView
from rest_framework.response import Response


class ApiList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, *args, **kwargs):
        res = {"data":"ok"}

        return Response(res)
