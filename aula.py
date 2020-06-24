from aiohttp import web
from LeadConverter import LeadConverter
from TechBot import TechBot


async def handle(request):
    return web.Response(text=lead_converter.converter())


async def chat_bot_handle(request):
    if "question" in request.rel_url.query:
        question = request.rel_url.query['question']
        rsp = tech_bot.get_response(question)
        return web.Response(text=str(rsp))
    else:
        return web.Response(text="O param. question é obrigatório")

lead_converter = LeadConverter()
tech_bot = TechBot()
app = web.Application()
app.add_routes([web.get('/', handle), web.get("/chatbot", chat_bot_handle)])

if __name__ == '__main__':
    web.run_app(app)

