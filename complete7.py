from flask import Flask, render_template_string, request, redirect, url_for
from os import listdir, path
import os
import re
import base64
import mimetypes

app = Flask(__name__)
img_directory = ""
img_list = []
current_img = 0

DIRECTORY_FORM_HTML = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Select Directory</title>
    </head>
    <body>
        <h1>Select Image Directory</h1>
        <form method="POST">
            <input type="text" name="img_directory" placeholder="Enter the image directory" required>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
'''

IMAGE_VIEW_HTML = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Image Viewer</title>
    </head>
    <body>
        <img src="{{ img_path }}" alt="image" width="30%">
        <form method="POST">
            <textarea name="img_description" rows="4" cols="50" placeholder="Enter a description">{{ img_description }}</textarea>
            <input type="submit" value="Save and Next">
        </form>
    </body>
</html>
'''

def image_to_base64(img_path):
    with open(img_path, "rb") as f:
        image_data = f.read()
    mime_type, _ = mimetypes.guess_type(img_path)
    return f"data:{mime_type};base64," + base64.b64encode(image_data).decode()

def read_txt_content(txt_filepath):
    with open(txt_filepath, "r") as f:
        return f.read()

@app.route("/", methods=["GET", "POST"])
def home():
    global img_directory, img_list, current_img
    if request.method == "POST":
        img_directory = request.form["img_directory"]
        try:
            img_list = [i for i in listdir(img_directory) if re.search(r'\.(png|jpg|jpeg|gif)$', i, re.IGNORECASE)]
            return redirect(url_for("image_view"))
        except FileNotFoundError:
            return "Invalid image directory, please try again.<br><a href='/'>Go back</a>"
    return render_template_string(DIRECTORY_FORM_HTML)

@app.route("/image", methods=["GET", "POST"])
def image_view():
    global img_list, current_img
    if request.method == "POST":
        description = request.form["img_description"]
        txt_filename = path.splitext(img_list[current_img])[0] + ".txt"
        with open(path.join(img_directory, txt_filename), "w") as f:
            f.write(description)
        current_img += 1
        if current_img >= len(img_list):
            current_img = 0
    if img_list:
        img_path = os.path.join(img_directory, img_list[current_img])
        base64_image = image_to_base64(img_path)
        
        img_description = ""
        txt_filepath = path.join(img_directory, path.splitext(img_list[current_img])[0] + ".txt")
        if path.exists(txt_filepath):
            img_description = read_txt_content(txt_filepath)
        
        return render_template_string(IMAGE_VIEW_HTML, img_path=base64_image, img_description=img_description)
    else:
        return "No images found in the directory.<br><a href='/'>Go back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8881)