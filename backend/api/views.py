from django.http import JsonResponse
from api.serializer import ProductSerializer
from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
 
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer= ProductSerializer(products, many=True)
    # return JsonResponse({
    #     'data': serializer.data
        
    # })
    return Response(serializer.data)