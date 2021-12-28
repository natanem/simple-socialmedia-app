from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import serializers, viewsets, permissions

from feed.models import Feed
from feed.api.serializers import FeedSerializer



@csrf_exempt
def feed_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data.user = request.user
        serializer = FeedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def feed_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        feed = Feed.objects.get(pk=pk)
    except Feed.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FeedSerializer(feed)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FeedSerializer(feed, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    if request.method == 'DELETE':
        feed.delete()
        return HttpResponse(status=204)















# @api_view(['GET'])
# def all_feeds(request):
#     if request.method == 'GET':
#         feeds = Feed.objects.all()
#         serializer = FeedSerializer(feeds, many=True)
#         return response(serializer.data)

# @api_view(['GET']):
# def feed(request, pk):
#     try:
#         feed = Feed.objects.get(pk=pk)
#     except Feed.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = FeedSerializer(feed)
#         return Response(serializer.data)

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    authentication_classes =[]
    permission_classes = []

