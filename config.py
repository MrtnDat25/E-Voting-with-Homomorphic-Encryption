import math

# cau hinh demo  e-voting

# 1. define quantity candidates
NUM_CANDIDATES = 4

# 2. define max quantity voters 
MAX_VOTERS = 10 # ID \in [0,10]

# 3. Calcule bit 
# formula : 2^NUM_BITS > MAX_VOTERS
NUM_BITS = math.ceil(math.log2(MAX_VOTERS +1))

# 4. parameters for generating prime numbers (Paillier keygen)
# upper Bound and lower bound
PRIME_UPPER_BOUND = 1000
PRIME_LOWER_BOUND = 500

# 5. Caculate min value n
# total of plaintext's bits = NUM_CANDIDATES * NUM_BITS
# value n in paillier > max(total)
TOTAL_PLAINTEXT_BITS = NUM_CANDIDATES * NUM_BITS
MIN_N_VALUE = 2 ** TOTAL_PLAINTEXT_BITS

# 6. named file to save data --> bb.py
DATA_FILE = "ballot_box.json"
PUBLIC_KEY_FILE = "public_key.txt"

def print_config_summary():
    print("----E-Voting sysytem configuration----")
    print(f"Candidates: {NUM_CANDIDATES}")
    print(f"Max voters: {MAX_VOTERS}")
    print(f"Bits per candidate slot : {NUM_BITS} bits")
    print(f"Total required bits for plaintext : {TOTAL_PLAINTEXT_BITS} bits")
    print(f"Minium 'n' value required : {MIN_N_VALUE} ")

if __name__ == '__main__':
    print_config_summary()


