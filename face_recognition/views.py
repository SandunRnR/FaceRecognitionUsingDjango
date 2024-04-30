from django.http import JsonResponse
from .services import FaceRecognitionService
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        try:
            file = request.FILES['file']
            next_action = request.POST['nextAction']
            result = FaceRecognitionService().upload_image(file, next_action)
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

@csrf_exempt
def send_details(request):
    if request.method == 'POST':
        try:
            data = request.POST
            file_name = data.get('fileName')
            recognized_names = data.get('recognizedNames')
            next_action = data.get('nextAction')
            result = FaceRecognitionService().save_data(file_name, recognized_names, next_action)
            return JsonResponse({"message": result})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

def get_all_data(request):
    try:
        all_data = list(FaceRecognitionEntity.objects.all().values())
        return JsonResponse(all_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def first_anjali_profile(request):
    try:
        anjali_profile = FaceRecognitionEntity.objects.filter(nextAction='Anjali', recognizedNames='').first()
        return JsonResponse(anjali_profile)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def update_face_recognition_table(request):
    if request.method == 'PUT':
        try:
            data = request.POST
            id = data.get('id')
            recognized_names = data.get('recognizedNames')
            next_action = data.get('nextAction')
            result = FaceRecognitionService().update_face_recognition(id, recognized_names, next_action)
            return JsonResponse({"message": result})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only PUT method allowed"}, status=405)

def recognized_names_by_id(request, id):
    try:
        recognized_names = FaceRecognitionService().get_recognized_names_by_id_and_next_action(id, "Rukshan")
        return JsonResponse({"recognized_names": recognized_names})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
