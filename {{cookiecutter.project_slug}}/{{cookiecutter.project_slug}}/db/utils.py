def get_connect_args_for_sqlite(url):
    if url.dialect == "sqlite":
        return {"connect_args": {"check_same_thread": False}}
    else:
        return {}
