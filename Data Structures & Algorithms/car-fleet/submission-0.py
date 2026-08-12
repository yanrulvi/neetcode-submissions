class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        res = 0

        for i in range(len(position)):
            cars.append((position[i], (target - position[i]) / speed[i]))
        
        cars = sorted(cars, key=lambda x: -x[0])
        
        t = 0
        for car in cars:
            if car[1] > t:
                t = car[1]
                res += 1
        
        return res