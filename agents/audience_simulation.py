# agents/audience_simulation_agent.py

from google.cloud import aiplatform

class AudienceSimulationAgent:
    def __init__(self, audience_type="teen_gamers"):
        aiplatform.init(project="echoverse-ai", location="us-central1")
        self.model = aiplatform.models.ModelRegistry.get_model(name="gemini-1.0-pro")
        self.audience_type = audience_type

    def evaluate_reaction(self, story_script):
        prompt = f"""
        You're simulating an audience group: {self.audience_type}.
        How would they react to this story? Suggest changes to make it more engaging for them.

        Story:
        {story_script}
        """

        response = self.model.predict({"prompt": prompt})
        return response.text
