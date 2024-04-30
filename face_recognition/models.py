from django.db import models

class FaceRecognitionEntity(models.Model):
    fileName = models.CharField(max_length=255)
    savedFileName = models.CharField(max_length=255)
    uploadDateAndTime = models.DateTimeField()
    recognizedNames = models.CharField(max_length=255)
    nextAction = models.CharField(max_length=255)

class Meta:
        db_table = 'face_recognition_table'