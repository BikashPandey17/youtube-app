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