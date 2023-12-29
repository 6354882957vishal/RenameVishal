# Don't Remove Credit @SUMIT_KING_2
# Subscribe YouTube Channel For Amazing Bot @King1_devil
# Ask Doubt on telegram @King1_devil

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("LazyDeveloper")


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
