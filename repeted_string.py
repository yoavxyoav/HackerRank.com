# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def repeatedString(s, n):
    factor = n // len(s)
    mod = n % len(s)
    a_count = s.count('a')

    return a_count * factor + s[:mod].count('a')
