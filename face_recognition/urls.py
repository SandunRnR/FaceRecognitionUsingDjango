from django.urls import path
from . import views

urlpatterns = [
    path('upload_image/', views.upload_image, name='upload_image'),
    path('send_details/', views.send_details, name='send_details'),
    path('get_all_data/', views.get_all_data, name='get_all_data'),
    path('first-anjali-profile/', views.first_anjali_profile, name='first_anjali_profile'),
    path('update-face-recognition-table/', views.update_face_recognition_table, name='update_face_recognition_table'),
    path('recognized_names/<int:id>/', views.recognized_names_by_id, name='recognized_names_by_id'),
    # Add other URL patterns if needed
]
