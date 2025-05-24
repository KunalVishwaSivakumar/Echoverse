# main.py

from agents.story_architect import StoryArchitectAgent
from agents.character_agent import CharacterAgent
from agents.visual_director import VisualDirectorAgent
from agents.soundtrack_agent import SoundtrackAgent
from agents.audience_simulation_agent import AudienceSimulationAgent
from agents.remix_agent import RemixAgent

# Simulated user input
user_prompt = "The day I met my evil clone in Times Square"
character_name = "Evil Clone"
personality = "manipulative, unpredictable"
audience_type = "sci-fi fans"

def main():
    print("🧠 Initializing EchoVerse Agent Flow...")

    # 1. Story Architect
    architect = StoryArchitectAgent(user_prompt)
    story = architect.craft_story()
    print("\n📖 Story Script:\n", story["script"])

    # 2. Character Agent
    character_agent = CharacterAgent(character_name, personality)
    character_line = character_agent.act_in_scene(story["script"])
    print("\n🎭 Character Dialogue:\n", character_line)

    # 3. Visual Director
    visual_agent = VisualDirectorAgent()
    visual_description = visual_agent.generate_scene_description(story["script"])
    print("\n🎬 Visual Description:\n", visual_description)

    # 4. Soundtrack Agent
    music_agent = SoundtrackAgent()
    soundtrack = music_agent.suggest_music(story["script"])
    print("\n🎵 Soundtrack Suggestion:\n", soundtrack)

    # 5. Audience Simulation
    audience_agent = AudienceSimulationAgent(audience_type)
    audience_feedback = audience_agent.evaluate_reaction(story["script"])
    print("\n👥 Audience Feedback:\n", audience_feedback)

    # 6. Remix Agent
    remix_agent = RemixAgent()
    remixed = remix_agent.remix_story(story["script"], remix_type="dark comedy")
    print("\n🔁 Remixed Version:\n", remixed)

if __name__ == "__main__":
    main()
