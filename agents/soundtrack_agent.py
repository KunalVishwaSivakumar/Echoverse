# agents/soundtrack_agent.py

from google.cloud import aiplatform

class SoundtrackAgent:
    def __init__(self):
        aiplatform.init(project="echoverse-ai", location="us-central1")
        self.model = aiplatform.models.ModelRegistry.get_model(name="gemini-1.0-pro")

    def suggest_music(self, story_script):
        prompt = f"""
        Based on this story scene, suggest a mood-appropriate music theme or genre.
        Also recommend sound effects if needed.

        Scene:
        {story_script}
        """

        response = self.model.predict({"prompt": prompt})
        return response.text
