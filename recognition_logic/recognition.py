import face_recognition
import os
import sys
from PIL import Image, ImageDraw


class Recognizer:
    def picture_face_recognition(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        if face_locations:
            print(f"The face is detected on image '{image_path}'.")
            return (image, face_locations)
        else:
            print("There is no face on this image.")

    def mark_faces(self, loaded_image, face_coordinates, destination):
        image = Image.fromarray(loaded_image)
        draw = ImageDraw.Draw(image)

        for (top, right, bottom, left) in face_coordinates:
            draw.rectangle(
                ((left, top), (right, bottom)), outline=(255, 69, 0), width=5
            )

        del draw
        image.save(destination)

    def compare_two_faces(self, loaded_img1, loaded_img2):
        img1_encoding = face_recognition.face_encodings(loaded_img1)[0]
        img2_encoding = face_recognition.face_encodings(loaded_img2)[0]
        result = face_recognition.compare_faces([img1_encoding], img2_encoding)

        if result[0]:
            print("There is the same person on the images.")
        else:
            print("There are different peoples on the images.")
        return result

    def recognition_run(self, input_path, output_path):
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

    def train_model_with_images(self, name, input_path):
        known_encodings = []
        images = os.listdir(input_path)
        for image_path in images:
            image = face_recognition.load_image_file(f"{input_path}/{image_path}")
            encoding = face_recognition.face_encodings(image)[0]
            if len(known_encodings) == 0:
                known_encodings.append(encoding)
            else:
                for item in range(0, len(known_encodings)):
                    result = face_recognition.compare_faces(
                        [encoding], known_encodings[item]
                    )
                    if result[0]:
                        known_encodings.append(encoding)
                        print("The same person!")
                        break
                    else:
                        print("Another person!")
                        break

        data = {"name": name, "encoding": known_encodings}
        return data

    def main(self):
        pass
        # self.recognition_run("input_images", "output_images")

        # self.picture_face_recognition("input_images/laptop_1.jpeg")

        # img1, coordinates1 = self.picture_face_recognition("input_images/laptop_1.jpeg")
        # img2, coordinates2 = self.picture_face_recognition("input_images/jobs_1.jpg")
        # self.compare_two_faces(img1, img2)

        # print(self.train_model_with_images("Elon", "input_images"))


if __name__ == "__main__":
    Recognizer().main()
