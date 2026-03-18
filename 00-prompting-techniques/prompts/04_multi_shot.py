import sys
from pathlib import Path

# allow importing from the lesson module directory
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Tag each product with one category only:
Electronics, Clothing, Grocery, Furniture

Product: Wireless Bluetooth headphones with noise cancellation.
Category: Electronics

Product: Cotton t-shirt with round neck and short sleeves.
Category: Clothing

Product: Organic brown rice, 1kg pack.
Category: Grocery

Product: Wooden dining table with six chairs.
Category: Furniture

Product: Smartwatch with heart rate and sleep tracking.
Category: Electronics

Now tag this:
Product: Leather jacket with front zipper and side pockets.
Category:
"""


response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)
