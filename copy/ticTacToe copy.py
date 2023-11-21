import numpy as np
import pickle

BOARD_ROWS = 4
BOARD_COLS = 4
BOARD_LAYERS = 4

class State:
    def __init__(self, p1, p2):
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS, BOARD_LAYERS))
        self.p1 = p1
        self.p2 = p2
        self.isEnd = False
        self.boardHash = None
        # init p1 plays first
        self.playerSymbol = 1
    
    # get unique hash of current board state
    def getHash(self):
        self.boardHash = str(self.board.reshape(BOARD_COLS*BOARD_ROWS*BOARD_LAYERS))
        return self.boardHash
    
    def writeGameStates(self, game_number):
        with open(f'game_states_{game_number}.txt', 'w') as file:
            for state in self.states:
                file.write(state + '\n')
    
    def winner(self):
        # vertical
        for x in range(BOARD_ROWS):
            for y in range(BOARD_COLS):
                if sum(self.board[x, y, :]) == 4:
                    self.isEnd = True
                    return 1
                if sum(self.board[x, y, :]) == -4:
                    self.isEnd = True
                    return -1
        # horizontal y
        for x in range(BOARD_ROWS):
            for z in range(BOARD_LAYERS):
                if sum(self.board[x, :, z]) == 4:
                    self.isEnd = True
                    return 1
                if sum(self.board[x, :, z]) == -4:
                    self.isEnd = True
                    return -1
        # horizontal x
        for y in range(BOARD_COLS):
            for z in range(BOARD_LAYERS):
                if sum(self.board[:, y, z]) == 4:
                    self.isEnd = True
                    return 1
                if sum(self.board[:, y, z]) == -4:
                    self.isEnd = True
                    return -1

        # Diagonals from cube corner to cube corner
        diag_sum1 = sum([self.board[i, i, i] for i in range(BOARD_COLS)])
        diag_sum2 = sum([self.board[i, BOARD_COLS - i - 1, i] for i in range(BOARD_COLS)])
        diag_sum3 = sum([self.board[i, i, BOARD_LAYERS - i - 1] for i in range(BOARD_COLS)])
        diag_sum4 = sum([self.board[i, BOARD_COLS - i - 1, BOARD_LAYERS - i - 1] for i in range(BOARD_COLS)])
        
        if any(val == 4 for val in [diag_sum1, diag_sum2, diag_sum3, diag_sum4]):
            self.isEnd = True
            return 1
        if any(val == -4 for val in [diag_sum1, diag_sum2, diag_sum3, diag_sum4]):
            self.isEnd = True
            return -1

        # Diagonals from cube edge to cube edge (24 of them)
        diag_sums = []
        for i in range(BOARD_COLS):
            diag_sums.append(sum([self.board[i, j, k] for j, k in zip(range(BOARD_COLS), range(BOARD_LAYERS))]))
            diag_sums.append(sum([self.board[i, j, k] for j, k in zip(range(BOARD_COLS - 1, -1, -1), range(BOARD_LAYERS))]))
            diag_sums.append(sum([self.board[j, i, k] for j, k in zip(range(BOARD_COLS), range(BOARD_LAYERS))]))
            diag_sums.append(sum([self.board[j, i, k] for j, k in zip(range(BOARD_COLS - 1, -1, -1), range(BOARD_LAYERS))]))
            diag_sums.append(sum([self.board[k, j, i] for j, k in zip(range(BOARD_COLS), range(BOARD_LAYERS))]))
            diag_sums.append(sum([self.board[k, j, i] for j, k in zip(range(BOARD_COLS - 1, -1, -1), range(BOARD_LAYERS))]))

        if any(val == 4 for val in diag_sums):
            self.isEnd = True
            return 1
        if any(val == -4 for val in diag_sums):
            self.isEnd = True
            return -1

        # tie
        # no available positions
        if len(self.availablePositions()) == 0:
            self.isEnd = True
            return 0

        # not end
        self.isEnd = False
        return None

    
    def availablePositions(self):
        positions = []
        for x in range(BOARD_ROWS):
            for y in range(BOARD_COLS):
                for z in range(BOARD_LAYERS):
                    if self.board[x,y,z] == 0:
                        positions.append([x,y,z])  # need to be tuple
        return positions
    
    def updateState(self, position):
        self.board[position] = self.playerSymbol
        # switch to another player
        self.playerSymbol = -1 if self.playerSymbol == 1 else 1
    
    # only when game ends
    def giveReward(self):
        result = self.winner()
        # backpropagate reward
        if result == 1:
            self.p1.feedReward(1)
            self.p2.feedReward(0)
        elif result == -1:
            self.p1.feedReward(0)
            self.p2.feedReward(1)
        else:
            self.p1.feedReward(0.1)
            self.p2.feedReward(0.5)
    
    # board reset
    def reset(self):
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS, BOARD_LAYERS))
        self.boardHash = None
        self.isEnd = False
        self.playerSymbol = 1
    
    def play(self, rounds=100):
        for i in range(rounds):
            if i%1000 == 0:
                print("Rounds {}".format(i))
            while not self.isEnd:
                # Player 1
                positions = self.availablePositions()
                p1_action = self.p1.chooseAction(positions, self.board, self.playerSymbol)
                # take action and upate board state
                self.updateState(p1_action)
                board_hash = self.getHash()
                self.p1.addState(board_hash)
                # check board status if it is end

                win = self.winner()
                if win is not None:
                    # self.showBoard()
                    # ended with p1 either win or draw
                    self.giveReward()
                    self.p1.reset()
                    self.p2.reset()
                    self.reset()
                    break

                else:
                    # Player 2
                    positions = self.availablePositions()
                    p2_action = self.p2.chooseAction(positions, self.board, self.playerSymbol)
                    self.updateState(p2_action)
                    board_hash = self.getHash()
                    self.p2.addState(board_hash)
                    
                    win = self.winner()
                    if win is not None:
                        # self.showBoard()
                        # ended with p2 either win or draw
                        self.giveReward()
                        self.p1.reset()
                        self.p2.reset()
                        self.reset()
                        break
    
    # play with human
    def play2(self):
        while not self.isEnd:
            # Player 1
            positions = self.availablePositions()
            p1_action = self.p1.chooseAction(positions, self.board, self.playerSymbol)
            # take action and upate board state
            self.updateState(p1_action)
            self.showBoard()
            # check board status if it is end
            win = self.winner()
            if win is not None:
                if win == 1:
                    print(self.p1.name, "wins!")
                else:
                    print("tie!")
                self.reset()
                break

            else:
                # Player 2
                positions = self.availablePositions()
                p2_action = self.p2.chooseAction(positions)

                self.updateState(p2_action)
                self.showBoard()
                win = self.winner()
                if win is not None:
                    if win == -1:
                        print(self.p2.name, "wins!")
                    else:
                        print("tie!")
                    self.reset()
                    break

    def showBoard(self):
        # p1: x  p2: o
        # for z in range(0, BOARD_LAYERS):
        #     print('________________________')    
        #     for x in range(0, BOARD_ROWS):
        #         print('-------------')
        #         out = '| '
        #         for y in range(0, BOARD_COLS):
        #             if self.board[x, y,z] == 1:
        #                 token = 'x'
        #             if self.board[x, y,z] == -1:
        #                 token = 'o'
        #             if self.board[x, y,z] == 0:
        #                 token = ' '
        #             out += token + ' | '
        #         print(out)
        #     print('-------------')   
        print(self.board) 


