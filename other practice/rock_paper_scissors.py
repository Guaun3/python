import random


def play() -> str:
    player = input("please enter either 'r' for rock, 'p' for paper, 's' for scissors, or 'exit' to exit\n").lower()
    if player == "exit":
        return "exit"
    computer = random.choice(['r', 'p', 's'])
    print(f"computer: {computer}\n you: {player}")
    # tie
    if player == computer:
        return "Tie"
    # compare to determine who is the winner
    if rps_helper(player, computer):
        return "You Win!"
    return "You Lost!"


def rps_helper(player: str, comp: str) -> bool:
    """

    Args:
        player: user's choice ('r', 'p', or 's')
        comp: computer's choice ('r', 'p', or 's')

    Returns: ture if the user win, false if user lose
    """
    # r > s, s > p, p > r
    if (player == 'r' and comp == 's') or (player == 's' and comp == 'p') or (player == 'p' and comp == 'r'):
        return True
    return False


if __name__ == "__main__":
    play()
    exit_game = input("Enter 'exit' to exit the game or anything to continue \n")
    while exit_game != "exit":
        result = play()
        if result == "exit":
            break
        print(result)