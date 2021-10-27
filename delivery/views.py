from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import BranchSerializer, StatusSerializer, OrderSerializer, UserSerializer
from .models import Branch, Status, Order


class BranchListView(APIView):
    @swagger_auto_schema(responses={200: BranchSerializer})
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BranchSerializer, responses={200: BranchSerializer})
    def post(self, request):
        serializer = BranchSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'result': "Branch was created successfully",
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'data': serializer.errors
            }, status=status.HTTP_404_NOT_FOUND
        )


class StatusListView(APIView):
    @swagger_auto_schema(responses={200: StatusSerializer})
    def get(self, request):
        statuses = Status.objects.all()
        serializer = StatusSerializer(many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderListView(APIView):
    @swagger_auto_schema(responses={200: OrderSerializer})
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OrderSerializer, responses={200: OrderSerializer})
    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'result': "The order was accepted by the customer",
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'result': 'The order wasn\'t accepted by the customer',
                'data': serializer.errors
            }, status=status.HTTP_404_NOT_FOUND
        )


class OrderDetailView(APIView):

    @swagger_auto_schema(responses={200: OrderSerializer})
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OrderSerializer, responses={200: OrderSerializer})
    def put(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: OrderSerializer})
    def delete(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(
            {
                'data': 'Order was deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT
        )
