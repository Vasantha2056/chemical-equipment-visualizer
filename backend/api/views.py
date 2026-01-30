from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

from .models import Equipment

@api_view(['POST'])
def upload_csv(request):
    try:
        csv_file = request.FILES.get('file')

        if not csv_file:
            return Response({"error": "No file uploaded"}, status=400)

        df = pd.read_csv(csv_file)

        # Clear old data
        Equipment.objects.all().delete()

        for _, row in df.iterrows():
            Equipment.objects.create(
                name=row['Equipment Name'],
                type=row['Type']
            )

        return Response({"message": "CSV uploaded successfully"})

    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def equipment_list(request):
    data = Equipment.objects.values('name', 'type')
    return Response(data)
