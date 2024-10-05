from utils.ollama_run import LlamaRun


def main(data):
    template = """Представь, что ты HR и тебе надо {target_action} кандидата.
    Его зовут {name}. Вакансия была {position}
    """
    model = LlamaRun(
        template=template,
        ollama_url="https://useful-kite-settled.ngrok-free.app",
        model_name="llama3.1:8b",
        temperature=0
    )
    if data['target_action'] == "invite":
        text = model.run(name=data['name'],
                         target_action="пригласить",
                         position=data['position'])

    if data['target_action'] == "reject":
        text = model.run(name=data['name'],
                         target_action="отказать",
                         position=data['position'])

    if data['target_action'] == "rotate":
        text = model.run(name=data['name'],
                         target_action="предложить другую вакансию",
                         position=data['position'])

    return text