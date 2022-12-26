class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        fahr = (celsius * 9.0/5.0) + 32.0
        kelivin = celsius + 273.15
        arr=[]
        arr.append(kelivin)
        arr.append(fahr)
        return arr
