from .models import FaceRecognitionEntity
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, storage
from django.utils.text import slugify

class FaceRecognitionService:
    def __init__(self):
        try:
            # Initialize the Firebase Admin SDK with your service account key
            if not firebase_admin._apps:
                cred = credentials.Certificate("D:\\Sandun\\PythonProjects\\New folder\\Django_Face_Recognition\\face-app-604bc-firebase-adminsdk-nl0o5-cca3d57dd4.json")
                firebase_admin.initialize_app(cred, name='Face App', options={'storageBucket': 'face-app-604bc.appspot.com'})
        except Exception as e:
            print(f"Error initializing Firebase Admin SDK: {str(e)}")

    def upload_image(self, file, next_action):
        try:
            entity = FaceRecognitionEntity(
                fileName=file.name,
                savedFileName=f"{datetime.now()}_{file.name}",
                uploadDateAndTime=datetime.now(),
                recognizedNames="",
                nextAction=next_action
            )
            entity.save()

            # Upload image to Firebase Storage with explicit content type
            bucket = storage.bucket()
            content_type = "image/png" if file.name.lower().endswith(".png") else "image/jpeg"
            blob = bucket.blob("images/" + file.name)  # Specify the path within the bucket
            blob.upload_from_file(file, content_type=content_type)

            return {"id": entity.id}
        except Exception as e:
            return {"error": f"Could not save file: {str(e)}"}

    def save_data(self, file_name, recognized_names, next_action):
        try:
            entity = FaceRecognitionEntity(
                fileName=file_name,
                savedFileName=file_name,
                uploadDateAndTime=datetime.now(),
                recognizedNames=recognized_names,
                nextAction=next_action
            )
            entity.save()
            return "Successfully saved data"
        except Exception as e:
            return f"Could not save data: {str(e)}"

    def update_face_recognition(self, id, recognized_names, next_action):
        try:
            entity = FaceRecognitionEntity.objects.get(id=id)
            entity.recognizedNames = recognized_names
            entity.nextAction = next_action
            entity.save()
            return "Successfully updated"
        except Exception as e:
            return f"Could not update data: {str(e)}"

    def get_recognized_names_by_id_and_next_action(self, id, next_action):
        try:
            entity = FaceRecognitionEntity.objects.get(id=id, nextAction=next_action)
            return entity.recognizedNames
        except Exception as e:
            return f"No data found for the provided ID and next action: {str(e)}"
