# agents/character_agent.py

from google.cloud import aiplatform

class CharacterAgent:
    def __init__(self, character_name, personality):
        self.name = character_name
        self.personality = personality
        aiplatform.init(project="echoverse-ai", location="us-central1")

    def act_in_scene(self, context):
        model = aiplatform.models.ModelRegistry.get_model(name="gemini-1.0-pro")
        prompt = f"Act as {self.name} who is {self.personality}. React to this scene:\n{context}"
        response = model.predict({"prompt": prompt})
        return response.text
