def load_prompt_text(prompt_name):
    with open(f'prompts/{prompt_name}.txt', 'r', encoding='utf-8') as f:
        return f.read()