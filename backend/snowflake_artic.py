import replicate
from dotenv import load_dotenv

load_dotenv()

input = {
    "prompt": "write a code to create a snake game using python",
    "temperature": 0.2
}

for event in replicate.stream(
    "snowflake/snowflake-arctic-instruct",
    input=input
):
    print(event, end="")
#=> "Fizz Buzz is a common programming problem that involves ...
