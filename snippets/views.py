from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@csrf_exempt  # this decorator marks a view as being exempt from the protection ensured by the middleware
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()    # get all snippets from the database
        serializer = SnippetSerializer(snippets, many=True)    # serialize the snippets
        return JsonResponse(serializer.data, safe=False)    # return the serialized snippets as JSON

    elif request.method == 'POST':
        data = JSONParser().parse(request)  # parse the request data into a Python dictionary
        serializer = SnippetSerializer(data=data) # deserialize the data into a Snippet object
        if serializer.is_valid():  # check if the data is valid
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(
            pk=pk)  # get the snippet with the given primary key from the database
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet) # serialize the snippet
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request) # parse the request data into a Python dictionary
        serializer = SnippetSerializer(snippet, data=data) # deserialize the data into a Snippet object
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)  # return the serialized snippet as JSON

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)