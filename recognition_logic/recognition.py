import face_recognition
import os
import sys
from PIL import Image, ImageDraw


class Recognizer:
    def picture_face_recognition(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        return (image, face_locations)

    def mark_faces(self, loaded_image, face_coordinates, destination):
        image = Image.fromarray(loaded_image)
        draw = ImageDraw.Draw(image)

        for (top, right, bottom, left) in face_coordinates:
            draw.rectangle(
                ((left, top), (right, bottom)), outline=(255, 69, 0), width=5
            )

        del draw
        image.save(destination)

    def recognition_runner(self, input_path, output_path):
        if not os.path.exists(input_path):
            print("f[ERROR] there is no directory '{input_path}'")
            sys.exit()
        else:
            images = os.listdir(input_path)
            for image_path in images:
                image, face_coordinates = self.picture_face_recognition(
                    f"{input_path}/{image_path}"
                )
                destination = f"{output_path}/marked_{image_path}"
                self.mark_faces(image, face_coordinates, destination)

    def main(self):
        self.recognition_runner("input_images", "output_images")


if __name__ == "__main__":
    Recognizer().main()
