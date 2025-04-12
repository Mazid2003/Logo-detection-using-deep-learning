# 🔍 Logo Detection Using Deep Learning

A deep learning-based logo detection system that identifies logos in images with high accuracy. This project utilizes a CNN-VGG19 model trained to detect and classify logos, achieving an impressive 94.2% accuracy. The frontend is integrated using Django, allowing users to upload an image and get instant logo detection results.

**✨ Features:**

✅ CNN-VGG19 Model for high-accuracy logo detection

✅ 94.2% Accuracy in identifying logos

✅ User-Friendly Web Interface powered by Django

✅ Detects Genuine & Fake Logos (Only original logos generate an output)

**🔧 Technologies Used:**

Deep Learning: CNN - VGG19

Framework: Django (Python)

Frontend: HTML, CSS, JavaScript

Dataset: Available on Kaggle, Roboflow, and other sources

**📂 Repository Contents:**

model.py – Contains the class names of the dataset in a list

settings.py, urls.py, views.py – Django backend configuration

templates/ – Contains frontend UI for image upload and results display

In this templates folder index.html and style.css file are present

**🚀 How It Works:**

1️⃣ User uploads a logo image through the web interface

2️⃣ The VGG19 model processes the image and identifies the logo

3️⃣ If the logo is genuine, the system displays the result; otherwise, no output is generated

**Screenshots**

**Dataset Evaluation**

![image](https://github.com/user-attachments/assets/a7176c97-68e8-4bbd-8c65-8c72600b26dc) , ![image](https://github.com/user-attachments/assets/79b9102d-27c4-4b07-9642-657f4128548a)

**Methodology**

![image](https://github.com/user-attachments/assets/d82a90fe-7279-4eb8-8410-dc2152edb800)

**Example 1:**

![cnn1](https://github.com/user-attachments/assets/7c4e9841-af46-423f-b33d-e2c4d780ad12)

![cnn2](https://github.com/user-attachments/assets/8810f084-fbd9-459c-aa94-081a98262aaa)

**Example 2:**

![output2 1](https://github.com/user-attachments/assets/ef40a3ea-7dd8-4ffb-94ac-ce45bf230636)

![output2](https://github.com/user-attachments/assets/bcbf371c-9796-4596-94a2-0c8c5e1c513d)

**⚠️ Note:**

Ignore any minor errors and run the exact code to get the results

This project demonstrates the power of deep learning in brand authentication and counterfeit detection. 🚀

**📜 License**

This project is open-source under the MIT License. Feel free to use and
modify it! 🚀
