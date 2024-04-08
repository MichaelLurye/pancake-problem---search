

class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        #you may add data stractures to improve the search
        self.num_list = [int(num) for num in self.state_str.split(',')]


    #returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1), (pancake _state2, cost2)...]
    def get_neighbors(self):
        neighbors=[]
        for i in range(len(self.num_list)-1, -1, -1):
            state = self.num_list[:i]+self.num_list[i:][::-1]
            cost = sum(self.num_list[i:])
            state_string = ','.join(map(str, state))
            neighbors.append((pancake_state(state_string),cost))
        return neighbors




    #you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    #you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str


    def get_state_str(self):
        return self.state_str

    def get_state_lst(self):
        return self.num_list
