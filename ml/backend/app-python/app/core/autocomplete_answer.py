from app.utils.ollama_run import LlamaRun


def main(data):
    template = """Представь, что ты HR и тебе надо {target_action} кандидата. 
    Напиши текст, который можно отправить кандидату в мессенджер.
    Кандидата зовут {name}. Резюме кандидата: {summary}. 
    Вакансия: {position}. Описание вакансии: {description}.
    """
    model = LlamaRun(
        template="Представь, что ты HR и тебе надо кандидатом",
        ollama_url="https://useful-kite-settled.ngrok-free.app",
        model_name="llama3.1:8b",
        temperature=0
    )
    if data['target_action'] == "invite":
        text = model.run(template.format(name=data['name'],
                         target_action="пригласить",
                         position=data['position'],
                         summary=data['summary'],
                         description=data['description']),
                         )

    if data['target_action'] == "reject":
        text = model.run(dict(name=data['name'],
                         target_action="отказать",
                         position=data['position'],
                         summary=data['summary'],
                         description=data['description']),
                         )

    if data['target_action'] == "rotate":
        text = model.run(dict(name=data['name'],
                         target_action="предложить другую вакансию",
                         position=data['position'],
                         summary=data['summary'],
                         description=data['description']),
                         )

    return text