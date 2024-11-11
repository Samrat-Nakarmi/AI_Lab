class VacuumAgent:
    def __init__(self):
        self.position = 'A'  # starting position
        self.room_state = {'A': 'dirty', 'B': 'clean'}

    def perceive(self):
        return self.room_state[self.position]

    def act(self):
        if self.perceive() == 'dirty':
            self.room_state[self.position] = 'clean'
            return "Clean"
        else:
            self.position = 'B' if self.position == 'A' else 'A'
            return "Move"

agent = VacuumAgent()
for _ in range(4):
    print(agent.act())
