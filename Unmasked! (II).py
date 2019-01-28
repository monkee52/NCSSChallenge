# Enter your code for "Unmasked! (II)" here.
from collections import defaultdict
from string import punctuation

def process_text(filename):
  counts = defaultdict(int)  # {length: frequency}
  with open(filename) as f:
    for line in f:
      for word in line.strip().split():
        # Remove the external punctuation.
        word = word.strip(punctuation)
        if word:
          counts[len(word)] += 1
  return counts

def cosine_sim(a, b):
  # Makes one set that is the union of the lengths
  # in a and the lengths in b.
  lengths = set(a) | set(b)  
  # Perform cosine similarity as per the formula.
  num = sum(a[l] * b[l] for l in lengths)
  denom1 = sum(a[l]**2 for l in lengths)**0.5
  denom2 = sum(b[l]**2 for l in lengths)**0.5
  return num / (denom1 * denom2)

# Generate the counts mapping for each text, as
# well as unknown.txt.
counts = {}  # {filename: {length: frequency}}
with open('texts.txt') as f:
  for line in f:
    filename = line.strip()
    counts[filename] = process_text(filename)

unknown = process_text('unknown.txt')

# Calculate the cosine similarity values for all 
# texts and sort them appropriately.
scored = [(cosine_sim(v, unknown), k) for k, v in counts.items()]
scored.sort(reverse=True)

# Output the ordered texts with scores to 3dp.
for score, filename in scored:
  print('{0:.3f} {1}'.format(score, filename))
