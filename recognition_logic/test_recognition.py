import face_recognition
import pytest
from .recognition import Recognizer


@pytest.fixture()
def recognizer():
    yield Recognizer()


class TestRecognizerUnit:
    def test_picture_face_recognition_fails(self, recognizer):
        result = recognizer.picture_face_recognition(
            "testing_resources/input_images/laptop_1.jpeg"
        )
        assert not result

    def test_picture_face_recognition_passes(self, recognizer):
        result = recognizer.picture_face_recognition(
            "testing_resources/input_images/jobs_1.jpg"
        )
        assert len(result) == 2
        assert len(result[1]) == 1
        assert len(result[1][0]) == 4

    def test_picture_multiface_recognition_passes(self, recognizer):
        result = recognizer.picture_face_recognition(
            "testing_resources/input_images/elon_and_exwife.jpeg"
        )
        assert len(result) == 2
        assert len(result[1]) == 2

        for coordinates in result[1]:
            assert len(coordinates) == 4

    def test_compare_two_faces_fails(self, recognizer):
        image1 = face_recognition.load_image_file(
            "testing_resources/input_images/elon_1.jpg"
        )
        image2 = face_recognition.load_image_file(
            "testing_resources/input_images/jobs_1.jpg"
        )
        result = recognizer.compare_two_faces(image1, image2)
        assert not result[0]

    def test_compare_two_faces_passes(self, recognizer):
        image1 = face_recognition.load_image_file(
            "testing_resources/input_images/elon_1.jpg"
        )
        image2 = face_recognition.load_image_file(
            "testing_resources/input_images/elon_3.jpg"
        )
        result = recognizer.compare_two_faces(image1, image2)
        assert result[0]

    def test_train_model_with_images(self, recognizer):
        data = recognizer.train_model_with_images(
            "Elon", "testing_resources/input_elon"
        )
        assert isinstance(data, dict)
        assert len(data) == 2
