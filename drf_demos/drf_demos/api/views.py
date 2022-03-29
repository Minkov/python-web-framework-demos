from rest_framework import generics as api_views
from rest_framework import mixins as api_mixins
from rest_framework import permissions
# from rest_framework import views as api_views
from rest_framework import serializers

from drf_demos.api.models import Product, Category


class IdAndNameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class IdAndNameProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')


class FullCategorySerializer(serializers.ModelSerializer):
    product_set = IdAndNameProductSerializer(many=True)

    class Meta:
        model = Category
        # fields = ('id', 'name')
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)
    category = IdAndNameCategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


# class ManualProductsListView(api_views.APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=201)
#         return Response(serializer.errors, status=400)
'''
ListAPIView
RetrieveAPIView
CreateAPIView
DestroyAPIView
UpdateAPIView
'''


class ProductsListView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def list(self, request, *args, **kwargs):
        print(self.request.user)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    # def get_queryset(self):


class CategoriesListView(api_views.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = FullCategorySerializer


class SingleProductView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ExampleView(api_views.ListAPIView, api_mixins.DestroyModelMixin):
    pass
