class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101  # Years array to count population in each year

        for birth, death in logs:
            for year in range(birth, death):
                years[year - 1950] += 1

        max_population = max(years)
        earliest_year = years.index(max_population) + 1950

        return earliest_year
