class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        conteo_s = {}
        conteo_t = {}

        for letra in s:
            if letra in conteo_s:
                conteo_s[letra] = conteo_s[letra] + 1
            else:
                conteo_s[letra] = 1
        for letra in t:
            if letra in conteo_t:
                conteo_t[letra] = conteo_t[letra] + 1
            else:
                conteo_t[letra] = 1
        return conteo_s == conteo_t