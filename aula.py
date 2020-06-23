from aiohttp import web
from LeadConverter import LeadConverter


async def handle(request):
    return web.Response(text=lead_converter.converter())

lead_converter = LeadConverter()
app = web.Application()
app.add_routes([web.get('/', handle)])

if __name__ == '__main__':
    web.run_app(app)

