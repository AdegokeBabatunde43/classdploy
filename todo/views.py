from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from todo.serializer import CustomerSerializer
from todo.models import Customer

# Create your views here.


@api_view(['POST'])
def createtodo(request):
    record= CustomerSerializer(data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)
    

@api_view(['GET'])
def alltodo(request):
    record=Customer.objects.all()
    record = CustomerSerializer(record,many=True)
    return Response(record.data)


@api_view(['DELETE'])
def deletetodo(request, id):
    record=Customer.objects.get(id=id)
    record.delete()
    return Response('totdo deleted successfully')


@api_view(['GET'])
def tododetail(request, id):
    record=Customer.objects.get(id=id)
    info=CustomerSerializer(record, many=False)
    return Response(info.data)


@api_view(['PUT'])
def todoedit(request, id):
    record=Customer.objects.get(id=id)
    info=CustomerSerializer(data=request.data, instance=record)
    if info.is_valid():
        info.save()
        return Response('Upadate Successfully')
    


    