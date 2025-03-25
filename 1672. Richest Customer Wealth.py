
def maximumWealth(accounts: list[list[int]]) -> int:

    wealth = []
    for account in accounts:
        total = 0
        total = sum(account)
        wealth.append(total)
    return max(wealth)


accounts = [[1, 5], [7, 3], [3, 5]]
print(maximumWealth(accounts))
