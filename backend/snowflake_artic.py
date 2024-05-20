import replicate
from dotenv import load_dotenv

load_dotenv()

def snowflake_rec(recomendation_query) -> str:
    input = {"prompt": recomendation_query,
            "temperature": 0.2}

    output = replicate.run("snowflake/snowflake-arctic-instruct",
                            input=input)
    return "".join(output)

if __name__ == '__main__':
    print(snowflake_rec("what is ai?"))