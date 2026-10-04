class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        visto = set()

        for numero in nums:
            if numero in visto:
                return True
            else:
                visto.add(numero)
        return False