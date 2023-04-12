# Enhanced Image Viewer and Description Writer

![Directory Search](img1.png)

Welcome to the improved web-based image viewer and description writer application, crafted using Flask. This application empowers users to choose a directory containing images, seamlessly browse through them, and effortlessly write descriptions. These descriptions are conveniently saved as text files.

## Overview

Our state-of-the-art program provides a user-friendly solution for AI industry professionals to seamlessly manage image-related tasks for their Fiverr gigs. It offers an easy-to-use locally hosted web application enabling users to smoothly attach prompts or descriptions to images.

![Image Labeling Textbox](img2.png)

## Requirements

- Python 3.6 or higher
- Flask package

To install the required Flask package, execute the following command:

```pip install flask```

## Usage Guide

1. Launch the Flask application using this command:

```python app.py```

2. Open your favorite web browser and navigate to: http://localhost:8881

3. Input the desired folder path containing your images and click "Submit".

4. The first image from the folder will appear alongside a form field to enter the description. Add a description and click "Save and Next".

5. The application will store the description as a text file, sharing the same name as the image, and showcase the next image in the folder.

6. Continue the process of adding descriptions to the images. Upon completion, the application will loop back to display the first image.

Designed for versatility, our solution operates seamlessly with any directory, eliminating the need for a specific working directory. This allows users the flexibility to collaborate with various directories and manage their images effectively.

By leveraging this program, you will optimize your Fiverr gig workflow, boost efficiency, and significantly elevate your productivity in a professional and user-friendly manner.

## Customization

Feel free to modify the templates and styles within the Python code. Locate the `DIRECTORY_FORM_HTML` and `IMAGE_VIEW_HTML` variables in the code to edit the templates.

## Contributing

We wholeheartedly welcome contributions that enhance the Image Viewer and Description Writer application! Please create issues or submit pull requests on the project's GitHub repository.

To contribute, kindly follow these steps:

1. Fork the project repository on GitHub.
2. Clone the forked repository to your local computer.
3. Establish a new branch in your local repository for your desired modifications.
4. Implement your changes and commit them to your local repository.
5. Push your changes to your forked repository on GitHub.
6. Initiate a pull request from your forked repository to the main project repository.
7. Await your pull request to be reviewed and, if required, make additional modifications based on the feedback.

By contributing to the project, you agree to license your contributions under the same open-source license as the original project, and grant the project maintainers and other contributors the right to utilize your submitted work.

We sincerely appreciate your interest in contributing to this project and helping us make the Image Viewer and Description Writer application even better!