
import json
import jiggybase

def generate_prompts(companies: list, template_path: str, output_path: str):
    with open(template_path, 'r') as file:
        template = file.read()

    prompts = template.split('Prompt ')[1:]

    company_prompts = {}

    for company in companies:
        company_prompts[company] = {}
        for prompt in prompts:
            prompt_number, prompt_text = prompt.split(" :", 1)
            prompt_text = prompt_text.replace('X', company)
            company_prompts[company][f'{company} Prompt {prompt_number}'] = prompt_text.strip()

    with open(output_path, 'w') as file:
        json.dump(company_prompts, file, indent=4)

def load_prompt_dictionary(dictionary_file_path: str):
    with open(dictionary_file_path, 'r') as file:
        prompt_dict = json.load(file)
    return prompt_dict

def create_prompt_tasks(org, prompt_dict):
    for company_name, company_prompts in prompt_dict.items():
        for prompt_name, prompt_content in company_prompts.items():
            prompt_message = jiggybase.PromptMessage(
                content=prompt_content,
                role="user",
                position=1,
                extras=None,
            )

            org.create_prompt_task(
                name=prompt_name.replace(" ", "_"),
                version=1,
                prompts=[prompt_message],
                type=None,
                description=f"{company_name}_report"
            )
