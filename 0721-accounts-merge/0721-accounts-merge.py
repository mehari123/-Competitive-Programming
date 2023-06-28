from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}  # Map email to the account name
        graph = defaultdict(set)  # Graph to store the connections between emails

        # Build the graph and map each email to its corresponding name
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1])  # Connect each email to the first email in the account
                graph[account[1]].add(email)  # Connect the first email to each other email in the account
                email_to_name[email] = name

        visited = set()  # Set to keep track of visited emails
        merged_accounts = []  # List to store the merged accounts

        # DFS function to explore the connected component of an email
        def dfs(email, component):
            component.append(email)
            visited.add(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        # Perform DFS for each email
        for email in graph:
            if email not in visited:
                component = []  # List to store the emails in the connected component
                dfs(email, component)
                merged_accounts.append([email_to_name[email]] + sorted(component))

        return merged_accounts
