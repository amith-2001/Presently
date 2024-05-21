import replicate
from dotenv import load_dotenv
from head_extractor import head_returner
load_dotenv()

def snowflake_rec(recomendation_query) -> str:
    input = {"prompt": "act as a data analyst , recommend the type of plot which conveys the most data by taking in the df.head(). Output only 2 types of plot names in a list format. Note, answer should be in the format of ['plot1','plot2']"+ recomendation_query,
            "temperature": 0.2}

    output = replicate.run("snowflake/snowflake-arctic-instruct",
                            input=input)
    return "".join(output)

if __name__ == '__main__':
    print(snowflake_rec(head_returner()))