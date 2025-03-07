# d - ალფავიტში სიმბოლოების რაოდენობა
d = 256  # ჩვეულებრივ ASCII სიმბოლოებისთვის

# ნიმუშის (pattern) და ტექსტის (text) შერჩევა
def search(pattern, text, prime_modulus):
    m = len(pattern)  # ნიმუშის სიგრძე
    n = len(text)  # ტექსტის სიგრძე
    hash_pattern = 0    # ნიმუშის ჰეშ-მნიშვნელობა
    hash_text = 0    # ტექსტის ქვეწინადის ჰეშ-მნიშვნელობა
    h = 1  # წინასწარი მნიშვნელობა, რომელიც გამოიყენება ჰეშის განახლებისთვის

    # ჰეშ-ის განახლების დაწყება
    for i in range(m-1):
        h = (h*d) % prime_modulus

    # ნიმუშის და პირველი ქვეწინადის ჰეშ-ფუნქციების გამოთვლა
    for i in range(m):
        hash_pattern = (d*hash_pattern + ord(pattern[i])) % prime_modulus
        hash_text = (d*hash_text + ord(text[i])) % prime_modulus

    # ნიმუშის გადაადგილება ტექსტში
    for i in range(n-m+1):
        # თუ ჰეშ-მნიშვნელობები ემთხვევა, შეამოწმე სიმბოლოები
        if hash_pattern == hash_text:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            else:
                print("Pattern found at index " + str(i))

        # შემდეგი ქვეწინადის ჰეშ-ფუნქციის გამოთვლა
        if i < n-m:
            hash_text = (d*(hash_text - ord(text[i])*h) + ord(text[i+m])) % prime_modulus
            if hash_text < 0:
                hash_text = hash_text + prime_modulus

# Driver Code
if __name__ == '__main__':
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"

    prime_modulus = 101

    # ფუნქციის გამოძახება
    search(pattern, text, prime_modulus)
