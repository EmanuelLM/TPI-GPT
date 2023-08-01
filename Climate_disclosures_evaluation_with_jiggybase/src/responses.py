
import jiggybase

def get_responses(collection, prompt_dict):
    for company_name, company_prompts in prompt_dict.items():
        for prompt_name, prompt_content in company_prompts.items():
            prompt_message = jiggybase.PromptMessage(
                content=prompt_content,
                role="user",
                position=1,
                extras=None,
            )

            task = org.create_prompt_task(
                name=prompt_name.replace(" ", "_"),
                version=1,
                prompts=[prompt_message],
                type=None,
                description=f"{company_name}_report"
            )

            response = collection._chat_completion(task.prompts, temperature=0, model="gpt-3.5-turbo")

            if response.choices:
                print(f"Response for {company_name}/{prompt_name}: {response.choices[0].message.content}")
            else:
                print(f"No response for {company_name}/{prompt_name}")
