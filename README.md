# Language Detection Model - README

## Introduction
This repository contains a language detection model that can identify the language of a given text. The model was trained on Google Colab, and the resulting model was then deployed as a FastAPI web application using Docker. The app is hosted on Liara, a platform similar to Heroku. You can access the deployed app at the following link: [Language Detection App](https://language-detection-app.iran.liara.run/).

## Model Training
The language detection model was created using the following Colab notebook: [Colab Notebook](https://colab.research.google.com/drive/1uaALcaatvxOu42IhQA4r0bahfdpw-Z7v?usp=sharing).

## FastAPI App
To use the language detection model, we created a FastAPI application that exposes an API endpoint for language detection. The API accepts text input and returns the predicted language.

## Dockerization
The FastAPI app was dockerized using the provided Dockerfile. This ensures that the app and its dependencies are encapsulated within a container, making it easy to deploy and run consistently across different environments.

## Deployment
The dockerized app is deployed on [Liara](https://liara.ir/), a platform that simplifies the deployment of web applications. It provides a seamless hosting solution for running the language detection app.
You follow [this](https://docs.liara.ir/app-deploy/docker/cli) insturnction to create your own API.



## How to Use the Language Detection App
To use the language detection app, simply make a POST request to the following endpoint:

You can use the link below to detect the language:

https://language-detection-app.iran.liara.run/detect-language

Or make a post request using the link below:

https://language-detection-app.iran.liara.run/detect-language/predict

The request body should contain the text you want to detect, provided in JSON format:

```json
{
  "text": "Enter your text here"
}
```
The API will respond with the predicted language in JSON format:
```json
{
  "language": "English"
}
```
