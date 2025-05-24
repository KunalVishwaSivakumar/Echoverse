# agents/story_architect.py

from google.cloud import aiplatform

class StoryArchitectAgent:
    def __init__(self, user_prompt):
        self.prompt = user_prompt
        self.story_structure = {}
        aiplatform.init(project="echoverse-ai", location="us-central1")

    def craft_story(self):
        model = aiplatform.models.ModelRegistry.get_model(name="gemini-1.0-pro")

        response = model.predict({
            "prompt": f"Turn this idea into a 4-act story: {self.prompt}"
        })

        script = response.text  # Gemini response
        self.story_structure = {
            "genre": "auto-detected",
            "beats": ["intro", "conflict", "twist", "resolution"],
            "script": script
        }
        return self.story_structure
