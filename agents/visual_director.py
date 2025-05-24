# agents/visual_director.py

from google.cloud import aiplatform_v1beta1 as aiplatform

class VisualDirectorAgent:
    def __init__(self):
        aiplatform.init(project="echoverse-ai", location="us-central1")

    def generate_scene_description(self, scene_text):
        model = aiplatform.models.ModelRegistry.get_model(name="gemini-1.0-pro-vision")
        response = model.predict({
            "prompt": f"Generate a vivid visual description or camera angles for:\n{scene_text}"
        })
        return response.text
