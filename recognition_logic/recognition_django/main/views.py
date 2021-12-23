from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import sys

sys.path.append("../../")
from recognition_logic.recognition import Recognizer
from .models import Image


def main(request):
    return render(request, template_name="main/base.html", context={})


def find_faces(request):
    if request.method == "POST" and request.FILES["upload"]:
        upload = request.FILES["upload"]
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        result = Recognizer().recognition_run_for_one_picture(
            f"/home/valentyn/Documents/csdt-cherkasovvs-2122/recognition_logic/recognition_django{file_url}",
            f"/home/valentyn/Documents/csdt-cherkasovvs-2122/recognition_logic/recognition_django/media/marked_{file}",
        )
        img = Image.objects.create(
            title=file_url,
            face_location=str(result),
            output_location=f"/media/marked_{file}",
        )
        return render(
            request,
            "main/find_faces.html",
            {"file_url": file_url, "result_image": img.output_location},
        )
    return render(request, "main/find_faces.html")


def compare_faces(request):
    if (
        request.method == "POST"
        and request.FILES["upload1"]
        and request.FILES["upload2"]
    ):
        upload1 = request.FILES["upload1"]
        upload2 = request.FILES["upload2"]
        fss = FileSystemStorage()
        file1 = fss.save(upload2.name, upload1)
        file_url1 = fss.url(file1)
        file2 = fss.save(upload2.name, upload2)
        file_url2 = fss.url(file2)
        result = Recognizer().compare_for_server(
            f"/home/valentyn/Documents/csdt-cherkasovvs-2122/recognition_logic/recognition_django{file_url1}",
            f"/home/valentyn/Documents/csdt-cherkasovvs-2122/recognition_logic/recognition_django{file_url2}",
        )
        return render(request, "main/compare_faces.html", {"result": result[0]})
    return render(request, "main/compare_faces.html")


def video_detection(request):
    if request.method == "POST" and request.FILES["upload"]:
        upload = request.FILES["upload"]
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        Recognizer().detect_person_in_video(
            f"/home/valentyn/Documents/csdt-cherkasovvs-2122/recognition_logic/recognition_django{file_url}"
        )
        return render(request, "main/video_detection.html", {"file_url": file_url})
    return render(request, "main/video_detection.html")
