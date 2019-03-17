import json
import random
random.seed(1)
foo = ['a', 'b', 'c', 'd', 'e']

with open('hotpot_dev_distractor_v1.json', 'r') as f:
    hotpot_dev_distractor = json.load(f)


#[q['context'][1] if q['context'][0] in q['supporting_facts']] for q in random_questions
random_questions =  random.sample(hotpot_dev_distractor,5)
questions = [q['question'] for q in random_questions]
answers = [q['answer'] for q in random_questions]
context = []
for q in random_questions: #[ EXP for x in seq if COND ]
    true_context = [c[0] for c in q['supporting_facts']]
    list_context = []
    for c in q['context']:
        try:
            index = true_context.index(c[0])
        except:
            continue
        which_sen = q['supporting_facts'][index][1]
        list_context.append(c[1][which_sen])
    context.append(list_context)


questions_and_context = zip(questions,context,answers)
for q,c,a in questions_and_context:
    print(q)
    print(c)
    print(a)
    print()
    print()

