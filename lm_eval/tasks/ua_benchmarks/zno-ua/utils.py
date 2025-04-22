from functools import partial


choices = [
    "A",
    "B",
    "C",
    "D",
    "E"
]

def doc_to_text(example):
    
    question_text = example["question"]
    answer_options = example["answers"]
    formatted_question = "Питання: " + question_text + "\n" + "Варіанти відповіді:\n"
    for i, answer in enumerate(answer_options):
        letter = choices[i]
        formatted_question += f"{letter}. {answer}\n"
    formatted_question += "Відповідь:"
    return formatted_question

def doc_to_target(doc) -> int:
    
   return choices[doc['correct_answer']-1]



def process_docs(dataset, subject):
    return dataset.filter(lambda x: x["source"] == subject)


process_math = partial(process_docs, subject="math")
process_geography = partial(process_docs, subject="geography")
process_history = partial(process_docs, subject="history")
process_ukr = partial(process_docs, subject="ukrainian-language-and-literature")