class Player:
    def __init__(self, name, exp_rate=0.8):
        self.name = name
        self.states = []  # record all positions taken
        self.lr = 0.2
        self.exp_rate = exp_rate
        self.decay_gamma = 0.9
        self.states_value = {}  # state -> value
    
    def getHash(self, board):
        boardHash = str(board.reshape(BOARD_COLS*BOARD_ROWS*BOARD_LAYERS))
        return boardHash
    
    def chooseAction(self, positions, current_board, symbol):
        if np.random.uniform(0, 1) <= self.exp_rate:
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            value_max = -999
            for p in positions:
                x, y, z = p
                next_board = current_board.copy()
                next_board[x, y, z] = symbol  # Update the position with the player symbol
                next_boardHash = self.getHash(next_board)
                value = 0 if self.states_value.get(next_boardHash) is None else self.states_value.get(next_boardHash)
                if value >= value_max:
                    value_max = value
                    action = (x, y, z)
        return action
    
    # append a hash state
    def addState(self, state):
        self.states.append(state)
    
    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        for st in reversed(self.states):
            if self.states_value.get(st) is None:
                self.states_value[st] = 0
            self.states_value[st] += self.lr*(self.decay_gamma*reward - self.states_value[st])
            reward = self.states_value[st]
            
    def reset(self):
        self.states = []
        
    def savePolicy(self):
        fw = open('policy_' + str(self.name), 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()

    def loadPolicy(self, file):
        fr = open(file,'rb')
        self.states_value = pickle.load(fr)
        fr.close()


class HumanPlayer:
    def __init__(self, name):
        self.name = name

    def chooseAction(self, positions):
        while True:
                lay = int(input("Input your action lay:"))
                row = int(input("Input your action row:"))
                col = int(input("Input your action col:"))
                action = (lay, row, col)

                if [lay,row,col] in positions:
                    return action
                else:
                    print("Invalid Input")

    # append a hash state
    def addState(self, state):
        pass

    # at the end of the game, backpropagate and update states value
    def feedReward(self, reward):
        pass

    def reset(self):
        pass




if __name__ == "__main__":
    # training
    p1 = Player("p1")
    p2 = Player("p2")

    st = State(p1, p2)
    print("training...")
    st.play(2000)

    p1.savePolicy()
    p2.savePolicy()
    print("saved successfully")

    # play with human
    p1 = Player("computer", exp_rate=0)
    p1.loadPolicy("policy_p1")

    p2 = HumanPlayer("human")

    st = State(p1, p2)
    st.play2()
