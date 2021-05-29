from myapp.source import app, views

route = app.add_url_rule

# --- Format ---

# route(
#     "",
#     endpoint="",
#     view_func=views.,
#     methods=["GET", "POST"]
# )

route(
    "/",
    endpoint="/",
    view_func=views.default,
    methods=["GET", "POST"]
)

route(
    "/search/title/<search_query>",
    endpoint="/search/title/<search_query>",
    view_func=views.search_title,
    methods=["GET"]
)

route(
    "/search/description/<search_query>",
    endpoint="/search/description/<search_query>",
    view_func=views.search_description,
    methods=["GET"]
)