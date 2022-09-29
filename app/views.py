from .models import Todo
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

@api_view(["GET","POST"])
def get_todo(request):
    
    if request.method == "GET":
        todo_obj = Todo.objects.all()
        serializer = TodoSerializer(todo_obj, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

@api_view(["PUT", "GET"])
def put_todo(request):

    try:
        data = request.data
        todo = Todo.objects.get(id=data.get('id'))
        serializer = TodoSerializer(todo,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(["PATCH"])
def patch_todo(request):
    try:
        data = request.data
        todo = Todo.objects.get(id=data.get('id'))
        
        serializer  = TodoSerializer(todo, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_todo(request):
    data  = request.data
    todo = Todo.objects.get(id=data.get('id'))
    todo.delete()
    return Response({"status": "Todo Deleted!!"})


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            
            user = User.objects.get(username = serializer.data['username'])
            token_obj ,_ = Token.objects.get_or_create(user=user)
            return Response({'status': 200,"payload": serializer.data, "token": str(token_obj), "message": "Your data is saved"})
        else:
            return Response({'status': 403, "errors":serializer.errors, "message": "Something went wrong"})


