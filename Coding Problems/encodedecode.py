class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string."""
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str):
        """Decodes a single string to a list of strings."""
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            res.append(s[j + 1 : j + 1 + word_len])
            i = j + 1 + word_len
        return res